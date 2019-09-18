import pygame.font
from pygame.sprite import Group
from shadow import Shadow


class Scoreboard:
    """A class that manages the scoreboad"""

    def __init__(self, ti_game):
        """Initializes the scoreboard class."""
        self.ti_game = ti_game
        self.screen = ti_game.screen
        self.screen_rect = self.screen.get_rect()
        self.settings = ti_game.settings
        self.stats = ti_game.stats

        self.text_color = (30, 30, 30)
        self.font = pygame.font.SysFont(None, 36)

        self.prep_level()
        self.prep_high_score()
        self.prep_shadows_left()

    def prep_level(self):
        """Render and show the current level of the game."""
        level_str = "Level: " + str(self.stats.level)
        self.level_image = self.font.render(level_str, True, self.text_color, self.settings.bg_color)

        self.level_rect = self.level_image.get_rect()
        self.level_rect.top = 20
        self.level_rect.right = self.screen_rect.right - 20

    def prep_high_score(self):
        """Render and show the high score of the game"""
        high_score_str = "High Score: " + str(self.stats.high_score)
        self.high_score_image = self.font.render(high_score_str, True, self.text_color, self.settings.bg_color)

        self.high_score_rect = self.high_score_image.get_rect()
        self.high_score_rect.top = 20
        self.high_score_rect.centerx = self.screen_rect.centerx

    def prep_shadows_left(self):
        """Show how many Shadows are left."""
        self.shadows = Group()

        for shadow_number in range(self.stats.shadow_lives_left):
            shadow = Shadow(self.ti_game)
            shadow.rect.x = 10 + shadow_number * shadow.rect.width
            shadow.rect.y = 10
            self.shadows.add(shadow)

    def show_elements(self):
        """Draws the elements to the screen."""
        self.screen.blit(self.high_score_image, self.high_score_rect)
        self.screen.blit(self.level_image, self.level_rect)
        self.shadows.draw(self.screen)

    def check_high_score(self):
        """Checks to see if there is a new high score."""
        if self.stats.level > self.stats.high_score:
            self.stats.high_score = self.stats.level
            self.prep_high_score()
