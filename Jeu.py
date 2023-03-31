import pyxel

tirs_liste = []

class Player:
    def __init__(self):
        self.ship_x = 60
        self.ship_y = 60
    
    def player_controls(self):
        if pyxel.btn(pyxel.KEY_RIGHT) and self.ship_x<120:
            self.ship_x += 2
        if pyxel.btn(pyxel.KEY_LEFT) and self.ship_x>0:
            self.ship_x += -2
        if pyxel.btn(pyxel.KEY_DOWN) and self.ship_y<120:
            self.ship_y += 2
        if pyxel.btn(pyxel.KEY_UP) and self.ship_y>0:
            self.ship_y += -2

    def update(self):
        self.player_controls()
        if pyxel.btn(pyxel.KEY_SPACE):
            tir = Bullet(player.ship_x, player.ship_y-8)
            tirs_liste.append(tir)

    def draw(self):
        pyxel.blt(self.ship_x, self.ship_y, 0, 0, 8, 8, 8)

class Bullet:
    def __init__(self,x,y):
        self.x=x
        self.y=y

    def update(self):
        self.y -= 3
        if self.y <-8:
            tirs_liste.remove(self)

    def draw(self):
        for tir in tirs_liste:
                pyxel.blt(tir.x, tir.y, 0, 8, 0, 8, 8)

class App:
    def __init__(self):
        global player
        player = Player()
        pyxel.init(128, 128, title="SpaceFucker")
        pyxel.load("Jeu.pyxres")
        pyxel.run(self.update, self.draw)
    
    def update(self):
        player.update()
        for tir in tirs_liste:
            tir.update()

    def draw(self):
        pyxel.cls(0)
        player.draw()
        for tir in tirs_liste:
            tir.draw()
        
if __name__ == "__main__":
    App()