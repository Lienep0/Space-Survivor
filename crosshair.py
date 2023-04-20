import pyxel

from player import player

from functions import move_towards
from constants import CROSSHAIR_SPEED, CROSSHAIR_HITBOX_CORRECTION

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