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
    ship = Ship(screen)

    # Start the main loop
    while True:
        gf.check_events(ship)
        gf.update_screen(ai_settings, screen, ship)


run_game()
