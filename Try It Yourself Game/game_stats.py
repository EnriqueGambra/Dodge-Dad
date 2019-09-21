class GameStats:
    """Tracks statistics for Try It."""

    def __init__(self, ti_game):
        """Initialize statistics."""
        self.settings = ti_game.settings
        self.reset_stats()

        self.game_active = False

        self.high_score = 1
        self.past_high_score()

    def reset_stats(self):
        """Initialize statistics that can change during the game."""
        self.shadow_lives_left = self.settings.shadow_lives_left
        self.level = 1

    def past_high_score(self):
        """Checks the high_score file to see if there is a past high score."""
        filename = "high_score.txt"
        try:
            with open(filename, 'r') as file_object:
                self.high_score = int(file_object.read())
        except FileNotFoundError:
            with open(filename, 'w') as file_object:
                file_object.write(str(self.high_score))

    def write_high_score(self):
        """Writes the high score to a file."""
        filename = "high_score.txt"
        with open(filename, 'w') as file_object:
            file_object.write(str(self.high_score))
