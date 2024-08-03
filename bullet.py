import pygame
from pygame.sprite import Sprite


class Bullet(Sprite):
    """A class that represents a bullet."""
    def __init__(self, ai_game):
        """Initialize the bullet."""
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.color = self.settings.bullet_color

        # Create a bullet rect and put it in position
        self.rect = pygame.Rect(0, 0, self.settings.bullet_width, self.settings.bullet_height)
        self.rect.midtop = ai_game.ship.rect.midtop

        # Save bullet position as a float number
        self.y = float(self.rect.y)

    def update(self):
        pass

    def draw_bullet(self):
        pass
