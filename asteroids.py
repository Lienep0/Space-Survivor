import pyxel

asteroid_list = []

class Asteroid:
    def __init__(self,x):
        self.x = x
        self.y = -8
        self.hp = 6

    def update(self):
        self.y += 1

    def draw(self):
        pyxel.blt(self.x, self.y, 0, 32, 16, 8, 8, 0)