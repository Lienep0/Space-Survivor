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
        self.iframes_cooldown -= 1

        if self.iframes_cooldown >= 0 and self.iframes_cooldown % 4 == 0: self.visible = not self.visible
        if self.iframes_cooldown <= 0: self.visible = True
    
    def take_damage(self):
        if self.iframes_cooldown <=0:
            self.iframes_cooldown = PLAYER_IFRAMES
            if self.has_explosive_shield and player.number_of_bombs >= 1:
                self.use_bomb()
            else:    
                self.hp -= 1
                if self.hp > 0: pyxel.play(1, PLAYER_DAMAGE_SOUND)
    
    def use_bomb(self):
        self.number_of_bombs -= 1
        bombs_list.append(Bomb(self.x + 3, self.y + 3))

    def shoot(self):
        pyxel.play(0, BULLET_SOUND)

        if self.has_quad_shot: positions_list = [[0,2,5,7], [3,0,0,3]]
        else: positions_list = [[1,6], [0,0]]
        for i in range(len(positions_list[0])):
            bullet_list.append(Bullet(self.x + positions_list[0][i], self.y + positions_list[1][i], 
                                      damage= BULLET_DAMAGE + DAMAGE_UPGRADE_BOOST * self.damage_mod,
                                      exploding= self.bullets_explode,
                                      piercing= random() <= PIERCING_UPGRADE_CHANCE * self.piercing_chance,
                                      crit= random() <= CRITICAL_UPGRADE_CHANCE * self.crit_chance))

        self.fireRateCooldown = BULLET_COOLDOWN - FIRE_RATE_UPGRADE_BOOST * self.fire_rate_mod
        if self.has_quad_shot: self.fireRateCooldown = self.fireRateCooldown * QUAD_SHOT_FIRE_RATE_PENALTY

    def draw(self):   
        if self.visible:
            pyxel.blt(self.x, self.y, 0, 64 + self.has_quad_shot * 8 + self.is_big * self.has_quad_shot * 8, self.is_big * 8, self.size, self.size, 0) # Player ship
            if self.isDashing: 
                pyxel.pset(player.x + 1, player.y + 9, 10)
                pyxel.pset(player.x + 6, player.y + 9, 10) # Player ship dashes   

    def check_upgrades(self):
        self.is_big = bool(len([upgrade for upgrade in self.inventory if upgrade.name == "Big"]))
        self.has_quad_shot = bool(len([upgrade for upgrade in self.inventory if upgrade.name == "Quad Shot"]))
        self.has_explosive_shield = bool(len([upgrade for upgrade in self.inventory if upgrade.name == "Explosive Shield"]))
        self.bullets_explode = bool(len([upgrade for upgrade in self.inventory if upgrade.name == "Explosions"]))
        self.has_dash = bool(len([upgrade for upgrade in self.inventory if upgrade.name == "Dash"]))

        self.crit_chance = len([upgrade for upgrade in self.inventory if upgrade.name == "Crit"])
        self.piercing_chance = len([upgrade for upgrade in self.inventory if upgrade.name == "Piercing"])

        self.damage_mod = len([upgrade for upgrade in self.inventory if upgrade.name == "Damage"])
        self.fire_rate_mod = len([upgrade for upgrade in self.inventory if upgrade.name == "Fire Rate"])
        self.magnet_range_mod = len([upgrade for upgrade in self.inventory if upgrade.name == "Magnet"])

    def reset(self):
        self.active = True

        self.inventory = []
        self.check_upgrades()
        
        self.x = PLAYER_STARTING_X
        self.y = PLAYER_STARTING_Y
        self.size = 16 if self.is_big else 8

        self.hp = PLAYER_HP
        self.number_of_bombs = START_NUMBER_OF_BOMBS
        
        self.level = 0
        self.xp = 0

        self.fireRateCooldown = 0
        self.iframes_cooldown = 0
        
player = Player()