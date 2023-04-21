import pyxel

from constants import IMPACT_SOUND, CRITICAL_UPGRADE_DAMAGE_MULTIPLIER
from particles import ExplodingBulletsImpact, Impact, particle_list

bullet_list = []

class Bullet:
    def __init__(self, x, y, damage, piercing, exploding, crit):
        self.x = x
        self.y = y
        self.xsize = 1
        self.ysize = 6
        self.damage = damage * CRITICAL_UPGRADE_DAMAGE_MULTIPLIER if crit else damage
        self.piercing = piercing
        self.exploding = exploding
        self.crit = crit
        self.things_hit = []
            
    def collide(self, collider):
        if self.exploding:
            pyxel.play(2, IMPACT_SOUND) # TODO : Change to explosive impact sound
            particle_list.append(ExplodingBulletsImpact(self.x, self.y + 3, self.damage))
        else:
            pyxel.play(2, IMPACT_SOUND)
            particle_list.append(Impact(self.x, self.y + 4))
            collider.take_damage(self.damage)
        if self.piercing:
            self.things_hit.append(collider) 
        elif self in bullet_list:
            bullet_list.remove(self)

    def update(self):
        self.y -= 3
        if self.y < -8:
            bullet_list.remove(self)

    def draw(self):
        pyxel.blt(self.x, self.y, 0, 0, 0, self.xsize, self.ysize, 0)

        # Custom Visuals for different bullet types (stackable)
        if self.exploding: pyxel.rect(self.x, self.y, 1, 3, 8)
        if self.piercing: pyxel.rect(self.x, self.y + 4, 1, 2, 12)
        if self.crit: pyxel.rect(self.x, self.y + 1, 1, 2, 11)