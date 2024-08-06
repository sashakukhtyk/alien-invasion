import sys
from time import sleep
import pygame

from settings import Settings
from game_stats import GameStats
from scoreboard import Scoreboard
from button import Button
from ship import Ship
from bullet import Bullet
from alien import Alien


class AlienInvasion:
    """Base class that regulates the game of Alien Invasion."""

    def __init__(self):
        """Initialize the game."""
        pygame.init()
        self.settings = Settings()

        # Window control
        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        self.settings.screen_width = self.screen.get_rect().width
        self.settings.screen_height = self.screen.get_rect().height
        pygame.display.set_caption('Alien Invasion')

        # Create a game statistics and a scoreboard
        self.stats = GameStats(self)
        self.sb = Scoreboard(self)

        # Initialize characters
        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()
        self.aliens = pygame.sprite.Group()

        self._create_fleet()

        # Create Play button
        self.play_button = Button(self, "Play")

    def run_game(self):
        """Start the main game loop."""
        while True:
            self._check_events()
            if self.stats.game_active:
                self.ship.update()
                self._update_bullets()
                self._update_aliens()

            self._update_screen()

    def _update_screen(self):
        """Update the screen at every step and show new screen"""
        self.screen.fill(self.settings.bg_color)

        # Update character images
        self.ship.blitme()
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        self.aliens.draw(self.screen)

        # Draw the scoreboard
        self.sb.show_score()

        # Draw the button if the game is inactive
        if not self.stats.game_active:
            self.play_button.draw_button()

        # Show last created display
        pygame.display.flip()

    def _check_events(self):
        """Listening for the mouse and keys"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)

            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)

            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                self._check_play_button(mouse_pos)

    def _check_play_button(self, mouse_pos):
        """Start new game when Play button is pressed"""
        button_clicked = self.play_button.rect.collidepoint(mouse_pos)
        if button_clicked and not self.stats.game_active:
            # Empty game stats
            self.settings.initialize_dynamic_settings()
            self.stats.reset_stats()
            self.stats.game_active = True
            self.sb.prep_score()

            # Empty bullets and aliens
            self.aliens.empty()
            self.bullets.empty()

            # Create new fleet and center the ship
            self._create_fleet()
            self.ship.center_ship()

            # Hide the mouse pointer
            pygame.mouse.set_visible(False)

    def _check_keydown_events(self, event):
        """Respond to keydown events."""
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True
        if event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        if event.key == pygame.K_q:
            sys.exit()
        if event.key == pygame.K_SPACE:
            self._fire_bullet()

    def _check_keyup_events(self, event):
        """Respond to keyup events."""
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        if event.key == pygame.K_LEFT:
            self.ship.moving_left = False

    def _fire_bullet(self):
        """Create a new bullet and add it to the bullets group."""
        if len(self.bullets) < self.settings.bullets_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)

    def _update_bullets(self):
        """Update the bullets group."""
        self.bullets.update()

        # Remove bullets that disappear
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)

        self._check_bullets_alien_collision()

    def _check_bullets_alien_collision(self):
        """
        Check collision between a bullet and alien
        Make collided rect disappears
        """
        collision = pygame.sprite.groupcollide(self.bullets, self.aliens, True, True)

        if collision:
            for aliens in collision.values():
                self.stats.score += self.settings.alien_points * len(aliens)

            self.sb.prep_score()
            self.sb.check_high_score()

        if not self.aliens:
            # Kill existing bullets and create new fleet
            self.bullets.empty()
            self._create_fleet()
            self.settings.increase_speed()

    def _create_fleet(self):
        """Create alien and add it to the fleet group."""
        # Create aliens and define how many of them in a row
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size
        available_space_x = self.settings.screen_width - (2 * alien_width)
        number_aliens_x = available_space_x // (2 * alien_width)

        # Define how many aliens could be on the screen
        ship_height = self.ship.rect.height
        available_space_y = (self.settings.screen_height - (3 * alien_height) - ship_height)
        number_rows = available_space_y // (2 * alien_height)

        # Create the first row of aliens
        for row_number in range(number_rows):
            for alien_number in range(number_aliens_x):
                # Create an alien and put it in a row
                self._create_alien(alien_number, row_number)

    def _create_alien(self, alien_number, row_number):
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size
        alien.x = alien_width + 2 * alien_width * alien_number
        alien.rect.x = alien.x
        alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number
        self.aliens.add(alien)

    def _check_fleet_edges(self):
        """Respond to fleet edge events."""
        for alien in self.aliens.sprites():
            if alien.check_edge():
                self._change_fleet_directions()
                break

    def _change_fleet_directions(self):
        """Change the fleet directions and its move down"""
        for alien in self.aliens.sprites():
            alien.rect.y += self.settings.fleet_drop_speed
        self.settings.fleet_direction *= -1

    def _update_aliens(self):
        """Update the alien group."""
        self._check_fleet_edges()
        self.aliens.update()

        # Look for ship aliens collision
        if pygame.sprite.spritecollideany(self.ship, self.aliens):
            self._ship_hit()

        # Look for alien to hit the bottom of the screen
        self._check_aliens_bottom()

    def _ship_hit(self):
        """Check if the ship is hit by aliens"""
        if self.stats.ships_left > 0:
            # Decrease ship_left
            self.stats.ships_left -= 1

            # Empty alien and bullets
            self.aliens.empty()
            self.bullets.empty()

            # Create new fleet and center the ship
            self._create_fleet()
            self.ship.center_ship()

            # Pause
            sleep(1.0)
        else:
            self.stats.game_active = False
            pygame.mouse.set_visible(True)

    def _check_aliens_bottom(self):
        """"Check if the aliens hit the bottom of the screen"""
        screen_rect = self.screen.get_rect()
        for alien in self.aliens.sprites():
            if alien.rect.bottom >= screen_rect.bottom:
                # React as ship hit by alien
                self._ship_hit()
                break


if __name__ == '__main__':
    # Create the example of game and run it
    ai = AlienInvasion()
    ai.run_game()
