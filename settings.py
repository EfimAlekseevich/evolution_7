from environment import Environment
from statistics import get_stat_file, get_organisms_statistics


class Settings:
    def __init__(self):

        self.screen_width = 360
        self.screen_height = 360
        self.text_color = (0, 50, 0)
        self.bg_color = None
        self.brightness = 1

        self.fps = 5
        self.run = True

        self.environment = Environment(self)
        self.strong_mutation = 15
        self.max_health = 1500000

        self.parent_health = 0.3
        self.heir_health = 0.1

        self.stat_file = get_stat_file()
        self.cycles_between_records = 10

        self.update_bg_color()

    def update_bg_color(self):
        self.brightness = self.environment.sun / 100

        def get_color(mi, ma):
            changing = ma - mi
            return changing * self.brightness + mi

        red = get_color(150, 250)
        green = get_color(150, 250)
        blue = get_color(10, 50)
        self.bg_color = (red, green, blue)

    def update_statistics(self, organisms, cycle):
        stat = self.get_statistics(organisms, cycle)
        line = ','.join(map(str, list(stat.values())))
        self.stat_file.write('\n' + line)

    def get_statistics(self, organisms, cycle):
        stat = dict()
        stat['cycle'] = cycle
        stat['num org-s'] = len(organisms)
        stat = {**stat, **self.get_dict_parameters()}
        stat = {**stat, **get_organisms_statistics(organisms)}
        return stat

    def get_dict_parameters(self):
        parameters = dict()
        parameters['max FPS'] = self.fps
        parameters['sun'] = self.environment.sun
        parameters['mutations'] = self.strong_mutation
        parameters['max health'] = self.max_health
        parameters['parent health'] = self.parent_health
        parameters['heir health'] = self.heir_health
        parameters['common l'] = self.environment.losses.common
        parameters['move l'] = self.environment.losses.move
        parameters['sleep l'] = self.environment.losses.sleep
        parameters['sun-sun l'] = self.environment.losses.sun_sun
        parameters['eat plant'] = self.environment.eat_plant
        parameters['eat sun'] = self.environment.eat_sun
        return parameters
