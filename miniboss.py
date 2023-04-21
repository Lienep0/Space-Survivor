import pyxel

from bullets import bullet_list
from constants import (CROSSHAIR_HITBOX_CORRECTION, CROSSHAIR_SPEED,
                       GAME_WIDTH, MINIBOSS_FIRE_COOLDOWN, MINIBOSS_HEIGHT,
                       MINIBOSS_HP)
from functions import move_towards, round_collision
from particles import ExplodingBulletsImpact, MinibossShotLine, particle_list
from player import player


class Miniboss:
    def __init__(self):
        self.reset()

    def update(self):
        
        if self.y <= MINIBOSS_HEIGHT: self.y += 1
        else:
            self.shoot_cooldown -= 1
            self.timer +=1

            if self.crosshair is None and self.shoot_cooldown <= 0:
                self.crosshair = Crosshair(self.x, self.y)
            elif self.crosshair is not None: 
                self.crosshair.update()
                if self.crosshair.hasHit and player.iFramesCooldown <= 0:
                    player.take_damage()
                    particle_list.append(MinibossShotLine(self.x + 8 + (self.sprite_offset/8), self.y + 8, player.x + 3, player.y))
                    self.crosshair = None
                    self.shoot_cooldown = MINIBOSS_FIRE_COOLDOWN

            if self.timer % 60 == 0:
                pattern = self.patterns[self.timer // 60 % len(self.patterns)] # Cycle through patterns

                for i in pattern:
                    self.projectiles_list.append(MinibossProjectile(self.x + self.offset, self.y + self.size - 3, i))

            for projectile in self.projectiles_list:
                projectile.update()

            for bullet in [bullet for bullet in bullet_list if miniboss not in bullet.things_hit]:
                if round_collision(self.x + self.size/2, self.y + self.size/2, 
                                    (bullet.x + (bullet.xsize/2 - .5)), (bullet.y + (bullet.ysize/2 - .5)), 
                                    self.size/2 + 2):
                    bullet.collide(miniboss)
                    bullet.things_hit.append(miniboss)
            
            for explosion in [particle for particle in particle_list if type(particle) == ExplodingBulletsImpact and miniboss not in particle.things_hit]:
                if round_collision(self.x + self.size/2 + 1, self.y + self.size/2 + 1, 
                                    explosion.x, explosion.y, explosion.radius):
                    self.take_damage(explosion.damage)
                    explosion.things_hit.append(self)

    def take_damage(self, damage):
        self.hp -= damage
        print("ouch", damage)
        if self.hp <= 0:
            self.reset()

    def draw(self):
        if player.x < self.x - 16: self.sprite_offset = -16
        elif player.x > self.x + 16: self.sprite_offset = 16
        else: self.sprite_offset = 0
        pyxel.blt(self.x, self.y, 0, 16 + self.sprite_offset, 16, 16, 16, 0)

        if self.crosshair is not None: self.crosshair.draw()

        for projectile in self.projectiles_list:
            projectile.draw()

    def reset(self):
        self.active = False
        self.size = 16
        self.x = (GAME_WIDTH - self.size)/2
        self.y = -self.size
        self.hp = MINIBOSS_HP
        self.sprite_offset = 0
        self.crosshair = None
        self.shoot_cooldown = 0
        self.timer = 0
        self.projectiles_list = []
        self.offset = self.size / 2
        self.patterns = [[-1.5,-.75,0,.75,1.5],
                         [-1.125,-.375,.375,1.125]]

class MinibossProjectile():
    def __init__(self,x,y,movement):
        self.x = x
        self.y = y
        self.size = 2
        self.movement = movement

    def update(self):
        self.x += self.movement
        self.y += 1.5
        if round_collision(self.x + self.size / 2, self.y + self.size / 2, player.x + player.size / 2, player.y + player.size / 2, 5):
            player.take_damage()
            miniboss.projectiles_list.remove(self)
    
    def draw(self):
        pyxel.circ(self.x, self.y, self.size, 4)

class Crosshair:
    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.size = 16
        self.hasHit = False

    def update(self):
        self.x, self.y, self.hasHit = move_towards(self.x, self.y, player.x - self.size/4, player.y - self.size/4, CROSSHAIR_SPEED, 2 + CROSSHAIR_HITBOX_CORRECTION)

    def draw(self):
        pyxel.blt(self.x, self.y, 0, 16, 0, 16, 16, 0)

miniboss = Miniboss()