import pyxel

from constants import GAME_WIDTH, MINIBOSS_FIRE_COOLDOWN, MINIBOSS_HEIGHT
from crosshair import Crosshair
from particles import MinibossShotLine, particle_list
from player import player


class Miniboss:
    def __init__(self):
        self.reset()

    def update(self):
        self.shootcooldown -= 1
        if self.y <= MINIBOSS_HEIGHT: self.y += 1
        elif self.crosshair is None and self.shootcooldown <= 0:
            self.hasFired = True
            self.crosshair = Crosshair(self.x, self.y)
        elif self.crosshair is not None: 
            self.crosshair.update()
            if self.crosshair.hasHit and player.iFramesCooldown <= 0:
                player.take_damage()
                particle_list.append(MinibossShotLine(self.x + 8 + (self.spriteOffset/8), self.y + 8, player.x + 3, player.y))
                self.crosshair = None
                self.hasFired = False
                self.shootcooldown = MINIBOSS_FIRE_COOLDOWN

    def draw(self):
        if player.x < self.x - 16: self.spriteOffset = -16
        elif player.x > self.x + 16: self.spriteOffset = 16
        else: self.spriteOffset = 0
        pyxel.blt(self.x, self.y, 0, 16 + self.spriteOffset, 16, 16, 16, 0)

        if self.crosshair is not None and player.hp != 0: self.crosshair.draw()

    def reset(self):
        self.active = False
        self.size = 16
        self.x = (GAME_WIDTH - self.size)/2
        self.y = -self.size
        self.hp = 50
        self.spriteOffset = 0
        self.crosshair = None
        self.shootcooldown = 0

miniboss = Miniboss()