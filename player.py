from random import random

import pyxel

from bomb import Bomb, bomb_list
from bullets import Bullet, bullet_list
from constants import (BULLET_COOLDOWN, BULLET_DAMAGE, BULLET_SOUND,
                       DAMAGE_UPGRADE_BOOST, EXPLODING_UPGRADE_CHANCE,
                       FIRE_RATE_UPGRADE_BOOST, PICKUP_SOUND,
                       PIERCING_UPGRADE_CHANCE, PLAYER_DAMAGE_SOUND, PLAYER_HP,
                       PLAYER_IFRAMES, PLAYER_STARTING_X, PLAYER_STARTING_Y,
                       QUAD_SHOT_FIRE_RATE_PENALTY)
from functions import move_towards
from pickups import pickup_list


class Player:
    def __init__(self):
        self.reset()

    def update(self):
        self.fireRateCooldown -= 1
        self.iFramesCooldown -= 1
        self.hasQuadShot = len([x for x in self.inventory if x.name == "Quad Shot"])

        if self.iFramesCooldown >= 0 and self.iFramesCooldown % 4 == 0: self.visible = not self.visible
        if self.iFramesCooldown <= 0: 
            self.visible = True

        self.attract_pickups()
    
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
        bomb_list.append(Bomb(self.x, self.y))

    def attract_pickups(self):
        for pickup in pickup_list:
            if pickup.activated:
                pickup.x, pickup.y, collected = move_towards(pickup.x, pickup.y, player.x + 3, player.y + 3, pickup.speed, 5)
                if collected:
                    pyxel.play(2, PICKUP_SOUND)
                    self.xp += 1
                    pickup_list.remove(pickup)

    def shoot(self):
        pyxel.play(0, BULLET_SOUND)

        if self.hasQuadShot: positions_list = [[0,2,5,7],[3,0,0,3]]
        else: positions_list = [[1,6],[0,0]]
        for i in range(len(positions_list[0])):
            bullet_list.append(Bullet(self.x + positions_list[0][i], self.y + positions_list[1][i], 
                                      damage= BULLET_DAMAGE + DAMAGE_UPGRADE_BOOST * len([x for x in self.inventory if x.name == "Damage"]),
                                      piercing= random() <= PIERCING_UPGRADE_CHANCE * len([x for x in self.inventory if x.name == "Piercing"]),
                                      exploding= random() <= EXPLODING_UPGRADE_CHANCE * len([x for x in self.inventory if x.name == "Explosions"])))

        self.fireRateCooldown = BULLET_COOLDOWN - FIRE_RATE_UPGRADE_BOOST * len([x for x in self.inventory if x.name == "Fire Rate"])
        if self.hasQuadShot: self.fireRateCooldown = self.fireRateCooldown * QUAD_SHOT_FIRE_RATE_PENALTY

    def draw(self):   
        if self.visible:
            if self.hasQuadShot:
                pyxel.blt(self.x, self.y, 2, 24, 40, self.size, self.size, 0) # Quad Shot Player Ship
            else :
                pyxel.blt(self.x, self.y, 0, 0, 8, self.size, self.size, 0) # Player Ship
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
        self.number_of_bombs = 1
        self.isDashing = False
        self.hasQuadShot = False
        
player = Player()