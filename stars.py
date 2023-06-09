import pyxel
from random import randint, uniform

from constants import GAME_HEIGHT, GAME_WIDTH

star_list = []

class Star:
    def __init__(self,x,y,speed):
        self.x = x
        self.y = y
        self.speed = speed

    def update(self):
        self.y += self.speed
        if self.y > GAME_HEIGHT:
            self.y = 0
            self.x = randint(2, GAME_WIDTH - 2)
            self.speed = uniform(2, 4)

    def draw(self):
        pyxel.pset(self.x, self.y, 1)

def generate_stars():
    for _ in range(30):
        star_list.append(Star(randint(2,102),randint(2,138),uniform(2,4)))