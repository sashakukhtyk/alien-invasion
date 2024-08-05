import pygame.font


class Scoreboard:
    """Initialize attributes and methods of score"""
    def __init__(self, ai_game):
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()
        self.settings = ai_game.settings
        self.stats = ai_game.stats

        # Font settings for score
        self.text_color = (30, 30, 30)
        self.font = pygame.font.SysFont(None, 48)

        # Prepre the image of starting score
        self.prep_score()

    def prep_score(self):
        pass