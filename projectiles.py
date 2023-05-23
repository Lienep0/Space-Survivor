import pyxel

projectile_list = []

class Projectile:
    def __init__(self,x,y,movement):
        self.x = x
        self.y = y
        self.size = 4
        self.radius = (self.size - 1) / 2
        self.movement = movement

    def update(self):
        self.x += self.movement[0]
        self.y += self.movement[1]
    
    def draw(self):
        pyxel.blt(self.x, self.y, 0, 3, 4, 4, 4, 0)