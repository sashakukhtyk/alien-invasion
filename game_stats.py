class GameStats:
    """Statistics of the game"""
    def __init__(self, ai_game):
        """Initialize statistics of the game"""
        self.ai_settings = ai_game.settings
        self.reset_stats()

        # Start the active game
        self.game_active = False

        # High score initialization
        self.high_score = 0

    def reset_stats(self):
        """Initialize statistics of the game, that can be changed through the game"""
        self.ships_left = self.ai_settings.ship_limit
        self.score = 0
        self.level = 1

