import pyxel

from bullets import *
from pickups import pickup_list
from constants import PLAYER_STARTING_X, PLAYER_STARTING_Y

class Player:
    def __init__(self):
        self.x = PLAYER_STARTING_X
        self.y = PLAYER_STARTING_Y
        self.fireRateTimer = 3
        self.fireRateCooldown = 0

    def player_controls(self):
        if pyxel.btn(pyxel.KEY_RIGHT) and self.x < 96:
            self.x += 2
        if pyxel.btn(pyxel.KEY_LEFT) and self.x > 0:
            self.x -= 2
        if pyxel.btn(pyxel.KEY_DOWN) and self.y < 132:
            self.y += 2
        if pyxel.btn(pyxel.KEY_UP) and self.y > 0:
            self.y -= 2
        if pyxel.btn(pyxel.KEY_SPACE) and self.fireRateCooldown <= 0:
            self.fireRateCooldown = self.fireRateTimer
            bullet_list.extend([Bullet(self.x + 1, self.y), Bullet(self.x + 6, self.y)])

    def check_pickups(self):
        for pickup in pickup_list:
            dx = (pickup.x - self.x)
            dy = (pickup.y - self.y)
            if -3 < dx and dx < 10 and -4 < dy and dy < 10:
                pickup_list.remove(pickup)

    def update(self):
        self.fireRateCooldown -= 1
        self.player_controls()
        self.check_pickups()

    def draw(self):
        pyxel.blt(self.x, self.y, 0, 0, 8, 8, 8, 0)
    
player = Player()