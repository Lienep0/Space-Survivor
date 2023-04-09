import pyxel

from bullets import *
from pickups import pickup_list
from constants import PLAYER_STARTING_X, PLAYER_STARTING_Y, MAGNET_RANGE, BULLET_COOLDOWN, PLAYER_HP, PLAYER_IFRAMES, ASTEROID_HITBOX_CORRECTION, XP_REQUIREMENTS
from constants import BULLET_SOUND, PICKUP_SOUND, PLAYER_DAMAGE_SOUND
from movetowards import move_towards

class Player:
    def __init__(self):
        self.x = PLAYER_STARTING_X
        self.y = PLAYER_STARTING_Y
        self.size = 8
        self.fireRateCooldown = 0
        self.iFramesCooldown = 0
        self.level = 0
        self.xp = 0
        self.hp = PLAYER_HP
        self.visible = True
        self.active = True

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
            pyxel.play(0, BULLET_SOUND)
            self.fireRateCooldown = BULLET_COOLDOWN
            bullet_list.extend([Bullet(self.x + 1, self.y), Bullet(self.x + 6, self.y)])

    def check_pickups_activate(self): 
        for pickup in pickup_list:
            if not pickup.activated:
                dx = (pickup.x - self.x)
                dy = (pickup.y - self.y)
                if -3 - MAGNET_RANGE < dx and dx < 10 + MAGNET_RANGE and -4 - MAGNET_RANGE < dy and dy < 10 + MAGNET_RANGE:
                    pickup.activated = True

    def check_pickups_collect(self):
        for pickup in pickup_list:
            dx = (pickup.x - self.x)
            dy = (pickup.y - self.y)
            if -3 < dx and dx < 10 and -4 < dy and dy < 10:
                pyxel.play(2, PICKUP_SOUND)
                self.xp += 1
                pickup_list.remove(pickup)

    def check_asteroids(self):
        for asteroid in asteroid_list:
            dx = asteroid.x + (asteroid.parameters.size/2 - .5) - (self.x + (self.size/2 - .5))
            dy = asteroid.y + (asteroid.parameters.size/2 - .5) - (self.y + (self.size/2 - .5))
            if pyxel.sqrt(dx**2 + dy**2) <= asteroid.parameters.size/2 + 3 - ASTEROID_HITBOX_CORRECTION:
                self.hp -= 1
                self.iFramesCooldown  = PLAYER_IFRAMES
                if self.hp > 0: pyxel.play(1, PLAYER_DAMAGE_SOUND)

    def attract_pickups(self):
        for pickup in pickup_list:
            if pickup.activated:
                pickup.x, pickup.y = move_towards(pickup.x, pickup.y, player.x + 3, player.y + 3, pickup.speed)

    def update(self):
        self.fireRateCooldown -= 1
        self.iFramesCooldown -= 1

        if self.xp == XP_REQUIREMENTS[self.level]:
            self.xp = 0
            self.level += 1

        if self.iFramesCooldown >= 0 and self.iFramesCooldown % 4 == 0: self.visible = not self.visible
        if self.active: self.player_controls()
        if self.iFramesCooldown <= 0: self.check_asteroids()

        self.check_pickups_activate()
        self.attract_pickups()
        self.check_pickups_collect()

    def draw(self):   
        if self.visible: 
            pyxel.blt(self.x, self.y, 0, 0, 8, self.size, self.size, 0) # Player Ship
                
    
player = Player()