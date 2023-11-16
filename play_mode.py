from pico2d import *

import game_framework
import pikachu_world
import random
from beach import Beach
from monster_ball import Monster_ball
from pikachu import Pikachu
from pikachu_map_objects import *


def handle_events():

    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            game_framework.quit()
        else:
            pikachu.handle_event(event)

def init():
    global beach, net, wave, clouds, pikachu
    beach = Beach()
    pikachu_world.add_object(beach, 0)

    net = Net()
    pikachu_world.add_object(net, 2)

    #wave = Wave()
    #pikachu_world.add_object(wave, 1)

    #clouds = [Cloud(random.randint(0,1130), random.randint(400,700)) for _ in range(10)]
    #pikachu_world.add_objects(clouds, 1)

    pikachu = Pikachu()
    pikachu_world.add_object(pikachu,2)

    monster_ball = Monster_ball()
    pikachu_world.add_object(monster_ball, 2)

def finish():
    pikachu_world.clear()

def update():
    pikachu_world.update()
    pikachu_world.handle_collisions()

def draw():
    clear_canvas()
    pikachu_world.render()
    update_canvas()

def pause():
    pass

def resume():
    pass
