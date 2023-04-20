import pyxel

from asteroids import asteroid_list
from particles import particle_list, Impact, ExplodingBulletsImpact
from constants import IMPACT_SOUND
from functions import round_collision

bullet_list = []

class Bullet:
    def __init__(self, x, y, damage):
        self.x = x
        self.y = y
        self.xsize = 1
        self.ysize = 6
        self.damage = damage
    
    def check_asteroids(self):
        for asteroid in asteroid_list:
            if round_collision(asteroid.x + (asteroid.parameters.size/2 - .5), asteroid.y + (asteroid.parameters.size/2 - .5), 
                               (self.x + (self.xsize/2 - .5)), (self.y + (self.ysize/2 - .5)), 
                               asteroid.parameters.size/2 + 3):
                pyxel.play(2, IMPACT_SOUND)
                particle_list.append(Impact(self.x, self.y + 3))
                asteroid.take_damage(self.damage)
                if self in bullet_list:
                    bullet_list.remove(self)

    def update(self):
        self.y -= 3
        if self.y < -8:
            bullet_list.remove(self)
        self.check_asteroids()

    def draw(self):
        pyxel.blt(self.x, self.y, 0, 0, 0, self.xsize, self.ysize, 0)

class ExplodingBullet:
    def __init__(self, x, y, damage):
        self.x = x
        self.y = y
        self.xsize = 1
        self.ysize = 6
        self.damage = damage
    
    def check_asteroids(self):
        for asteroid in asteroid_list:            
            if round_collision(asteroid.x + (asteroid.parameters.size/2 - .5), asteroid.y + (asteroid.parameters.size/2 - .5), 
                               (self.x + (self.xsize/2 - .5)), (self.y + (self.ysize/2 - .5)), 
                               asteroid.parameters.size/2 + 3):
                pyxel.play(2, IMPACT_SOUND) # TODO : Change to explosive impact sound
                particle_list.append(ExplodingBulletsImpact(self.x, self.y + 3, self.damage))
                if self in bullet_list:
                    bullet_list.remove(self)

    def update(self):
        self.y -= 3
        if self.y < -8:
            bullet_list.remove(self)
        self.check_asteroids()

    def draw(self):
        pyxel.blt(self.x, self.y, 0, 0, 0, self.xsize, self.ysize, 0)
        pyxel.rect(self.x, self.y, 1, 3, 8)