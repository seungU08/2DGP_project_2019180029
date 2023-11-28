from pico2d import *
import game_framework
import play_mode

PIXEL_PER_METER = (1000 / 18)
RUN_SPEED_KMPH = 8.0
RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)

TIME_PER_ACTION = 0.5
ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
FRAMES_PER_ACTION = 7

class Monster_ball:
    def __init__(self, start_x):
        self.image = load_image('resource\\monster_ball.png')
        self.x, self.y = start_x, 500
        self.frame = 0
        self.speed_x, self.speed_y = 0, -1

    def update(self):
        self.frame = (self.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 5
        self.y += self.speed_y * RUN_SPEED_PPS * game_framework.frame_time
        self.x += self.speed_x * RUN_SPEED_PPS * game_framework.frame_time
        self.x = clamp(25-1, self.x, 975+1)
        self.y = clamp(150 - 1, self.y, 675+1)
        self.speed_y -= 0.03
        if self.x <= 25 or self.x >= 975:
            self.speed_x = -self.speed_x
        if self.y >= 675 or self.y <= 150:
            self.speed_y = -self.speed_y
        self.speed_x = clamp(-10, self.speed_x, 10)
        self.speed_y = clamp(-10, self.speed_y, 10)

    def draw(self):
        self.image.clip_draw(int(self.frame) * 100, 0, 100, 100, self.x, self.y)
        #draw_rectangle(*self.get_bb())



    def get_bb(self):
        return self.x - 50, self.y - 50, self.x + 50, self.y + 50

    def handle_collision(self, group, a):
        if group == 'pikachu:monster_ball':
            self.speed_x += (self.x - play_mode.pikachu.x) / 50
            self.speed_y += (self.y - (play_mode.pikachu.y-10)) / 50
            self.y += self.speed_y * RUN_SPEED_PPS * game_framework.frame_time
            self.x += self.speed_x * RUN_SPEED_PPS * game_framework.frame_time
        if group == 'pikachu_2:monster_ball':
            self.speed_x += (self.x - play_mode.pikachu_2.x) / 50
            self.speed_y += (self.y - (play_mode.pikachu_2.y-10)) / 50
        if group == 'monster_ball:net':
            if self.y - 50 >= 220 + 40:
                self.speed_y = -self.speed_y
            else:
                self.speed_x = -self.speed_x

        pass