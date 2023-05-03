from random import randint

import pyxel

from constants import GAME_HEIGHT, PICKUP_SCORE, PICKUP_SOUND
from particles import ScoreParticle, particle_list
from player import player

pickup_list = []

class Pickup: # Collectible pour augmenter le score/l'xp
    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.size = 4
        self.radius = (self.size - 1) / 2
        self.activated = False
        self.speed = 3

    def update(self):
        self.y += 1
        if self.y > GAME_HEIGHT + 2:
            pickup_list.remove(self)

    def collect(self):
        pyxel.play(2, PICKUP_SOUND)
        particle_list.append(ScoreParticle(player.x + player.radius, player.y - 4, PICKUP_SCORE))
        player.score += PICKUP_SCORE
        player.xp += 1
        player.pickups_collected += 1
        pickup_list.remove(self)

    def draw(self):
        pyxel.blt(self.x, self.y, 0, 3, 0, 4, 4, 0)

def spawn_pickups(asteroid):
    sqrtxp = int(pyxel.sqrt(asteroid.parameters.xp))
    for i in range(sqrtxp):
        for j in range(sqrtxp):
            randoffset = asteroid.type * 2
            xoffset = randint(-randoffset, randoffset)
            yoffset = randint(-randoffset, randoffset)
            pickup_list.append(Pickup(asteroid.x + 2 + (i * 7) + xoffset, asteroid.y + 2 + (j * 7) + yoffset))