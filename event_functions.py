import pygame
import statistics as stat


def check_events(settings, organisms):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit()
        elif event.type == pygame.KEYDOWN:
            check_control_events(event, settings, organisms)


def check_control_events(event, settings, organisms):
    if event.key == pygame.K_a:
        stat.print_organisms(organisms)
    elif event.key == pygame.K_o:
        stat.print_oldest_organism(organisms)
    elif event.key == pygame.K_s:
        stat.print_organisms_statistics(organisms)

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
        settings.environment.losses.common += 10
    elif event.key == pygame.K_F1:
        settings.environment.losses.common -= 10

    elif event.key == pygame.K_2:
        settings.environment.losses.move += 10
    elif event.key == pygame.K_F2:
        settings.environment.losses.move -= 10

    elif event.key == pygame.K_3:
        settings.environment.losses.sleep += 5
    elif event.key == pygame.K_F3:
        settings.environment.losses.sleep -= 5

    elif event.key == pygame.K_4:
        settings.environment.losses.sun_sun += 0.01
    elif event.key == pygame.K_F4:
        settings.environment.losses.sun_sun -= 0.01

    elif event.key == pygame.K_5:
        settings.environment.losses.eat_plant += 0.01
    elif event.key == pygame.K_F5:
        settings.environment.losses.eat_plant -= 0.01

    elif event.key == pygame.K_6:
        settings.environment.losses.eat_sun += 0.01
    elif event.key == pygame.K_F6:
        settings.environment.losses.eat_sun -= 0.01
