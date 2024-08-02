import sys
import pygame

from settings import Settings
from ship import Ship
from skeleton import Skeleton


class AlienInvasion:
    """Base class that regulates the game of Alien Invasion."""

    def __init__(self):
        """Initialize the game."""
        pygame.init()
        self.settings = Settings()

        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption('Alien Invasion')

        # Initialize characters
        self.ship = Ship(self)
        self.skeleton = Skeleton(self)

    def run_game(self):
        """Start the main game loop."""
        while True:
            self._check_events()
            self._update_screen()

    def _check_events(self):
        """Listening for the mouse and keys"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    self.ship.rect.x += 1

    def _update_screen(self):
        """Update the screen at every step and show new screen"""
        self.screen.fill(self.settings.bg_color)

        # Update character images
        self.ship.blitme()
        self.skeleton.blitme()

        # Show last created display
        pygame.display.flip()


if __name__ == '__main__':
    # Create the example of game and run it
    ai = AlienInvasion()
    ai.run_game()
