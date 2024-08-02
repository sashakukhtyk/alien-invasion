import sys
import pygame

from settings import Settings
from ship import Ship


class AlienInvasion:
    """Base class that regulates the game of Alien Invasion."""

    def __init__(self):
        """Initialize the game."""
        pygame.init()
        self.settings = Settings()

        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption('Alien Invasion')

        self.ship = Ship(self)

    def run_game(self):
        """Start the main game loop."""
        while True:
            self._check_events()

            # Repaint the screen on each iteration
            self.screen.fill(self.settings.bg_color)
            self.ship.blitme()

            # Show last created display
            pygame.display.flip()

    def _check_events(self):
        """Listening for the mouse and keys"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()


if __name__ == '__main__':
    # Create the example of game and run it
    ai = AlienInvasion()
    ai.run_game()
