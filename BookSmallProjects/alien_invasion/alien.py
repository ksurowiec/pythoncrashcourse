import pygame
from pygame.sprite import Sprite


class Alien(Sprite):
    """A class to represent a single alien in the fleet"""

    def __init__(self, ai_settings, screen):
        super().__init__()
        self.screen = screen
        self.ai_settings = ai_settings

        # Load alien ship image and set its rect attribute
        self.image = pygame.image.load('images/romulan.png')
        self.rect = self.image.get_rect()

        # Start each new alien near the top left of the screen
        self.rect.x = self.rect.width / 2
        self.rect.y = self.rect.height / 2

        # Store the aliens exact position
        self.x = float(self.rect.x)

    def blitme(self):
        """Draw the alien ship"""
        self.screen.blit(self.image, self.rect)

    def update(self):
        self.x += (self.ai_settings.alien_speed_factor * self.ai_settings.alien_fleet_direction)
        self.rect.x = self.x

    def check_edged(self):
        screen_rect = self.screen.get_rect()

        if self.rect.right >= screen_rect.right:
            return True
        elif self.rect.left < 0:
            return True
