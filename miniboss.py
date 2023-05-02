import pyxel

from constants import GAME_WIDTH, MINIBOSS_HEIGHT, MINIBOSS_HP, MINIBOSS_SCORE
from particles import MinibossExplosionParticle, ScoreParticle, particle_list
from player import player


class Miniboss:
    def __init__(self):
        self.reset()

    def update(self):
        
        if self.y <= MINIBOSS_HEIGHT: self.y += 1
        else:
            self.shoot_cooldown -= 1
            self.timer +=1

            self.manage_crosshair()

            self.shoot_projectiles()
            for projectile in self.projectiles_list:
                projectile.update()

    def shoot_projectiles(self):
        if self.timer % 60 == 0:
            pattern = self.patterns[self.timer // 60 % len(self.patterns)] # Cycle through patterns

            for i in pattern:
                self.projectiles_list.append(MinibossProjectile(self.x + self.offset, self.y + self.size - 3, i))

    def manage_crosshair(self):
        if self.crosshair is None and self.shoot_cooldown <= 0:
            self.crosshair = Crosshair(self.x, self.y)

    def take_damage(self, damage):
        self.hp -= damage
        if self.hp <= 0:
            particle_list.extend([ScoreParticle(self.x + self.size / 2, self.y - 2, MINIBOSS_SCORE),
                                  MinibossExplosionParticle(self.x + self.size / 2, self.y + self.size / 2)])
            player.minibosses_destroyed += 1
            player.score += MINIBOSS_SCORE
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
    
    def draw(self):
        pyxel.circ(self.x, self.y, self.size, 4)

class Crosshair:
    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.size = 16
        self.hasHit = False

    def draw(self):
        pyxel.blt(self.x, self.y, 0, 16, 0, 16, 16, 0)

miniboss = Miniboss()