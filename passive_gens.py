from random import randint, choice


class PassiveGens:

    def __init__(self):
        self.nutrition = {'meat': 85, 'sun': 85, 'plant': 85}

        self.speed = 5
        self.size = 5

        self.protection = 5
        self.strong = 5

        self.strong_mutation = 10

    def __str__(self):
        out_info = ''
        for key, value in self.nutrition.items():
            out_info += f'{key}: {str(value)},'
        out_info += f'\nSpeed = {str(self.speed)}, Size = {str(self.size)}' \
            f'\nProtection = {str(self.protection)}, Strong = {str(self.strong)}'
        return out_info

    def mutation(self, settings):
        self.nutrition_mutation(self.strong_mutation + settings.strong_mutation)
        change = randint(-1, 1)
        self.speed_size_mutation(change)
        change = randint(-1, 1)
        self.protection_strong_mutation(change)

    def nutrition_mutation(self, strong_mutation):
        change = randint(-strong_mutation, strong_mutation)
        parameter1 = choice(list(self.nutrition.keys()))
        parameter2 = choice(list(self.nutrition.keys()))
        self.nutrition[parameter1] += change
        self.nutrition[parameter2] -= change
        if (self.nutrition[parameter1] < 1 or self.nutrition[parameter1] > 255) or (
                self.nutrition[parameter2] < 1 or self.nutrition[parameter2] > 255):
            self.nutrition[parameter1] -= change
            self.nutrition[parameter2] += change
            self.strong_mutation = 1

    def speed_size_mutation(self, change):
        self.speed += change
        self.size -= change
        if self.speed < 1 or self.speed > 9:
            self.speed -= change
            self.size += change

    def protection_strong_mutation(self, change):
        self.strong += change
        self.protection -= change
        if self.protection < 1 or self.protection > 9:
            self.strong -= change
            self.protection += change
