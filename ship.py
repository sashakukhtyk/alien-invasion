import pygame


class Ship:
    """Class representing a ship"""
    def __init__(self, ai_game):
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect()

        # Download an image and get it rect
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()

        # Creating each new ship down the screen, centered
        self.rect.midbottom = self.screen_rect.midbottom

        # Save float number for ship position horizontally
        self.x = float(self.rect.x)

        # Move indication
        self.moving_right = False
        self.moving_left = False

    def blitme(self):
        """Blits the ship"""
        self.screen.blit(self.image, self.rect)

    def update(self):
        """Updates the ship position based on move indicator"""
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.ship_speed

        # update the rect position, because it can't take float number
        self.rect.x = self.x

    def center_ship(self):
        """Centers the ship"""
        self.rect.midbottom = self.screen_rect.midbottom
        self.x = float(self.rect.x)
