import pyxel

from game import App, generate_stars
from stars import star_list
from constants import *

class Menu:
    def __init__(self):
        self.app = App()
        self.in_menu = True
        generate_stars()

        pyxel.init(GAME_WIDTH, GAME_HEIGHT, title="Space Survivor")
        pyxel.load("game.pyxres")
        pyxel.run(self.update, self.draw)

    def update(self):
        for star in star_list:
            star.update()        
        if self.in_menu:
            if pyxel.btn(pyxel.KEY_SPACE):
                self.in_menu = False
        else: 
            self.app.update()

    def draw(self):
        pyxel.cls(0)
        for star in star_list:
            star.draw()
        if self.in_menu:
            pyxel.blt(24, 50, 0, 8, 64, 40, 8) #SPACE
            pyxel.blt(16, 58, 0, 0, 72, 64, 8) #SURVIVOR
            pyxel.blt(PLAYER_STARTING_X, PLAYER_STARTING_Y, 0, 0, 8, 8, 8, 0) #PLAYER
        else: 
            self.app.draw()

game = Menu()