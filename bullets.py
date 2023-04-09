import pyxel

from asteroids import asteroid_list
from particles import *
from constants import IMPACT_SOUND, CHANNEL_2, BULLET_DAMAGE

bullet_list = []

class Bullet:
    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.xsize = 1
        self.ysize = 6
        self.damage = BULLET_DAMAGE
    
    def check_asteroids(self):
        for asteroid in asteroid_list:
            dx = asteroid.x - self.x
            dy = asteroid.y - self.y
            if -asteroid.size < dx and dx < self.xsize and -asteroid.size < dy and dy < self.ysize:
                pyxel.play(CHANNEL_2, IMPACT_SOUND)
                particle_list.append(Impact(self.x, self.y + 3))
                asteroid.hp -= self.damage
                if self in bullet_list:
                    bullet_list.remove(self)

    def update(self):
        self.y -= 3
        if self.y < -8:
            bullet_list.remove(self)
        self.check_asteroids()

    def draw(self):
        pyxel.blt(self.x, self.y, 0, 0, 0, self.xsize, self.ysize, 0)