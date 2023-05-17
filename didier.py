import pyxel
from random import choice
from constants import GAME_WIDTH, DIDIER_HP
from player import player

class Didier:
    def __init__(self):
        self.reset()
        self.active = False

    def update(self):
        self.timer += 1
        self.x += self.direction[0]
        self.y += self.direction[1]
        self.shoot_projectiles()
        for projectile in self.projectiles_list:
            projectile.update()
        if self.x > GAME_WIDTH + self.size or self.x < -self.size:
            self.active= False

    def draw(self):
        pyxel.blt(self.x, self.y, 0, 0, 32 + 8 * self.timer % 4, self.size, self.size, 0)
        for projectile in self.projectiles_list:
            projectile.draw()
    
    def shoot_projectiles(self):
        if self.timer % 30 == 0:
            self.projectiles_list.append(DidierProjectile(self.x + self.radius - 2, self.y, player.x + player.radius, player.y + player.radius))
            
    def take_damage(self, damage):
        self.hp -= damage
        if self.hp <= 0:
            self.active = False

    def reset(self):
        self.active = True
        self.direction = (choice([-1, 1]),choice([-0.1, 0 , 0.1]))
        self.size = 8
        self.x = -self.size if self.direction[0] == 1 else GAME_WIDTH + self.size
        self.y = 30 + (GAME_WIDTH * (-self.direction[1]))
        self.radius = (self.size - 1) / 2
        self.hp = DIDIER_HP
        self.projectiles_list = []
        self.timer = 0

class DidierProjectile():
    def __init__(self,x,y,playerx,playery):
        self.x = x
        self.y = y
        self.size = 4
        self.radius = (self.size - 1) / 2
        self.angle = pyxel.atan2(playery - self.radius - y, playerx - self.radius - x)
        self.speed = 2

    def update(self):
        self.x += pyxel.cos(self.angle) * self.speed
        self.y += pyxel.sin(self.angle) * self.speed
        
    def draw(self):
        pyxel.blt(self.x, self.y, 0, 3, 4, 4, 4, 0)

didier = Didier()