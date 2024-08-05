class GameStats:
    """Statistics of the game"""
    def __init__(self, ai_game):
        """Initialize statistics of the game"""
        self.settings = ai_game.settings
        self.reset_stats()

        # Start the active game
        self.game_active = False

    def reset_stats(self):
        """Initialize statistics of the game, that can be changed through the game"""
        self.ships_left = self.settings.ship_limit
