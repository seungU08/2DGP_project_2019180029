
from pico2d import *

import pikachu_world


def handle_events():
    global running

    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False

def create_world():
    global running

    running = True


def update_world():
    pikachu_world.update()

def render_world():
    clear_canvas()
    pikachu_world.render()
    update_canvas()

open_canvas(1137,800)
create_world()

while running:
    handle_events()
    update_world()
    render_world()
close_canvas()
