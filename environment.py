class Losses:
    def __init__(self):
        self.common = 500
        self.move = 200
        self.sleep = 50
        self.sun_sun = 1.2


class Environment:
    def __init__(self, settings):
        self.width = settings.screen_width
        self.height = settings.screen_height
        self.border_size = 4
        self.border_color = (250, 50, 10)
        self.sun = 70
        self.eat_plant = 3.5
        self.eat_sun = 3.5
        self.losses = Losses()
