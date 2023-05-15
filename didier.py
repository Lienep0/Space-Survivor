import pyxel
from random import choice
from constants import GAME_WIDTH, DIDIER_HP

class Didier:
    def __init__(self):
        self.reset()

    def update(self):
        self.timer += 1
        self.x += self.direction[0]
        self.y += self.direction[1]

    def draw(self):
        pyxel.blt(self.x, self.y, 0, 32 + (8 * self.timer % 3), 0, self.size, self.size, 0)
    
    def shoot_projectiles(self):
        if self.timer % 30 == 0:
            self.projectiles_list.append(DidierProjectile(self.x + self.radius - 2, self.y))
            
    def take_damage(self, damage):
        self.hp -= damage

    def reset(self):
        self.active = False
        self.direction = (choice([-1, 1]),choice([-0.1, 0 , 0.1]))
        self.size = 8
        self.x = -self.size if self.direction[0] == 1 else GAME_WIDTH + self.size
        self.y = 30 + (GAME_WIDTH * (-self.direction[1]))
        self.radius = (self.size - 1) / 2
        self.hp = DIDIER_HP
        self.projectiles_list = []
        self.timer = 0

class DidierProjectile():
    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.size = 4
        self.radius = (self.size - 1) / 2

    def update(self):
        self.y += 1.5
    
    def draw(self):
        pyxel.blt(self.x, self.y, 0, 3, 4, 4, 4, 0)

didier = Didier()