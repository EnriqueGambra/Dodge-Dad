import pygame
from pygame.sprite import Sprite


class Shadow(Sprite):
    """Class that represents the Shadow object"""

    def __init__(self, ti_game):
        """Initializes Shadow's attributes"""
        super().__init__()
        self.settings = ti_game.settings

        self.screen = ti_game.screen
        self.screen_rect = self.screen.get_rect()

        self.image = pygame.image.load('images/Mom2.bmp')
        self.rect = self.image.get_rect()

        self.rect.midbottom = self.screen_rect.midbottom

        self.moving_left = False
        self.moving_right = False
        self.jump = False

        self.jump_count = 100

        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

    def update(self):
        """Updates Shadow's current position"""
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.shadow_speed
        if self.moving_left and self.rect.x > 0:
            self.x -= self.settings.shadow_speed
        if self.jump:
            self._shadow_jump()

        self.rect.y = self.y
        self.rect.x = self.x

    def _shadow_jump(self):
        if self.jump_count >= -100:
            neg = 1
            if self.jump_count < 0:
                neg = -1
            self.y -= (self.settings.shadow_jump ** 2) * 0.2 * neg
            self.jump_count -= 1
        else:
            self.jump_count = 100
            self.jump = False
            self.rect.midbottom = self.screen_rect.midbottom
            self.y = float(self.rect.y)

    def center_shadow(self):
        """Centers shadow to the middle of the screen on restart."""
        self.jump = False
        self.rect.midbottom = self.screen_rect.midbottom
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

    def blitme(self):
        """Redraws Shadow to the screen, constantly updating his image."""
        self.screen.blit(self.image, self.rect)
