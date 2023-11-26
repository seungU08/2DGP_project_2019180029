from pico2d import *
import game_framework
import pikachu_world


def right_down(e):
    return e[0] == 'INPUT' and e[1].type == SDL_KEYDOWN and e[1].key == SDLK_d


def right_up(e):
    return e[0] == 'INPUT' and e[1].type == SDL_KEYUP and e[1].key == SDLK_d


def left_down(e):
    return e[0] == 'INPUT' and e[1].type == SDL_KEYDOWN and e[1].key == SDLK_a


def left_up(e):
    return e[0] == 'INPUT' and e[1].type == SDL_KEYUP and e[1].key == SDLK_a


def up_down(e):
    return e[0] == 'INPUT' and e[1].type == SDL_KEYDOWN and e[1].key == SDLK_w


def up_up(e):
    return e[0] == 'INPUT' and e[1].type == SDL_KEYUP and e[1].key == SDLK_w

def y_150(e):
    return e[0] == 'y==150'

def l_down(e):
    return e[0] == 'INPUT' and e[1].type == SDL_KEYDOWN and e[1].key == SDLK_g


PIXEL_PER_METER = (1000/18)
RUN_SPEED_KMPH = 12.0
RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)

TIME_PER_ACTION = 0.5
ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
FRAMES_PER_ACTION = 5


class Jump:
    @staticmethod
    def enter(pikachu_2, e):
        if right_down(e) or right_up(e):
            pikachu_2.speed_x = 1
        elif left_down(e) or left_up(e):
            pikachu_2.speed_x = -1
        elif up_up(e) or up_down(e):
            pikachu_2.speed_y = 5
        pikachu_2.action = 2
        pass

    @staticmethod
    def exit(pikachu_2, e):
        if l_down(e):
            pikachu_2.hit_ball()
        pass

    @staticmethod
    def do(pikachu_2):
        pikachu_2.frame = (pikachu_2.frame + FRAMES_PER_ACTION*2 * ACTION_PER_TIME * game_framework.frame_time) % 4
        pikachu_2.x += pikachu_2.speed_x * RUN_SPEED_PPS * game_framework.frame_time
        pikachu_2.x = clamp(500+25, pikachu_2.x, 1000 - 25)

        if pikachu_2.speed_y != 0:
            pikachu_2.y += pikachu_2.speed_y * RUN_SPEED_PPS * game_framework.frame_time
            pikachu_2.speed_y = pikachu_2.speed_y - 0.03
        if pikachu_2.y < 150:
            pikachu_2.speed_y = 0
            pikachu_2.state_machine.handle_event(('y==150', 0))

        pass

    @staticmethod
    def draw(pikachu_2):
        pikachu_2.image.clip_composite_draw(int(pikachu_2.frame) * 100,int(pikachu_2.action) * 100, 100, 100, 0, 'h', pikachu_2.x, pikachu_2.y, 100, 100)



class Run:
    @staticmethod
    def enter(pikachu_2, e):
        if right_down(e) or left_up(e):
            pikachu_2.speed_x, pikachu_2.action = 1, 3
        elif left_down(e) or right_up(e):
            pikachu_2.speed_x, pikachu_2.action = -1, 3
        pass

    @staticmethod
    def exit(pikachu_2, e):
        if l_down(e):
            pikachu_2.hit_ball()
        pass

    @staticmethod
    def do(pikachu_2):

        pikachu_2.frame = (pikachu_2.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 8
        pikachu_2.x += pikachu_2.speed_x * RUN_SPEED_PPS * game_framework.frame_time
        pikachu_2.x = clamp(525, pikachu_2.x, 975)

    @staticmethod
    def draw(pikachu_2):
        pikachu_2.image.clip_composite_draw(int(pikachu_2.frame) * 100,int(pikachu_2.action) * 100, 100, 100, 0, 'h', pikachu_2.x, pikachu_2.y, 100, 100)




class Idle:
    @staticmethod
    def enter(pikachu_2, e):
        pikachu_2.action = 3
        pikachu_2.speed_x = 0
        pikachu_2.frame = 0



    @staticmethod
    def exit(pikachu_2, e):
        if l_down(e):
            pikachu_2.hit_ball()
        pass

    @staticmethod
    def do(pikachu_2):
        pikachu_2.frame = (pikachu_2.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 8

        pass

    @staticmethod
    def draw(pikachu_2):
        pikachu_2.image.clip_composite_draw(int(pikachu_2.frame) * 100,int(pikachu_2.action) * 100, 100, 100, 0, 'h', pikachu_2.x, pikachu_2.y, 100, 100)


class StateMachine:
    def __init__(self, pikachu_2):
        self.pikachu_2 = pikachu_2
        self.cur_state = Idle
        self.transitions = {
            Idle: {right_down: Run, left_down: Run, left_up: Run, right_up: Run, up_down: Jump, l_down: Idle},
            Run: {right_down: Idle, left_down: Idle, right_up: Idle, left_up: Idle, up_down: Jump, l_down: Run},
            Jump: {right_down: Jump, left_down: Jump, left_up: Jump, right_up: Jump, y_150: Idle, l_down: Jump}
        }

    def start(self):
        self.cur_state.enter(self.pikachu_2, ('NONE', 0))

    def update(self):
        self.cur_state.do(self.pikachu_2)

    def handle_event(self, e):
        for check_event, next_state in self.transitions[self.cur_state].items():
            if check_event(e):
                self.cur_state.exit(self.pikachu_2, e)
                self.cur_state = next_state
                self.cur_state.enter(self.pikachu_2, e)
                return True

        return False

    def draw(self):
        self.cur_state.draw(self.pikachu_2)


class Pikachu_2:
    def __init__(self):
        self.x, self.y = 1000 - 200, 150
        self.image = load_image('resource\\pikachu.png')
        self.frame = 0
        self.speed_y = 0
        self.speed = 0
        self.action = 0
        self.state_machine = StateMachine(self)
        self.state_machine.start()
        self.move = 0

    def update(self):
        self.state_machine.update()
        pass

    def handle_event(self, event):
        self.state_machine.handle_event(('INPUT', event))
        pass

    def draw(self):
        self.state_machine.draw()
        draw_rectangle(*self.get_bb())

    def hit_ball(self):
        pass

    def get_bb(self):
        return self.x - 50, self.y - 50, self.x + 40, self.y + 50

    def handle_collision(self, group, other):
        if group == 'pikachu_2:monster_ball':
            print('pikachu_2:ball')
        pass