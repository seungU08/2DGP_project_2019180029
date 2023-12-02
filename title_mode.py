from pico2d import *

import game_framework
import game_start
import play_mode


def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            game_framework.quit()
        elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_SPACE):
            wav.play()
            game_framework.change_mode(game_start)


def init():
    global image, image_2, wav
    image = load_image('resource\\title.png')
    image_2 = load_image('resource\\continue.png')

    wav = load_wav('resource\\WAVE144_1.wav')
    wav.set_volume(32)


def finish():
    pass


def update():
    pass


def draw():
    clear_canvas()
    image.draw(500, 350)
    image_2.draw(500, 400)
    update_canvas()


def pause():
    pass


def resume():
    pass
