from pygame.sprite import Sprite
from random import randint
from boo import Boo
import pygame
import sys
from shadow import Shadow
from settings import Settings
from time import sleep
from game_stats import GameStats
from button import Button
from scoreboard import Scoreboard
from music import Music


class TryIt:

    def __init__(self):
        """Initialize the TryIt game"""
        pygame.init()
        self.settings = Settings()

        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Try It!")

        self.shadow = Shadow(self)
        self.boos = pygame.sprite.Group()

        self.stats = GameStats(self)
        self.sb = Scoreboard(self)

        self.play_button = Button(self, "Play")

        self.timer = self.settings.timer

        self.music = Music()

    def run_game(self):
        """Main method of the game"""
        while True:
            self._check_events()

            if self.stats.game_active:
                self.shadow.update()
                self._create_boo()

            self._update_screen()

    def _check_events(self):
        """Checks key presses and mouse events"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                self._check_play_button(mouse_pos)

    def _check_play_button(self, mouse_pos):
        """Checks to see if the play button is pressed"""
        button_clicked = self.play_button.rect.collidepoint(mouse_pos)

        if not self.stats.game_active and button_clicked:
            self.stats.reset_stats()
            self.stats.game_active = True

            # Resets all the scoreboard attributes
            self.sb.prep_shadows_left()
            self.sb.prep_level()
            self.sb.prep_high_score()

            self.boos.empty()

            self._create_boo()
            self.shadow.center_shadow()
            self.settings.initialize_dynamic_settings()

            pygame.mouse.set_visible(False)

    def _check_keydown_events(self, event):
        """Check for key presses"""
        if event.key == pygame.K_RIGHT:
            self.shadow.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.shadow.moving_left = True
        elif event.key == pygame.K_q:
            sys.exit()
        elif event.key == pygame.K_SPACE:
            self.shadow.jump = True

    def _check_keyup_events(self, event):
        """Check for key releases"""
        if event.key == pygame.K_RIGHT:
            self.shadow.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.shadow.moving_left = False

    def _create_boo(self):
        """Method to randomly generate Boos"""
        boo = Boo(self)

        if len(self.boos) == 0:
            initial_start = True
        else:
            initial_start = False

        boo.x = float(randint(0, self.settings.screen_width))
        boo.rect.x = boo.x
        boo.y = float(randint(0, self.settings.screen_mid_y))
        boo.rect.y = boo.y

        if not initial_start:
            if len(self.boos) < self.settings.num_boos:
                    if not pygame.sprite.spritecollideany(boo, self.boos):
                        self.boos.add(boo)

        else:
            self.boos.add(boo)

    def _drop_boos(self):
        """Drop the boos further down the screen"""
        for boos in self.boos.sprites():
            boos.y += self.settings.boo_drop_speed
            boos.rect.y = boos.y
            self._check_collision()
            self._check_boo_hit_ground(boos)
            self._boo_counter()

    def _boo_counter(self):
        """Timer for every time a period of time passes, boo speed gets quicker"""
        if self.timer < 0:
            self.settings.increase_speed()
            self.timer = 10000
            # Add in next level...
            self.stats.level += 1
            self.sb.prep_level()
            self.sb.check_high_score()

        self.timer -= 1

    def _check_boo_hit_ground(self, boo):
        """Checks to see if the boo hit the ground"""
        screen_rect = self.screen.get_rect()
        if boo.rect.top >= screen_rect.bottom:
            self.boos.remove(boo)

    def _check_collision(self):
        """Checks to see if boo collided with player"""
        if pygame.sprite.spritecollideany(self.shadow, self.boos):
            self._shadow_hit()

    def _shadow_hit(self):
        """Respond to shadow being hit by boo"""
        if self.stats.shadow_lives_left > 0:
            self.stats.shadow_lives_left -= 1

            self.sb.prep_shadows_left()
            self._create_boo()
            self.shadow.center_shadow()
            # Pause
            sleep(0.5)
        else:
            self.stats.game_active = False
            pygame.mouse.set_visible(True)
        self.boos.empty()

    def _update_boos(self):
        """Updating the boos position on the screen"""
        self._drop_boos()
        self.boos.update()

    def _update_screen(self):
        """Redraws the screen to consistently have new items pop up"""
        self.screen.fill(self.settings.bg_color)
        self.shadow.blitme()
        self._update_boos()
        self.boos.draw(self.screen)

        # Draw the score information
        self.sb.show_elements()

        if not self.stats.game_active:
            self.play_button.draw_button()

        # Redraws the screen
        pygame.display.flip()


if __name__ == '__main__':
    try_it = TryIt()
    try_it.run_game()
