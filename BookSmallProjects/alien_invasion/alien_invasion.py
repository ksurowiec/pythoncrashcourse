import pygame

import game_functions as gf
from settings import Settings
from ship import Ship


def run_game():
    # Initialize game and create a screen object
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption(ai_settings.game_title)

    # Set the background color
    bg_color = (230, 230, 230)

    # Make a ship
    ship = Ship(ai_settings, screen)

    # Make an alien ships
    aliens = pygame.sprite.Group()

    # Make a group to store bullets in
    bullets = pygame.sprite.Group()

    gf.create_alien_fleet(ai_settings, screen, ship, aliens)

    # Start the main loop
    while True:
        gf.check_events(ai_settings, screen, ship, bullets)
        ship.update()
        # gf.update_bullets(bullets)
        gf.update_screen(ai_settings, screen, ship, aliens, bullets)


run_game()
