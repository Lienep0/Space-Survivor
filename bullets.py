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
        self.xsize = 1
        self.ysize = 6
    
    def check_asteroids(self):
        for asteroid in asteroid_list:
            dx = asteroid.x - self.x
            dy = asteroid.y - self.y
            if -asteroid.size < dx and dx < self.xsize and -asteroid.size < dy and dy < self.ysize:
                pyxel.play(IMPACT_SOUND, CHANNEL_2)
                particle_list.append(Impact(self.x, self.y + 3))
                asteroid.hp -= 1
                if asteroid.hp == 0:
                    pickup_list.append(Pickup(asteroid.x + asteroid.size/2 - 1, asteroid.y + asteroid.size/2 - 1))
                    # for i in range(asteroid.xp):
                    #     pickup_list.append(Pickup(asteroid.x + asteroid.size/2, asteroid.y + asteroid.size/2))
                    asteroid_list.remove(asteroid)
                if self in bullet_list:
                    bullet_list.remove(self)

    def update(self):
        self.y -= 3
        if self.y < -8:
            bullet_list.remove(self)
        self.check_asteroids()

    def draw(self):
        pyxel.blt(self.x, self.y, 0, 0, 0, self.xsize, self.ysize, 0)