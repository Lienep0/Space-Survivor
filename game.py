import pyxel
from random import randint

from player import *
from asteroids import *
from stars import *
from pickups import *

framecount = 0

class App:
    def __init__(self):
        self.asteroid_cooldown = 10

    def update(self):
        global framecount
        framecount += 1

        if framecount % self.asteroid_cooldown == 0: #Génère un astéroide toutes les "asteroid_cooldown" frames
            asteroid_list.append(Asteroid(randint(0,96)))

        player.update()
        for element in asteroid_list + impact_list + bullet_list + pickup_list: #Evil python hack
            element.update()

    def draw(self):
        pyxel.cls(0)
        for element in star_list + asteroid_list + impact_list + bullet_list + pickup_list:
            element.draw()
        player.draw()