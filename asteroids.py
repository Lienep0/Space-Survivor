import pyxel

from constants import GAME_HEIGHT, ASTEROIDS
from pickups import spawn_pickups

asteroid_list = []

class Asteroid:
    def __init__(self, x, type):
        self.x = x
        self.speed = 1
        self.type = type

        if self.type == ASTEROIDS["SMALL_ASTEROID"]["type"]:
            self.parameters = AsteroidParameters(ASTEROIDS["SMALL_ASTEROID"])
        elif self.type == ASTEROIDS["MEDIUM_ASTEROID"]["type"]:
            self.parameters = AsteroidParameters(ASTEROIDS["MEDIUM_ASTEROID"])
        elif self.type == ASTEROIDS["LARGE_ASTEROID"]["type"]:
            self.parameters = AsteroidParameters(ASTEROIDS["LARGE_ASTEROID"])
        else:
            raise Exception("Invalid Asteroid Type")
        
        self.y = -self.parameters.size

    def take_damage(self, damage):
        self.parameters.hp -= damage
        if self.parameters.hp <= 0:
            spawn_pickups(self)
            asteroid_list.remove(self)

    def update(self):
        self.y += self.speed
        if self.y > GAME_HEIGHT + self.parameters.size:
            asteroid_list.remove(self)
            
    def draw(self):
        pyxel.blt(self.x, self.y, 0, self.parameters.spritexcoord, self.parameters.spriteycoord, self.parameters.size, self.parameters.size, 0)


class AsteroidParameters:
    def __init__(self,parameters):
        self.size = parameters["size"]
        self.spritexcoord = parameters["coords"][0]
        self.spriteycoord = parameters["coords"][1]
        self.hp = parameters["hp"]
        self.xp = parameters["xp"]