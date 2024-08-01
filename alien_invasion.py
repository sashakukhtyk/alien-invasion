import sys
import pygame

from settings import Settings


class AlienInvasion:
    """Base class that regulates the game of Alien Invasion."""

    def __init__(self):
        """Initialize the game."""
        pygame.init()
        self.settings = Settings()

        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption('Alien Invasion')


    def run_game(self):
        """Start the main game loop."""
        while True:
            # Listening for the mouse and keys
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            # Repaint the screen on each iteration
            self.screen.fill(self.settings.bg_color)

            # Show last created display
            pygame.display.flip()


if __name__ == '__main__':
    # Create the example of game and run it
    ai = AlienInvasion()
    ai.run_game()
