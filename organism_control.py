import pygame


def check_organism_control_keydown(event, settings, organisms):
    organism = get_control_organism(organisms)
    if event.key == pygame.K_RIGHT:
        organism.active_gens = [6]
    if event.key == pygame.K_LEFT:
        organism.active_gens = [4]
    if event.key == pygame.K_UP:
        organism.active_gens = [2]
    if event.key == pygame.K_DOWN:
        organism.active_gens = [8]

    if event.key == pygame.K_p:
        if organism.active_gens == [0]:
            organism.active_gens = [5]
        else:
            organism.active_gens = [0]

    if event.key == pygame.K_g:
        set_active_gens(organism)


def check_organism_control_keyup(event, settings, organisms):
    organism = get_control_organism(organisms)
    if event.key == pygame.K_RIGHT or event.key == pygame.K_LEFT or\
            event.key == pygame.K_UP or event.key == pygame.K_DOWN:
        organism.active_gens = [5]


def get_control_organism(organisms):
    for organism in organisms:
        if organism.remote:
            return organism


def set_active_gens(organism):
    pass