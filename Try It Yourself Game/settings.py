
class Settings:
    """Controls all the games settings"""

    def __init__(self):
        """Contains all the screen settings"""
        # Screen settings
        self.screen_width = 1200
        self.screen_height = 800
        # Red, Green, Blue
        self.bg_color = (0, 180, 230)
        self.screen_ground_y = 706
        self.screen_mid_y = 400

        # Shadow settings
        self.shadow_speed = 1.5
        self.shadow_jump = 3
        self.shadow_lives_left = 3

        # Boo settings
        self.num_boos = 5
        self.boo_drop_speed = .3
        self.boo_direction = 1

        # Dynamic settings
        self.speedup_speed = 1.1
        self.initialize_dynamic_settings()

        # Timer settings
        self.timer = 10000

    def initialize_dynamic_settings(self):
        """Initialize dynamic settings."""
        self.shadow_speed = 1.5
        self.boo_drop_speed = .3

    def increase_speed(self):
        """Increase the speed of various objects."""
        self.shadow_speed *= self.speedup_speed
        self.boo_drop_speed *= self.speedup_speed

