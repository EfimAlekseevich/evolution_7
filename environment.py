class Losses:
    def __init__(self):
        self.common = 200
        self.move = 1000
        self.sleep = 50
        self.sun_sun = 0.05
        self.eat_plant = 1
        self.eat_sun = 1


class Environment:
    def __init__(self, settings):
        self.width = settings.screen_width
        self.height = settings.screen_height
        self.border_size = 4
        self.border_color = (250, 50, 10)
        self.sun = 50
        self.losses = Losses()
