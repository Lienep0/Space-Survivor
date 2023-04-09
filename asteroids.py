import pyxel

from pickups import spawn_pickups
from constants import GAME_HEIGHT, ASTEROID_TYPE_1, ASTEROID_TYPE_2, ASTEROID_TYPE_3, ASTEROID_TYPE_1_SIZE, ASTEROID_TYPE_2_SIZE, ASTEROID_TYPE_3_SIZE

asteroid_list = []

class Asteroid:
    def __init__(self,x,type):
        self.x = x
        self.speed = 1
        self.type = type

        if self.type == ASTEROID_TYPE_1: #Y'a moyen de mieux faire ça je pense. Des sous-classes peut-être ?
            self.size = ASTEROID_TYPE_1_SIZE
            self.spritexcoord = 32
            self.spriteycoord = 16
            self.hp = 6
            self.xp = 1
        elif self.type == ASTEROID_TYPE_2:
            self.size = ASTEROID_TYPE_2_SIZE
            self.spritexcoord = 48
            self.spriteycoord = 0
            self.hp = 12
            self.xp = 8
        elif self.type == ASTEROID_TYPE_3:
            self.size = ASTEROID_TYPE_3_SIZE
            self.spritexcoord = 0
            self.spriteycoord = 32
            self.hp = 24
            self.xp = 16
        else:
            raise Exception("Invalid Asteroid Type")
        
        self.y = -self.size

    def update(self):
        self.y += self.speed
        if self.y > GAME_HEIGHT + self.size:
            asteroid_list.remove(self)
        if self.hp <= 0:
                spawn_pickups(self)
                asteroid_list.remove(self)

    def draw(self):
        pyxel.blt(self.x, self.y, 0, self.spritexcoord, self.spriteycoord, self.size, self.size, 0)