import pygame
from settings import Settings
import constantes as const
from display import show_records
from event_functions import check_events
from main_functions import perform_actions


def main():
    settings = Settings()

    pygame.init()
    screen = pygame.display.set_mode((settings.screen_width + 220, settings.screen_height))
    pygame.display.set_caption(const.caption)
    clock = pygame.time.Clock()
    cycle_count = 0

    font = pygame.font.Font(None, 24)

    organisms = [const.first_organism]

    while True:
        clock.tick(settings.fps)
        screen.fill(settings.bg_color)
        pygame.draw.rect(screen, settings.environment.border_color,
                         (0, 0, settings.environment.width, settings.environment.height),
                         settings.environment.border_size)
        check_events(settings, organisms)
        show_records(screen, cycle_count, settings, font, organisms)

        for organism in organisms:
            organism.draw(screen, settings)
            if settings.run:
                perform_actions(organism, organisms, settings)

        if settings.run:
            cycle_count += 1

        pygame.display.flip()


main()
