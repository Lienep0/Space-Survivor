import pyxel
from random import *
from globals import bullet_list, pickup_list, star_list, asteroid_list, framecount,impact_list,player

class Player:
    def __init__(self):
        self.x = 48
        self.y = 100
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
        if pyxel.btn(pyxel.KEY_R):
            reset_game()

    def update(self):
        self.fireRateCooldown -= 1
        self.player_controls()

    def draw(self):
        pyxel.blt(self.x, self.y, 0, 0, 8, 8, 8, 0)

class Star:
    def __init__(self,x,y,speed):
        self.x = x
        self.y = y
        self.speed = speed

    def update(self):
        self.y += self.speed
        if self.y > 138:
            self.y = 0
            self.x = randint(2,94)
            self.speed = uniform(2,4)

    def draw(self):
        pyxel.pset(self.x, self.y, 1)

class Bullet:
    def __init__(self,x,y):
        self.x = x
        self.y = y

    def update(self):
        self.y -= 3
        if self.y < -8:
            bullet_list.remove(self)
        for asteroid in asteroid_list:
            if abs((asteroid.x + 4) - self.x) < 8 and abs((asteroid.y + 8) - self.y) < 8:
                global framecount
                impact_list.append(Impact(self.x, self.y))
                bullet_list.remove(self)
                asteroid.hp -= 1
                if asteroid.hp == 0:
                    asteroid_list.remove(asteroid)
                    break

    def draw(self):
        pyxel.blt(self.x, self.y, 0, 0, 0, 1, 8)

class Asteroid:
    def __init__(self,x):
        self.x = x
        self.y = -8
        self.hp = 6

    def update(self):
        self.y += 1

    def draw(self):
        pyxel.blt(self.x, self.y, 0, 32, 16, 8, 8, 0)

class Pickup:   #collectible pour augmenter le score
    def __init__(self,x,y):
        self.x = x
        self.y = y

    def update(self):
        self.y += 1
        if abs(self.x - (player.x + 8)) < 4 and abs(self.y - (player.y + 8)) < 4:
            pickup_list.remove(self)
            score += 50

    def draw(self):
        pyxel.circb(self.x, self.y, 2, 10)

class Impact:
    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.timer = 0

    def update(self):
        self.timer += 1
        if self.timer == 6:
            impact_list.remove(self)

    def draw(self):
        pyxel.circb(self.x, self.y, self.timer // 2, 8 + self.timer % 3) #Probablement à modifier

class Miniboss:
    def __init__(self):
        self.x = 40
        self.y = -8
        self.hp = 6

    def update(self):
        if self.y <= 50: self.y += 1

    def draw(self):
        pyxel.blt(self.x, self.y, 0, 16, 16, 16, 16, 0)

class App:
    def __init__(self):
        self.asteroid_cooldown = 10
        global player
        player = Player()

    def update(self):
        global framecount
        framecount += 1
        if framecount % self.asteroid_cooldown == 0: #Génère un astéroide toutes les "asteroid_cooldown" frames
            asteroid_list.append(Asteroid(randint(0,96)))

        player.update()
        for element in asteroid_list + impact_list + bullet_list: #Evil python hack
            element.update()

    def draw(self):
        pyxel.cls(0)
        for element in star_list + asteroid_list + impact_list + bullet_list:
            element.draw()
        player.draw()

def generate_stars():
    for _ in range(30):
        star_list.append(Star(randint(2,102),randint(2,138),uniform(2,4)))

def reset_game():
    global framecount

    star_list.clear()
    asteroid_list.clear()
    asteroid_list.clear()
    bullet_list.clear()
    pickup_list.clear()
    framecount = 0
    player.x = 48
    player.y = 100

    generate_stars()