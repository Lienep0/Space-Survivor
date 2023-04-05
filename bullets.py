import pyxel

from asteroids import asteroid_list
from particles import Impact, impact_list

bullet_list = []

class Bullet:
    def __init__(self,x,y):
        self.x = x
        self.y = y

    def update(self):
        self.y -= 3
        if self.y < -8:
            bullet_list.remove(self)
        for asteroid in asteroid_list:
            if abs((asteroid.x + 4) - self.x) < 8 and abs((asteroid.y + 8) - self.y) < 8:
                global framecount
                impact_list.append(Impact(self.x, self.y))
                bullet_list.remove(self)
                asteroid.hp -= 1
                if asteroid.hp == 0:
                    asteroid_list.remove(asteroid)
                    break

    def draw(self):
        pyxel.blt(self.x, self.y, 0, 0, 0, 1, 8)