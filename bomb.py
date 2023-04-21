import pyxel

from constants import BOMB_BOSS_DAMAGE, BOMB_DAMAGE, BOMB_SOUND

bomb_list = []

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

        if self.timer >= 22:
            bomb_list.remove(self)

    def draw(self):
        pyxel.circb(self.x, self.y, self.radius, 8 + self.timer % 3)