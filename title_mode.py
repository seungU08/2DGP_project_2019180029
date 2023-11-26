from pico2d import *

import game_framework
import play_mode


def handle_events():

    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            game_framework.quit()
        elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_SPACE):
            game_framework.change_mode(play_mode)


def init():
    global image
    image = load_image('resource\\title.png')
    pass

def finish():
    pass

def update():
    pass

def draw():
    clear_canvas()
    image.draw(500, 350)
    update_canvas()

def pause():
    pass

def resume():
    pass
