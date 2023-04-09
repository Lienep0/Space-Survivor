import pyxel

from bullets import *
from pickups import pickup_list
from constants import PLAYER_STARTING_X, PLAYER_STARTING_Y, BULLET_SOUND, CHANNEL_1, PICKUP_SOUND, CHANNEL_3, MAGNET_RANGE, BULLET_COOLDOWN
from movetowards import move_towards

class Player:
    def __init__(self):
        self.x = PLAYER_STARTING_X
        self.y = PLAYER_STARTING_Y
        self.size = 8
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
            pyxel.play(BULLET_SOUND, CHANNEL_1)
            self.fireRateCooldown = BULLET_COOLDOWN
            bullet_list.extend([Bullet(self.x + 1, self.y), Bullet(self.x + 6, self.y)])

    def check_pickups_activated(self): 
        for pickup in pickup_list:
            if not pickup.activated:
                dx = (pickup.x - self.x)
                dy = (pickup.y - self.y)
                if -3 - MAGNET_RANGE< dx and dx < 10 +MAGNET_RANGE and -4 - MAGNET_RANGE < dy and dy < 10 + MAGNET_RANGE:
                    pickup.activated = True

    def check_pickups_collected(self):
        for pickup in pickup_list:
            dx = (pickup.x - self.x)
            dy = (pickup.y - self.y)
            if -3 < dx and dx < 10 and -4 < dy and dy < 10:
                pyxel.play(PICKUP_SOUND, CHANNEL_3)
                pickup_list.remove(pickup)

    def update(self):
        self.fireRateCooldown -= 1
        self.player_controls()
        self.check_pickups_activated()
        for pickup in pickup_list:
            if pickup.activated:
                pickup.x, pickup.y = move_towards(pickup.x, pickup.y, player.x + 3, player.y + 3, pickup.speed)
        self.check_pickups_collected()

    def draw(self):
        pyxel.blt(self.x, self.y, 0, 0, 8, 8, 8, 0)
    
player = Player()