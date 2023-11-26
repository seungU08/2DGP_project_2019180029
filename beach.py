from pico2d import *

class Beach:
    def __init__(self):
        self.image = load_image('resource\\beach.png')

    def update(self):
        pass

    def draw(self):
        self.image.draw(500,350)

    def get_bb(self):
        pass

    def handle_collision(self, group, a):
        pass