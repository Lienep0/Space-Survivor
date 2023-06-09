import pyxel

from constants import EXPLODING_BULLET_RADIUS

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

class ExplodingImpact:
    def __init__(self,x,y,damage):
        self.x = x
        self.y = y
        self.timer = 0
        self.radius = 0
        self.damage = damage
        self.things_hit= []

    def update(self):
        self.timer += 1
        self.radius = self.timer * 2.5
        if self.timer % 2 == 0: self.y += 1
        if self.timer == EXPLODING_BULLET_RADIUS / 2.5:
            particle_list.remove(self)

    def draw(self):
        pyxel.circb(self.x, self.y, self.radius, 8 + self.timer % 3)

class ScoreParticle:
    def __init__(self,x,y,score):
        self.x = x
        self.y = y
        self.score = str(score)
        self.timer = 0

    def update(self):
        self.y -= 1
        self.timer += 1
        if self.timer == 5:
            particle_list.remove(self)

    def draw(self):
        pyxel.text(self.x - len(self.score) * 4 / 2, self.y - 2, self.score, 7)

class MinibossExplosion:
    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.timer = 0

    def update(self):
        self.timer += 1
        if self.timer == 30:
            particle_list.remove(self)
            self = None

    def draw(self):
        pyxel.circb(self.x, self.y, self.timer * 2, 8 + self.timer % 3)
        if self.timer % 5 == 0:
            pyxel.cls(7)