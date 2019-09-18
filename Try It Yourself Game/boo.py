from pygame.sprite import Sprite
import pygame


class Boo(Sprite):
    """This class creates has everything to do with a Boo object"""

    def __init__(self, ti_game):
        super().__init__()
        self.screen = ti_game.screen
        self.settings = ti_game.settings

        self.image = pygame.image.load('images/Dad.bmp')
        self.rect = self.image.get_rect()

        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

    def update(self):
        """Update boo's position."""
        self.y += self.settings.boo_drop_speed
        self.rect.y = self.y

