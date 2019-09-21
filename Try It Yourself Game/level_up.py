import pygame.font


class LevelUp:
    """A class for the rectangular box that will show across the screen everytime you level up."""

    def __init__(self, ti_game):
        """Initializes the level up class."""
        self.screen = ti_game.screen
        self.screen_rect = self.screen.get_rect()

        self.settings = ti_game.settings
        self.stats = ti_game.stats
        # Idea -- for timer, as it goes down to a certain number, make the box smaller
        self.timer = 10000

        self.text_color = (30, 30, 30)
        self.font = pygame.font.SysFont(None, 36)

        self.prep_level_up()
        self.show_level_up()

    def prep_level_up(self):
        """Preps the level up rectangle and renders it."""
        level_up_str = "Level Up!"
        self.level_up_image = self.font.render(level_up_str, True, self.text_color, self.settings.bg_color)

        self.level_up_rect = self.level_up_image.get_rect()
        self.level_up_rect.x = self.screen_rect.centerx
        self.level_up_rect.y = self.screen_rect.centery

        # Size is a tuple of width, height
        self.level_up_rect.size = 100, 100

        # Immidiately start decreasing the size of level_up rectangle
        self.decrease_level_up_size()

    def show_level_up(self):
        """Draws the level up rectangle to the screen."""
        self.screen.blit(self.level_up_image, self.level_up_rect)

    def decrease_level_up_size(self):
        """Decreases the size of level up"""
        while self.timer > 1:
            self.show_level_up()
            print(str(self.level_up_rect.size))
            self.timer -= 1


