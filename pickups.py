import pyxel

from constants import GAME_HEIGHT

pickup_list = []

class Pickup:   #collectible pour augmenter le score
    def __init__(self,x,y):
        self.x = x
        self.y = y

    def update(self):
        self.y += 1
        if self.y > GAME_HEIGHT + 2:
            pickup_list.remove(self)

    def draw(self):
        pyxel.circ(self.x, self.y, 2, 10)