import pyxel
from random import randint

from constants import GAME_HEIGHT

pickup_list = []

class Pickup: # Collectible pour augmenter le score/l'xp
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
        # pyxel.circ(self.x, self.y, 2, 10) # Petits
        # pyxel.circ(self.x, self.y, 2, 10) # Moyens
        # pyxel.rect(self.x, self.y, 3, 3, 10) # Carrés
        # pyxel.rectb(self.x, self.y, 3, 3, 10) # Donuts Carrés
        pyxel.blt(self.x, self.y, 0, 2, 0, 4, 4, 0) # Customs

def spawn_pickups(asteroid):
    sqrtxp = int(pyxel.sqrt(asteroid.parameters.xp))
    for i in range(sqrtxp):
        for j in range(sqrtxp):
            randoffset = asteroid.type * 2
            xoffset = randint(-randoffset, randoffset)
            yoffset = randint(-randoffset, randoffset)
            pickup_list.append(Pickup(asteroid.x + 2 + (i * 7) + xoffset, asteroid.y + 2 + (j * 7) + yoffset))