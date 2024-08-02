import pygame


class Skeleton:
    """Class that represents a Skeleton."""
    def __init__(self, ai_game):
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()

        # Download an image and get it rect
        self.image = pygame.image.load('images/skeleton.bmp')
        self.rect = self.image.get_rect()

        # Creating each new skeleton at the center of the screen
        self.rect.center = self.screen_rect.center

    def blitme(self):
        """Blits the skeleton"""
        self.screen.blit(self.image, self.rect)
