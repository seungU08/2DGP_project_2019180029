from pico2d import *

import game_framework
import play_mode
import title_mode


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
    global logo_start_time, a
    global image, game_start_image
    image = load_image('resource\\start_map.png')
    logo_start_time = get_time()
    game_start_image = load_image('resource\\start.png')
    a = 1.0
    pass

def finish():
    pass

def update():
    global a
    a += 0.005
    if get_time() - logo_start_time >= 2.0:
        game_framework.change_mode(play_mode)
    pass

def draw():
    clear_canvas()
    image.draw(500, 350)
    game_start_image.clip_draw(0,0,100,50, 500,500, 100*a,50*a)
    update_canvas()

def pause():
    pass

def resume():
    pass
