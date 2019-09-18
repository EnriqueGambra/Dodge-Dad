import pygame.font


class Button:
    """A class for the play button"""

    def __init__(self, ti_game, msg):
        """Initialize play button settings"""
        self.screen = ti_game.screen
        self.screen_rect = self.screen.get_rect()

        self.height, self.width = 200, 50
        self.text_color = (0, 0, 255)
        self.button_color = (0, 0, 100)
        self.font = pygame.font.SysFont(None, 48)

        self.rect = pygame.Rect(0, 0, self.height, self.width)
        self.rect.center = self.screen_rect.center

        self._prep_msg(msg)

    def _prep_msg(self, msg):
        """Turns text into a rendered image and centers text on the button"""
        self.msg_image = self.font.render(msg, True, self.text_color, self.button_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.screen_rect.center

    def draw_button(self):
        # Draw blank button and then draw message
        self.screen.fill(self.button_color, self.rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)

