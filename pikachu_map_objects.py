from pico2d import *

class Net:
    def __init__(self):
        self.image = load_image('resource\\net.png')

    def update(self):
        pass

    def draw(self):
        self.image.draw(565,220)

class Wave:
    def __init__(self):
        self.image = load_image('resource\\wave.png')
        self.y = 0
        self.dir = 1

    def update(self):
        if self.y > 25:
            self.dir = -0.1
        elif self.y < -25:
            self.dir = 0.1
        self.y = self.y + self.dir

    def draw(self):
        self.image.draw(565, self.y)


