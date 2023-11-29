import random

from pico2d import *

import game_framework
import pikachu_world
import server
import title_mode
from beach import Beach
from pikachu_map_objects import *


def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            game_framework.quit()
        elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_SPACE):
            game_framework.change_mode(title_mode)


def init():
    beach = Beach()
    pikachu_world.add_object(beach, 0)

    net = Net()
    pikachu_world.add_object(net, 2)

    wave = Wave()
    pikachu_world.add_object(wave, 1)

    clouds = [Cloud(random.randint(0, 1000), random.randint(400, 700)) for _ in range(10)]
    pikachu_world.add_objects(clouds, 1)
    pass

def finish():
    server.score_1 = None
    server.score_2 = None
    server.winner = None
    pikachu_world.clear()
    pass

def update():
    pikachu_world.update()
    pass

def draw():
    clear_canvas()
    pikachu_world.render()
    update_canvas()

def pause():
    pass

def resume():
    pass
