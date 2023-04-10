import pyxel

from bullets import *
from pickups import pickup_list
from constants import PLAYER_STARTING_X, PLAYER_STARTING_Y, MAGNET_RANGE, BULLET_COOLDOWN, PLAYER_HP, PLAYER_IFRAMES, ASTEROID_HITBOX_CORRECTION, BULLET_DAMAGE, PLAYER_SPEED, GAME_HEIGHT, GAME_WIDTH, BOTTOM_UI_BAR_SIZE
from constants import BULLET_SOUND, PICKUP_SOUND, PLAYER_DAMAGE_SOUND, PLAYER_DASH_SOUND
from movetowards import move_towards

class Player:
    def __init__(self):
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
        self.isDashing = False

    def player_controls(self):
        self.isDashing = pyxel.btn(pyxel.KEY_SHIFT) and len([x for x in self.inventory if x.name == "Dash"])
        if self.isDashing: pyxel.play(3, PLAYER_DASH_SOUND)
        speed = PLAYER_SPEED * 1.5 ** self.isDashing
        if pyxel.btn(pyxel.KEY_RIGHT) and self.x < GAME_WIDTH - self.size - 1:
            self.x += speed
        if pyxel.btn(pyxel.KEY_LEFT) and self.x > 1:
            self.x -= speed
        if pyxel.btn(pyxel.KEY_DOWN) and self.y < GAME_HEIGHT - self.size - BOTTOM_UI_BAR_SIZE - 1:
            self.y += speed
        if pyxel.btn(pyxel.KEY_UP) and self.y > 1:
            self.y -= speed
        if pyxel.btn(pyxel.KEY_SPACE) and self.fireRateCooldown <= 0:
            pyxel.play(0, BULLET_SOUND)
            self.fireRateCooldown = BULLET_COOLDOWN * 0.8 ** len([x for x in self.inventory if x.name == "Fire Rate"])
            bullet_list.extend([Bullet(self.x + 1, self.y, BULLET_DAMAGE * 1.2 ** len([x for x in self.inventory if x.name == "Damage"])),
                                Bullet(self.x + 6, self.y, BULLET_DAMAGE * 1.2 ** len([x for x in self.inventory if x.name == "Damage"]))])
            
    def check_pickups_activate(self): 
        range = MAGNET_RANGE * 1.5 ** len([x for x in self.inventory if x.name == "Magnet"])
        for pickup in pickup_list:
            if not pickup.activated:
                dx = (pickup.x - self.x)
                dy = (pickup.y - self.y)
                if -3 - range < dx and dx < 10 + range and -4 - range < dy and dy < 10 + range:
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
            if pyxel.sqrt(dx**2 + dy**2) <= asteroid.parameters.size/2 + 3 + ASTEROID_HITBOX_CORRECTION:
                self.take_damage()

    def take_damage(self):
        self.hp -= 1
        self.iFramesCooldown  = PLAYER_IFRAMES
        if self.hp > 0: pyxel.play(1, PLAYER_DAMAGE_SOUND)

    def attract_pickups(self):
        for pickup in pickup_list:
            if pickup.activated:
                pickup.x, pickup.y, _ = move_towards(pickup.x, pickup.y, player.x + 3, player.y + 3, pickup.speed)

    def update(self):
        self.fireRateCooldown -= 1
        self.iFramesCooldown -= 1

        if self.iFramesCooldown >= 0 and self.iFramesCooldown % 4 == 0: self.visible = not self.visible
        if self.active: self.player_controls()
        if self.iFramesCooldown <= 0: 
            self.visible = True
            self.check_asteroids()

        self.check_pickups_activate()
        self.attract_pickups()
        self.check_pickups_collect()

    def draw(self):   
        if self.visible: 
            pyxel.blt(self.x, self.y, 0, 0, 8, self.size, self.size, 0) # Player Ship
            if self.isDashing: 
                pyxel.pset(player.x + 1, player.y + 9, 10)
                pyxel.pset(player.x + 6, player.y + 9, 10) # Player Ship Dashes
                
    
player = Player()