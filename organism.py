"""
active_gens:
 0 - photosinthesis
 1~9 - turn (5-sleeping)
|1|2|3|
|4|O|6|
|7|8|9|
"""

import pygame
from copy import deepcopy
from random import randint


class Organism:

    def __init__(self, x, y, active_gens, passive_gens, parent_generation):
        self.active_gens = active_gens
        self.passive_gens = passive_gens
        self.x = x
        self.y = y
        self.radius = passive_gens.size + 5

        self.health = 60000
        self.gen_count = 0
        self.age = 0

        self.generation = parent_generation + 1

    def __str__(self):
        out_info = '='*10 + ' ORGANISM ' + 10*'=' + '\n'
        out_info += f'Age = {str(self.age)}, Generation = {str(self.generation)}\n' \
            f'Passive gens: \n{str(self.passive_gens)}\nActive gens: '
        for gen in self.active_gens:
            out_info += str(gen) + ' '

        return f'{out_info}\n'

    def full_mutation(self, settings):
        self.gen_count = 0
        self.passive_gens.mutation(settings)
        self.active_gens_mutation()

    def active_gens_mutation(self):
        change_length = randint(-1, 1)
        if change_length > 0:
            self.active_gens.append(randint(0, 9))
        elif change_length < 0 and len(self.active_gens) > 1:
            del self.active_gens[randint(0, len(self.active_gens) - 1)]
        else:
            self.active_gens[randint(0, len(self.active_gens) - 1)] = randint(0, 9)

    def get_heir(self, settings):
        heir = Organism(self.x+randint(-20, 20), self.y+randint(-20, 20),
                        self.active_gens.copy(), deepcopy(self.passive_gens), self.generation + 1)
        heir.full_mutation(settings)
        return heir

    def get_active_gen(self):
        if self.gen_count > len(self.active_gens) - 1:
            self.gen_count = 0
        action = self.active_gens[self.gen_count]
        self.gen_count += 1
        return action

    def update_radius(self, settings):
        coefficient_health = 2 * self.health / settings.max_health
        self.radius = int(coefficient_health * self.passive_gens.size) + 2

    def get_color(self, settings):
        color = []
        coefficient_health = self.health / settings.max_health
        for spectrum in self.passive_gens.nutrition.values():
            color.append(int(spectrum * coefficient_health))
        return color

    def draw(self, screen, settings):
        self.update_radius(settings)
        pygame.draw.circle(screen, self.get_color(settings), (self.x, self.y), self.radius)
