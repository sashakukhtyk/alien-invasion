import sys
import pygame


class AlienInvasion:
    """Base class that regulates the game of Alien Invasion."""

    def __init__(self):
        """Initialize the game."""
        pygame.init()

        self.screen = pygame.display.set_mode((1200, 800))
        pygame.display.set_caption('Alien Invasion')

    def run_game(self):
        """Start the main game loop."""
        while True:
            # Listening for the mouse and keys
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            # Show last created display
            pygame.display.flip()


if __name__ == '__main__':
    # Create the example of game and run it
    ai = AlienInvasion()
    ai.run_game()
