import pygame
import statistics as stat
from main_functions import give_birth
from organism_control import check_organism_control_keydown, check_organism_control_keyup


def check_events(settings, organisms):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            settings.stat_file.close()
            quit()
        elif event.type == pygame.KEYDOWN:
            check_organism_control_keydown(event, settings, organisms)
            check_control_events(event, settings, organisms)
        elif event.type == pygame.KEYUP:
            check_organism_control_keyup(event, settings, organisms)


def check_control_events(event, settings, organisms):
    if event.key == pygame.K_a:
        stat.print_organisms(organisms)
    elif event.key == pygame.K_o:
        stat.print_oldest_organism(organisms)
    elif event.key == pygame.K_s:
        stat.print_organisms_statistics(organisms, len(organisms))

    elif event.key == pygame.K_0:
        settings.__init__()
    elif event.key == pygame.K_SPACE:
        if settings.run:
            settings.run = False
        else:
            settings.run = True

    elif event.key == pygame.K_KP4 and settings.environment.sun:
            settings.environment.sun -= 1
            settings.update_bg_color()
    elif event.key == pygame.K_KP6 and settings.environment.sun < 100:
            settings.environment.sun += 1
            settings.update_bg_color()

    elif event.key == pygame.K_KP2 and settings.fps:
            settings.fps -= 1
    elif event.key == pygame.K_KP8:
            settings.fps += 1

    elif event.key == pygame.K_1:
        settings.max_health += 10000
    elif event.key == pygame.K_F1 and settings.max_health > 10000:
        settings.max_health -= 10000
        for organism in organisms:
            if organism.health > settings.max_health:
                give_birth(organism, organisms, settings)

    elif event.key == pygame.K_2:
        settings.parent_health += 0.01
    elif event.key == pygame.K_F2 and settings.parent_health > 0.01:
        settings.parent_health -= 0.01

    elif event.key == pygame.K_3:
        settings.heir_health += 0.01
    elif event.key == pygame.K_F3 and settings.heir_health > 0.01:
        settings.heir_health -= 0.01

    elif event.key == pygame.K_4:
        settings.environment.losses.common += 10
    elif event.key == pygame.K_F4:
        settings.environment.losses.common -= 10

    elif event.key == pygame.K_5:
        settings.environment.losses.move += 10
    elif event.key == pygame.K_F5:
        settings.environment.losses.move -= 10

    elif event.key == pygame.K_6:
        settings.environment.losses.sleep += 5
    elif event.key == pygame.K_F6:
        settings.environment.losses.sleep -= 5

    elif event.key == pygame.K_7:
        settings.environment.losses.sun_sun += 0.01
    elif event.key == pygame.K_F7:
        settings.environment.losses.sun_sun -= 0.01

    elif event.key == pygame.K_8:
        settings.environment.eat_plant += 0.01
    elif event.key == pygame.K_F8:
        settings.environment.eat_plant -= 0.01

    elif event.key == pygame.K_9:
        settings.environment.eat_sun += 0.01
    elif event.key == pygame.K_F9:
        settings.environment.eat_sun -= 0.01

    elif event.key == pygame.K_KP_PLUS:
        settings.strong_mutation += 1
    elif event.key == pygame.K_KP_MINUS and settings.strong_mutation > 1:
        settings.strong_mutation -= 1
