class GameStats:
    """Tracks statistics for Try It."""

    def __init__(self, ti_game):
        """Initialize statistics."""
        self.settings = ti_game.settings
        self.reset_stats()

        self.game_active = False
        self.high_score = 1

    def reset_stats(self):
        """Initialize statistics that can change during the game."""
        self.shadow_lives_left = self.settings.shadow_lives_left
        self.level = 1
