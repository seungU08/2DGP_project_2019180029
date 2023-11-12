from pico2d import *
import game_framework
import pikachu_world


def right_down(e):
    return e[0] == 'INPUT' and e[1].type == SDL_KEYDOWN and e[1].key == SDLK_RIGHT


def right_up(e):
    return e[0] == 'INPUT' and e[1].type == SDL_KEYUP and e[1].key == SDLK_RIGHT


def left_down(e):
    return e[0] == 'INPUT' and e[1].type == SDL_KEYDOWN and e[1].key == SDLK_LEFT


def left_up(e):
    return e[0] == 'INPUT' and e[1].type == SDL_KEYUP and e[1].key == SDLK_LEFT


def up_down(e):
    return e[0] == 'INPUT' and e[1].type == SDL_KEYDOWN and e[1].key == SDLK_UP


def up_up(e):
    return e[0] == 'INPUT' and e[1].type == SDL_KEYUP and e[1].key == SDLK_UP


PIXEL_PER_METER = (10.0 / 0.3)
RUN_SPEED_KMPH = 20.0
RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)

TIME_PER_ACTION = 0.5
ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
FRAMES_PER_ACTION = 5


class Jump:
    @staticmethod
    def enter(pikachu, e):
        pass

    @staticmethod
    def exit(pikachu, e):
        pass

    @staticmethod
    def do(pikachu):
        pass

    @staticmethod
    def draw(pikachu):
        pass


class Run:
    @staticmethod
    def enter(pikachu, e):
        if right_down(e) or left_up(e):
            pikachu.dir, pikachu.action, pikachu.face_dir = 1, 3, 1
        elif left_down(e) or right_up(e):
            pikachu.dir, pikachu.action, pikachu.face_dir = -1, 3, -1
        pass

    @staticmethod
    def exit(pikachu, e):
        pass

    @staticmethod
    def do(pikachu):
        pikachu.x += pikachu.dir * RUN_SPEED_PPS * game_framework.frame_time
        pikachu.x = clamp(25, pikachu.x, 1600 - 25)
        pikachu.frame = (pikachu.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 5
        pass

    @staticmethod
    def draw(pikachu):
        pikachu.image.clip_draw(int(pikachu.frame) * 100, pikachu.action * 100, 100, 100, pikachu.x, pikachu.y)
        pass


class Idle:
    @staticmethod
    def enter(pikachu, e):
        pikachu.action = 3
        pikachu.dir = 0
        pikachu.frame = 0

        pass

    @staticmethod
    def exit(pikachu, e):
        pass

    @staticmethod
    def do(pikachu):
        pikachu.frame = (pikachu.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 5

        pass

    @staticmethod
    def draw(pikachu):
        pikachu.image.clip_draw(int(pikachu.frame) * 100, pikachu.action * 100, 100, 100, pikachu.x, pikachu.y)
        pass


class StateMachine:
    def __init__(self, pikachu):
        self.pikachu = pikachu
        self.cur_state = Idle
        self.transitions = {
            Idle: {right_down: Run, left_down: Run, left_up: Run, right_up: Run, up_down: Jump},
            Run: {right_down: Idle, left_down: Idle, right_up: Idle, left_up: Idle},
            Jump: {}
        }

    def start(self):
        self.cur_state.enter(self.pikachu, ('NONE', 0))

    def update(self):
        self.cur_state.do(self.pikachu)

    def handle_event(self, e):
        for check_event, next_state in self.transitions[self.cur_state].items():
            if check_event(e):
                self.cur_state.exit(self.pikachu, e)
                self.cur_state = next_state
                self.cur_state.enter(self.pikachu, e)
                return True

        return False

    def draw(self):
        self.cur_state.draw(self.pikachu)


class Pikachu:
    def __init__(self):
        self.x, self.y = 400, 150
        self.image = load_image('resource\\pikachu.png')
        self.frame = 0
        self.face_dir = 1
        self.dir = 0
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
