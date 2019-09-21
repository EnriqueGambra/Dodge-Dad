import pygame


class Music:
    """Adds music to our game."""

    def __init__(self):
        """Initializes the music class."""
        self.sound = 'sounds\RideOfTheValkyries.mp3'
        pygame.mixer.music.load(self.sound)
        pygame.mixer.music.play(-1)


