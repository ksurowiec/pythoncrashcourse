import sys
from time import sleep
import pygame
from bullet import Bullet
from alien import Alien


def check_events(ai_settings, screen, stats, play_button, ship, aliens, bullets):
    # Watch for keyboard and mouse events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, ai_settings, screen, ship, bullets)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            check_play_button(ai_settings, screen, stats, play_button, ship, aliens, bullets, mouse_x, mouse_y)


def check_keydown_events(event, ai_settings, screen, ship, bullets):
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True
    elif event.key == pygame.K_UP:
        ship.moving_up = True
    elif event.key == pygame.K_DOWN:
        ship.moving_down = True
    elif event.key == pygame.K_SPACE:
        fire_bullets(ai_settings, bullets, screen, ship)
    elif event.key == pygame.K_q:
        sys.exit()


def check_keyup_events(event, ship):
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False
    elif event.key == pygame.K_UP:
        ship.moving_up = False
    elif event.key == pygame.K_DOWN:
        ship.moving_down = False


def update_screen(ai_settings, stats, screen, ship, aliens, bullets, play_button):
    # Redraw the screen during each pass through the loop
    screen.fill(ai_settings.bg_color)

    aliens.update()

    # Update ship position
    ship.update()

    # Draw the ship
    ship.blitme()

    # Draw alien fleet
    aliens.draw(screen)

    # Update alien fleet position
    check_alien_fleet_edges(ai_settings, aliens)

    if stats.game_active:
        # Redraw all bullets behind ship and aliens
        update_bullets(ai_settings, screen, ship, bullets, aliens)

        if pygame.sprite.spritecollideany(ship, aliens):
            ship_hit(ai_settings, stats, screen, ship, aliens, bullets)
    else:
        play_button.draw_button()

    # Make the most recently drawn screen visible
    pygame.display.flip()


def check_play_button(ai_settings, screen, stats, play_button, ship, aliens, bullets, mouse_x, mouse_y):
    button_clicked = play_button.rect.collidepoint(mouse_x, mouse_y)

    if button_clicked and not stats.game_active:
        stats.reset_stats()
        stats.game_active = True
        pygame.mouse.set_visible(False)

        aliens.empty()
        bullets.empty()

        create_alien_fleet(ai_settings, screen, ship, aliens)
        ship.center_ship()


def ship_hit(ai_settings, stats, screen, ship, aliens, bullets):
    """Respond to ship being hit by alien."""

    if stats.ships_left > 1:
        # Decrement ships left
        stats.ships_left -= 1

        # Empty the list of aliens and bullets
        aliens.empty()
        bullets.empty()

        # Create a new fleet and center the ship
        create_alien_fleet(ai_settings, screen, ship, aliens)
        ship.center_ship()

        sleep(0.5)
    else:
        stats.game_active = False
        ai_settings.ship_speed_factor = 0
        ai_settings.alien_speed_factor = 0
        pygame.mouse.set_visible(True)


def fire_bullets(ai_settings, bullets, screen, ship):
    if len(bullets) < ai_settings.bullets_allowed:
        left_bullet = Bullet(ai_settings, screen, ship)
        left_bullet.rect.centerx = ship.rect.left
        right_bullet = Bullet(ai_settings, screen, ship)
        right_bullet.rect.centerx = ship.rect.right
        bullets.add(left_bullet)
        bullets.add(right_bullet)


def update_bullets(ai_settings, screen, ship, bullets, aliens):
    # Redraw all bullets behind ship and aliens
    for bullet in bullets.sprites():
        bullet.draw_bullet()

    bullets.update()
    # Get rid of the bullets that have disappeared
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)

    check_bullet_alien_collisions(ai_settings, aliens, bullets, screen, ship)


def check_bullet_alien_collisions(ai_settings, aliens, bullets, screen, ship):
    # Check for any bullets that have hit aliens.
    # If so, get rid of the bullet and the alien.
    collisions = pygame.sprite.groupcollide(bullets, aliens, True, True)
    if len(aliens) == 0:
        # Destroy existing bullets and create new fleet.
        bullets.empty()
        create_alien_fleet(ai_settings, screen, ship, aliens)


def get_number_rows(ai_settings, ship_height, alien_heigh):
    available_space_y = (ai_settings.screen_width - (3 * alien_heigh) - ship_height)
    number_rows = int(available_space_y / (2 * alien_heigh))
    return number_rows


def get_number_aliens_x(ai_settings, alien_width):
    available_space_x = ai_settings.screen_width - 2 * alien_width
    number_of_aliens_x = int(available_space_x / (2 * alien_width))
    return number_of_aliens_x


def create_alien(ai_settings, screen, column_number, row_number):
    alien = Alien(ai_settings, screen)
    alien_width = alien.rect.width
    alien.x = alien_width + 2 * alien_width * column_number
    alien.rect.x = alien.x
    # alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number
    alien.rect.y = 80 + (alien.rect.height + (alien.rect.height / 5)) * row_number
    return alien


def create_alien_fleet(ai_settings, screen, ship, aliens):
    alien = Alien(ai_settings, screen)
    number_of_aliens = get_number_aliens_x(ai_settings, alien.rect.width)
    number_rows = get_number_rows(ai_settings, ship.rect.height, alien.rect.height)

    for row_index in range(number_rows):
        for column_index in range(number_of_aliens):
            new_alien = create_alien(ai_settings, screen, column_index, row_index)
            aliens.add(new_alien)


def change_alien_fleet_direction(ai_settings, aliens):
    for alien in aliens.sprites():
        alien.rect.y += ai_settings.alien_fleet_drop_speed

    ai_settings.alien_fleet_direction *= -1


def check_alien_fleet_edges(ai_settings, aliens):
    for alien in aliens.sprites():
        if alien.check_edged():
            change_alien_fleet_direction(ai_settings, aliens)
            break
