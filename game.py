import pyxel
from random import randint

from player import *
from asteroids import *
from stars import *
from pickups import *
from constants import PLAYER_STARTING_X, PLAYER_STARTING_Y

framecount = 0

class App:
    def __init__(self):
        self.asteroid_cooldown = 10
        global player
        player = Player()

    def update(self):
        global framecount
        framecount += 1
        if framecount % self.asteroid_cooldown == 0: #Génère un astéroide toutes les "asteroid_cooldown" frames
            asteroid_list.append(Asteroid(randint(0,96)))

        player.update()
        for element in asteroid_list + impact_list + bullet_list: #Evil python hack
            element.update()

    def draw(self):
        pyxel.cls(0)
        for element in star_list + asteroid_list + impact_list + bullet_list:
            element.draw()
        player.draw()

def reset_game():
    global framecount

    star_list.clear()
    asteroid_list.clear()
    asteroid_list.clear()
    bullet_list.clear()
    pickup_list.clear()
    framecount = 0
    player.x = PLAYER_STARTING_X
    player.y = PLAYER_STARTING_Y

    generate_stars()