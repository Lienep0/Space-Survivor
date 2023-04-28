from random import random

import pyxel

from bombs import Bomb, bombs_list
from bullets import Bullet, bullet_list
from constants import (BULLET_COOLDOWN, BULLET_DAMAGE, BULLET_SOUND,
                       CRITICAL_UPGRADE_CHANCE, DAMAGE_UPGRADE_BOOST,
                       FIRE_RATE_UPGRADE_BOOST, PIERCING_UPGRADE_CHANCE,
                       PLAYER_DAMAGE_SOUND, PLAYER_HP, PLAYER_IFRAMES,
                       PLAYER_STARTING_X, PLAYER_STARTING_Y,
                       QUAD_SHOT_FIRE_RATE_PENALTY, START_NUMBER_OF_BOMBS)


class Player:
    def __init__(self):
        self.reset()

    def update(self):
        self.fireRateCooldown -= 1
        self.iFramesCooldown -= 1
        self.has_quad_shot = bool(len([x for x in self.inventory if x.name == "Quad Shot"]))

        if self.iFramesCooldown >= 0 and self.iFramesCooldown % 4 == 0: self.visible = not self.visible
        if self.iFramesCooldown <= 0: 
            self.visible = True
        if self.is_big == True:
            self.size = 16
    
    def take_damage(self):
        if self.iFramesCooldown <=0:
            self.iFramesCooldown = PLAYER_IFRAMES
            if len([x for x in self.inventory if x.name == "Explosive Shield"]) and player.number_of_bombs >= 1:
                self.use_bomb()
            else:    
                self.hp -= 1
                if self.hp > 0: pyxel.play(1, PLAYER_DAMAGE_SOUND)
    
    def use_bomb(self):
        self.number_of_bombs -= 1
        bombs_list.append(Bomb(self.x + 3, self.y + 3))

    def shoot(self):
        pyxel.play(0, BULLET_SOUND)

        if self.has_quad_shot: positions_list = [[0,2,5,7],[3,0,0,3]]
        else: positions_list = [[1,6],[0,0]]
        for i in range(len(positions_list[0])):
            bullet_list.append(Bullet(self.x + positions_list[0][i], self.y + positions_list[1][i], 
                                      damage= BULLET_DAMAGE + DAMAGE_UPGRADE_BOOST * len([x for x in self.inventory if x.name == "Damage"]),
                                      piercing= random() <= PIERCING_UPGRADE_CHANCE * len([x for x in self.inventory if x.name == "Piercing"]),
                                      exploding= len([x for x in self.inventory if x.name == "Explosions"]),
                                      crit= random() <= CRITICAL_UPGRADE_CHANCE * len([x for x in self.inventory if x.name == "Crit"])))

        self.fireRateCooldown = BULLET_COOLDOWN - FIRE_RATE_UPGRADE_BOOST * len([x for x in self.inventory if x.name == "Fire Rate"])
        if self.has_quad_shot: self.fireRateCooldown = self.fireRateCooldown * QUAD_SHOT_FIRE_RATE_PENALTY

    def draw(self):   
        if self.visible:
            pyxel.blt(self.x, self.y, 0, self.has_quad_shot * 8 + self.is_big * self.has_quad_shot * 8 + 64, self.is_big * 8, self.size, self.size, 0)
            if self.isDashing: 
                pyxel.pset(player.x + 1, player.y + 9, 10)
                pyxel.pset(player.x + 6, player.y + 9, 10) # Player Ship Dashes                

    def reset(self):
        self.x = PLAYER_STARTING_X
        self.y = PLAYER_STARTING_Y
        self.size = 8
        self.level = 0
        self.xp = 0
        self.hp = PLAYER_HP
        self.active = True
        self.visible = True
        self.fireRateCooldown = 0
        self.iFramesCooldown = 0
        self.inventory = []
        self.number_of_bombs = START_NUMBER_OF_BOMBS
        self.isDashing = False
        self.has_quad_shot = False
        self.is_big = True
        
player = Player()