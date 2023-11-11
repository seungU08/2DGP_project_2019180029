from pico2d import *

import game_framework
import pikachu_world
from beach import Beach


def handle_events():
    global running

    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            game_framework.quit()

def init():
    beach = Beach()
    pikachu_world.add_object(beach, 0)


def finish():
    pikachu_world.clear()

def update():
    pikachu_world.update()

def draw():
    clear_canvas()
    pikachu_world.render()
    update_canvas()

def pause():
    pass

def resume():
    pass
