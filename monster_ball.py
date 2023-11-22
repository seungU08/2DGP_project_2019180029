from pico2d import *
import game_framework
import play_mode

PIXEL_PER_METER = (10.0 / 0.3)
RUN_SPEED_KMPH = 25.0
RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)

TIME_PER_ACTION = 0.5
ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
FRAMES_PER_ACTION = 7

class Monster_ball:
    def __init__(self):
        self.image = load_image('resource\\monster_ball.png')
        self.x, self.y = 200, 500
        self.frame = 0
        self.speed_x, self.speed_y = 0, -1

    def update(self):
        self.frame = (self.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 8
        self.y += self.speed_y * RUN_SPEED_PPS * game_framework.frame_time
        self.x += self.speed_x * RUN_SPEED_PPS * game_framework.frame_time
        self.x = clamp(25, self.x, 1150)
        self.y = clamp(150, self.y, 700)
        self.speed_y = self.speed_y - 0.03
        if self.y >= 650:
            self.speed_y = -self.speed_y
        if self.y <= 100:
            pass
        if self.x <= 50:
            self.speed_x = -self.speed_x
        if self.x >= 1100:
            self.speed_x = -self.speed_x



    def draw(self):
        self.image.clip_draw(int(self.frame) * 100, 0, 100, 100, self.x, self.y)
        draw_rectangle(*self.get_bb())


    def get_bb(self):
        return self.x - 50, self.y - 50, self.x + 50, self.y + 50

    def handle_collision(self, group, a):
        if group == 'pikachu:monster_ball':
            self.speed_x += (self.x - play_mode.pikachu.x) / 50
            self.speed_y += (self.y - (play_mode.pikachu.y-10)) / 50
        pass