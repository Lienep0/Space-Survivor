import pyxel
from random import *

class Player:
    def __init__(self):
        self.x = 60
        self.y = 60
        self.fireRateTimer = 5
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
            bullet = Bullet(self.x + 1, self.y)
            bullet2 = Bullet(self.x + 6, self.y)
            bullet_list.extend([bullet,bullet2])

    def update(self):
        self.fireRateCooldown -= 1
        self.player_controls()

    def draw(self):
        pyxel.blt(self.x, self.y, 0, 0, 8, 8, 8)

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
            self.speed = uniform(1,3)

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

    def draw(self):
        pyxel.blt(self.x, self.y, 0, 0, 0, 1, 8)

class Asteroid:
    def __init__(self,x):
        self.x = x
        self.y = 0

    def update(self):
        self.y += 1
        for bullet in bullet_list:
            if abs((self.x + 4) - bullet.x) < 8 and abs(self.y - bullet.y) < 8:
                impact_list.append(Impact(bullet.x, bullet.y))
                asteroid_list.remove(self)
                break

    def draw(self):
        pyxel.blt(self.x, self.y, 0, 32, 16, 8, 8)

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
        pyxel.circb(self.x, self.y, self.timer // 2, 8 + self.timer % 3)
        pyxel.rectb(self.x - 1, self.y - 1, 3, 3, 9)
        pyxel.pset(self.x, self.y, 9 - self.timer // 3) # C'est un peu moche mais je pensais à un truc comme ça pour les explosions (à modifier)

class App:
    def __init__(self):
        global player
        global bullet_list
        global asteroid_list
        global star_list
        global impact_list

        bullet_list, asteroid_list, star_list, impact_list = [], [], [], []
        player = Player()
        self.framecount = 0
        self.asteroid_cooldown = 10

        for _ in range(30):
            star_list+=[Star(randint(2,102),randint(2,138),uniform(1,3))]

        pyxel.init(104, 140, title="Space Survivor")
        pyxel.load("Jeu.pyxres")
        pyxel.run(self.update, self.draw)

    def update(self):
        self.framecount += 1
        if self.framecount % self.asteroid_cooldown == 0:
            asteroid_list.append(Asteroid(randint(0,96)))
        player.update()
        for bullet in bullet_list:
            bullet.update()
        for star in star_list:
            star.update()
        for asteroid in asteroid_list:
            asteroid.update()
        for impact in impact_list:
            impact.update()

    def draw(self):
        pyxel.cls(0)
        for star in star_list:
            star.draw()
        for asteroid in asteroid_list:
            asteroid.draw()
        for bullet in bullet_list:
            bullet.draw()
        for impact in impact_list:
            impact.draw()
        player.draw()

if __name__ == "__main__":
    App()