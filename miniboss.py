import pyxel

class Miniboss:
    def __init__(self):
        self.x = 40
        self.y = -8
        self.hp = 6

    def update(self):
        if self.y <= 50: self.y += 1

    def draw(self):
        pyxel.blt(self.x, self.y, 0, 16, 16, 16, 16, 0)