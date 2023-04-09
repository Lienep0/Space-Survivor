import pyxel
from random import randint

from constants import GAME_HEIGHT

pickup_list = []

class Pickup:   #collectible pour augmenter le score
    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.activated = False
        self.speed = 3

    def update(self):
        self.y += 1         
        if self.y > GAME_HEIGHT + 2:
            pickup_list.remove(self)

    def draw(self):
        pyxel.circ(self.x, self.y, 1, 10) # 1 ou 2, à voir


def spawn_pickups(asteroid):
    sqrtxp = int(pyxel.sqrt(asteroid.parameters.xp))
    for i in range(sqrtxp):
        for j in range(sqrtxp):
            randoffset = asteroid.type * 2
            xoffset = randint(-randoffset, randoffset)
            yoffset = randint(-randoffset, randoffset)
            pickup_list.append(Pickup(asteroid.x + 4 + (i * 7) + xoffset, asteroid.y + 4 + (j * 7) + yoffset))