class Settings():
    """A class to store all settings for Alien Invasion."""

    def __init__(self):
        """Initialize game settings"""

        # General settings
        self.game_title = "Alien Invasion"

        # Screen settings
        self.screen_width = 1300
        self.screen_height = 900
        self.bg_color = (230, 230, 230)

        # Ship settings
        self.ship_speed_factor = 2.5

        # Bullets settings
        self.bullet_speed_factor = 1
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (255, 60, 60)
        self.bullets_allowed = 8
