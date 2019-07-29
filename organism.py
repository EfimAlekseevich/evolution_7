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
from random import randint, choice


class Organism:

    def __init__(self, x, y, active_gens, nervous_system, passive_gens, parent_generation):
        self.nervous_system = nervous_system
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
        out_info = '=' * 10 + ' ORGANISM ' + 10 * '=' + '\n'
        a_gens = " ".join(map(str, self.active_gens))
        out_info += f'Age = {str(self.age)}, Generation = {str(self.generation)}\n' \
            f'Passive gens: \n{str(self.passive_gens)}\nActive gens: {a_gens}' \
            f'Nervous system: {str(self.nervous_system)}'
        return f'{out_info}\n'

    def full_mutation(self, settings):
        self.gen_count = 0
        self.nervous_system.mutation(settings.strong_mutation)
        self.passive_gens.mutation(settings.strong_mutation)
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
        heir = Organism(self.x + randint(10, 20) * choice((1, -1)), self.y + randint(-20, 20),
                        self.active_gens.copy(), deepcopy(self.nervous_system),
                        deepcopy(self.passive_gens), self.generation)
        heir.full_mutation(settings)
        return heir

    def get_active_gen(self, settings):
        action = self.get_reaction(settings)
        if not action:
            if self.gen_count > len(self.active_gens) - 1:
                self.gen_count = 0
            action = self.active_gens[self.gen_count]
            self.gen_count += 1
        return action

    def get_color(self, settings):
        color = []
        coefficient_health = self.health / settings.max_health
        for spectrum in self.passive_gens.nutrition.values():
            color.append(int(spectrum * coefficient_health))
        return color

    def get_reaction(self, settings):
        responses = []
        for weights_set in self.nervous_system.weights_sets:
            excitation = weights_set[0] * settings.environment.sun / 10 + \
                         weights_set[1] * self.nervous_system.x + weights_set[2] * self.nervous_system.y + \
                         weights_set[3] * self.passive_gens.nutrition['meat'] + \
                         weights_set[4] * self.passive_gens.nutrition['sun'] + \
                         weights_set[5] * self.passive_gens.nutrition['plant'] + \
                         weights_set[6] * self.passive_gens.speed + weights_set[7] * self.passive_gens.size + \
                         weights_set[8] * self.passive_gens.protection + weights_set[9] * self.passive_gens.strong
            responses.append(excitation)
        self.nervous_system.update_xy()
        best_response = max(responses)
        if best_response > settings.threshold:
            return responses.index(best_response)

    def draw(self, screen, settings):
        pygame.draw.circle(screen, self.get_color(settings), (self.x, self.y), self.radius)
