import pyxel
from random import choice
from constants import GAME_WIDTH, DIDIER_HP
from player import player
from projectiles import projectile_list, Projectile

class Didier:
    def __init__(self):
        self.reset()
        self.active = False
        self.projectile_speed = 2

    def update(self):
        self.timer += 1
        self.x += self.direction[0]
        self.y += self.direction[1]
        self.shoot_projectiles()

        if self.x > GAME_WIDTH + self.size or self.x < -self.size:
            self.active= False

    def draw(self):
        pyxel.blt(self.x, self.y, 0, 0, 32 + 8 * self.timer % 4, self.size, self.size, 0)
    
    def shoot_projectiles(self):
        if self.timer % 20 == 0:
            angle = pyxel.atan2(player.y + player.radius - self.radius - self.y, player.x + player.radius - self.radius - self.x + self.radius - 2)
            projectile_list.append(Projectile(self.x + self.radius - 2, self.y, [pyxel.cos(angle) * self.projectile_speed, pyxel.sin(angle) * self.projectile_speed]))
            
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
        self.timer = 0

didier = Didier()