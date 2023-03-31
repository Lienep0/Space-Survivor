import pyxel

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
            bullet = Bullet(player.x + 1, player.y)
            bullet2 = Bullet(player.x + 6, player.y)
            bullet_list.extend([bullet,bullet2])

    def update(self):
        self.fireRateCooldown -= 1
        self.player_controls()

    def draw(self):
        pyxel.blt(self.x, self.y, 0, 0, 8, 8, 8)

class Bullet:
    def __init__(self,x,y):
        self.x = x
        self.y = y

    def update(self):
        self.y -= 3
        if self.y < -8:
            bullet_list.remove(self)

    def draw(self):
        for bullet in bullet_list:
                pyxel.blt(bullet.x, bullet.y, 0, 0, 0, 1, 8)

class Asteroid():
    def __init__(self,x,y):
        self.x = x
        self.y = y

    def update(self):
        pass

    def draw(self):
        for asteroid in asteroid_list:
                pyxel.blt(asteroid.x, asteroid.y, 0, 32, 16, 8, 8)

class App:
    def __init__(self):
        global player
        global bullet_list
        global asteroid_list

        bullet_list = []
        asteroid = Asteroid(0,0)
        asteroid_list = [asteroid]
        player = Player()

        pyxel.init(104, 140, title="SpaceFucker")
        pyxel.load("Jeu.pyxres")
        pyxel.run(self.update, self.draw)
    
    def update(self):
        player.update()
        for bullet in bullet_list:
            bullet.update()

    def draw(self):
        pyxel.cls(0)
        for asteroid in asteroid_list:
            asteroid.draw()
        for bullet in bullet_list:
            bullet.draw()
        player.draw()
        
        
if __name__ == "__main__":
    App()