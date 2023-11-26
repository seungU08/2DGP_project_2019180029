from pico2d import *

import game_framework
import pikachu_world
import pause_mode
import play_mode
import random
from beach import Beach
from monster_ball import Monster_ball
from pikachu import Pikachu
from pikachu_2 import Pikachu_2
from pikachu_map_objects import *


def handle_events():

    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_SPACE:
            game_framework.push_mode(pause_mode)
        elif event.type == SDL_KEYDOWN and event.key == SDLK_r:
            game_framework.change_mode(play_mode)
        else:
            pikachu.handle_event(event)
            pikachu_2.handle_event(event)

def init():
    global beach, net, wave, clouds, pikachu, pikachu_2, monster_ball, score_1, score_2, start_ball

    score_1 = Score(50,650)
    pikachu_world.add_object(score_1, 2)
    score_2 = Score(1080, 650)
    pikachu_world.add_object(score_2, 2)

    beach = Beach()
    pikachu_world.add_object(beach, 0)

    net = Net()
    pikachu_world.add_object(net, 2)

    #wave = Wave()
    #pikachu_world.add_object(wave, 1)

    #clouds = [Cloud(random.randint(0,1130), random.randint(400,700)) for _ in range(10)]
    #pikachu_world.add_objects(clouds, 1)

    pikachu = Pikachu()
    pikachu_world.add_object(pikachu, 2)

    pikachu_2 = Pikachu_2()
    pikachu_world.add_object(pikachu_2, 2)

    start_ball = pikachu.x

    monster_ball = Monster_ball(start_ball)
    pikachu_world.add_object(monster_ball, 2)

    pikachu_world.add_collision_pair('pikachu:monster_ball', pikachu, None)
    pikachu_world.add_collision_pair('pikachu:monster_ball', None, monster_ball)

    pikachu_world.add_collision_pair('pikachu_2:monster_ball', pikachu_2, None)
    pikachu_world.add_collision_pair('pikachu_2:monster_ball', None, monster_ball)

    pikachu_world.add_collision_pair('monster_ball:net',monster_ball, None)
    pikachu_world.add_collision_pair('monster_ball:net', None, net)

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
