import pyxel

from asteroids import asteroid_list
from constants import (BOMB_BOSS_DAMAGE, BOMB_DAMAGE, BOMB_SOUND,
                       MINIBOSS_FIRE_COOLDOWN)
from functions import round_collision
from miniboss import miniboss


class Bomb():
    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.timer = 0
        self.radius = 0
        self.damage = BOMB_DAMAGE
        self.bossdamage = BOMB_BOSS_DAMAGE
        self.things_hit = []
        pyxel.play(1, BOMB_SOUND)
 
    def update(self):
        self.timer += 1
        self.radius = self.timer * 6

        for asteroid in asteroid_list:
            if asteroid not in self.things_hit and round_collision(asteroid.x + (asteroid.parameters.size/2 - .5), asteroid.y + (asteroid.parameters.size/2 - .5), self.x, self.y, self.radius):
                asteroid.take_damage(self.damage)

        if miniboss.active and miniboss not in self.things_hit and round_collision(miniboss.x + (miniboss.size/2 - .5), miniboss.y + (miniboss.size/2 - .5), self.x, self.y, self.radius):
            miniboss.take_damage(self.bossdamage)
            self.things_hit.append(miniboss)

        if miniboss.crosshair is not None and round_collision(miniboss.crosshair.x + (miniboss.crosshair.size/2 - .5), miniboss.crosshair.y + (miniboss.crosshair.size/2 - .5), self.x, self.y, self.radius):
            miniboss.crosshair = None
            miniboss.shoot_cooldown = MINIBOSS_FIRE_COOLDOWN

        for projectile in miniboss.projectiles_list:
            if round_collision(projectile.x + projectile.size / 2, projectile.y + projectile.size / 2, self.x, self.y, self.radius):
                miniboss.projectiles_list.remove(projectile)

    def draw(self):
        pyxel.circb(self.x, self.y, self.radius, 8 + self.timer % 3)