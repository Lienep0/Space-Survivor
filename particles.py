import pyxel

from asteroids import asteroid_list

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

class BombExplosion:
    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.timer = 0
        self.radius = self.timer * 6

    def update(self):
        self.timer += 1
        self.radius = self.timer * 6
        self.remove_asteroids()
        if self.timer == 22:
            particle_list.remove(self)
            self = None

    def remove_asteroids(self):
        for asteroid in asteroid_list:
            dx = asteroid.x + (asteroid.parameters.size/2 - .5) - self.x
            dy = asteroid.y + (asteroid.parameters.size/2 - .5) - self.y
            if pyxel.sqrt(dx ** 2 + dy ** 2) <= self.radius:
                asteroid.parameters.hp -= 100

    def draw(self):
        pyxel.circb(self.x, self.y, self.radius, 8 + self.timer % 3)