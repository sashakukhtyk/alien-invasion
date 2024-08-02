import pygame


class Ship:
    """Class representing a ship"""
    def __init__(self, ai_game):
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()

        # Download an image and get it rect
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()

        # Creating each new ship down the screen, centered
        self.rect.midbottom = self.screen_rect.midbottom

        # Move indication
        self.moving_right = False

    def blitme(self):
        """Blits the ship"""
        self.screen.blit(self.image, self.rect)

    def update(self):
        """Updates the ship position based on move indicator"""
        if self.moving_right:
            self.rect.x += 1
