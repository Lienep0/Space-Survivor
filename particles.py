import pyxel

from asteroids import asteroid_list
from constants import BOMB_BOSS_DAMAGE, BOMB_DAMAGE, EXPLODING_BULLET_RADIUS
from functions import round_collision

particle_list = []

class Impact:
    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.timer = 0

    def update(self):
        self.timer += 1
        if self.timer == 6:
            particle_list.remove(self)
            self = None

    def draw(self):
        pyxel.circb(self.x, self.y, self.timer // 2, 8 + self.timer % 3)

class MinibossShotLine:
    def __init__(self,x,y,xgoal,ygoal):
        self.x = x
        self.y = y
        self.xgoal = xgoal
        self.ygoal = ygoal
        self.timer = 0

    def update(self):
        self.timer += 1
        if self.timer == 18:
            particle_list.remove(self)
            self = None

    def draw(self):
        pyxel.line(self.x, self.y, self.xgoal, self.ygoal, 8 + self.timer % 3)

class PlayerExplosion:
    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.timer = 0

    def update(self):
        self.timer += 1

    def draw(self):
        pyxel.circb(self.x, self.y, self.timer // 2, 8 + self.timer % 3)

class ExplodingBulletsImpact:
    def __init__(self,x,y,damage):
        self.x = x
        self.y = y
        self.timer = 0
        self.radius = 0
        self.damage = damage * 2
        self.things_hit= []

    def update(self):
        self.timer += 1
        self.radius = self.timer * 2.5
        if self.timer % 2 == 0: self.y += 1
        self.hit_asteroids()
        if self.timer == EXPLODING_BULLET_RADIUS / 2.5:
            particle_list.remove(self)
            self = None

    def hit_asteroids(self):
        for asteroid in [asteroid for asteroid in asteroid_list if asteroid not in self.things_hit]:
            if round_collision(asteroid.x + (asteroid.parameters.size/2 - .5), asteroid.y + (asteroid.parameters.size/2 - .5), self.x, self.y, self.radius):
                asteroid.take_damage(self.damage)
                self.things_hit.append(asteroid)

    def draw(self):
        pyxel.circb(self.x, self.y, self.radius, 8 + self.timer % 3)