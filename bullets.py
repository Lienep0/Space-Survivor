import pyxel

from asteroids import asteroid_list
from particles import *
from pickups import *
from constants import IMPACT_SOUND, CHANNEL_2

bullet_list = []

class Bullet:
    def __init__(self,x,y):
        self.x = x
        self.y = y
    
    def check_asteroids(self):
        for asteroid in asteroid_list:
            dx = asteroid.x - self.x
            dy = asteroid.y - self.y
            if -8 < dx and dx < 1 and -8 < dy and dy < 6:
                pyxel.play(IMPACT_SOUND, CHANNEL_2)
                particle_list.append(Impact(self.x, self.y + 3))
                asteroid.hp -= 1
                if asteroid.hp == 0:
                    pickup_list.append(Pickup(asteroid.x + 3, asteroid.y + 3))
                    asteroid_list.remove(asteroid)
                if self in bullet_list:
                    bullet_list.remove(self)   

    def update(self):
        self.y -= 3
        if self.y < -8:
            bullet_list.remove(self)
        self.check_asteroids()

    def draw(self):
        pyxel.blt(self.x, self.y, 0, 0, 0, 1, 8, 0)