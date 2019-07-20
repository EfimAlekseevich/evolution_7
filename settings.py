from environment import Environment


class Settings:
    def __init__(self):

        self.screen_width = 480
        self.screen_height = 360
        self.text_color = (0, 50, 0)
        self.bg_color = None
        self.brightness = 1

        self.fps = 5
        self.run = True

        self.environment = Environment(self)
        self.strong_mutation = 0
        self.max_health = 1000000

        self.parent_health = 0.3
        self.heir_health = 0.1

        self.update_bg_color()

    def update_bg_color(self):
        self.brightness = self.environment.sun // 100

        def get_color(mi, ma):
            changing = ma - mi
            return changing * self.brightness + mi

        red = get_color(150, 250)
        green = get_color(150, 250)
        blue = get_color(10, 50)
        self.bg_color = (red, green, blue)
