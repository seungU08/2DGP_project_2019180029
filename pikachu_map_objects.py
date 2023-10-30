from pico2d import *


class Sky_block:
    def __init__(self):
        sky_x = 0
        sky_y = 0
        self.sprite_image = load_image('resuorce\sprite_sheet.png')

    def draw(self):

        self.sprite_image.clip_draw(156, 885-17-1, 15, 15, 100, 100)

    def update(self):
        pass
