from random import randint,uniform
import pyxel

bullet_list, asteroid_list, star_list, impact_list = [], [], [], []
framecount = 0

class App:
    def __init__(self):
        self.asteroid_cooldown = 10
        self.player = Player()

        for _ in range(30):
            star_list.append(Star(randint(2,102),randint(2,138),uniform(2,4)))

        pyxel.init(104, 140, title="Space Survivor")
        pyxel.load("Jeu.pyxres")
        pyxel.run(self.update, self.draw)

    def update(self):
        global framecount
        framecount += 1
        if framecount % self.asteroid_cooldown == 0: #Génère un astéroide toutes les "asteroid_cooldown" frames
            asteroid_list.append(Asteroid(randint(0,96)))

        self.player.update()
        for element in star_list + asteroid_list + impact_list + bullet_list:
            element.update()

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
        self.player.draw()

if __name__ == "__main__":
    game = App()