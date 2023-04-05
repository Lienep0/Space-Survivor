import pyxel

from game import App, generate_stars
from player import *
from asteroids import *
from stars import *
from pickups import *
from constants import *

class Menu:
    def __init__(self):
        self.app = App()
        self.in_menu = True
        generate_stars()

        pyxel.init(GAME_WIDTH, GAME_HEIGHT, title=TITLE, fps=FPS)
        pyxel.load("game.pyxres")
        pyxel.run(self.update, self.draw)

    def update(self):
        if pyxel.btn(pyxel.KEY_R):
            reset_game(self)
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
            pyxel.blt(32, 20, 0, 8, 64, 40, 8, 0) #SPACE
            pyxel.blt(23, 28, 0, 0, 72, 64, 8, 0) #SURVIVOR
            pyxel.text(27, 48, "High scores :", 7)
            pyxel.text(30, 60, "XXX  000000", 7)
            pyxel.text(30, 70, "XXX  000000", 7)
            pyxel.text(30, 80, "XXX  000000", 7)
            pyxel.text(10, 100, "Press SPACE to Start !", 7)
            pyxel.blt(PLAYER_STARTING_X, PLAYER_STARTING_Y, 0, 0, 8, 8, 8, 0) #PLAYER
        else: 
            self.app.draw()

def reset_game(menu):
    global framecount

    framecount = 0
    menu.in_menu = True
    star_list.clear()
    asteroid_list.clear()
    asteroid_list.clear()
    bullet_list.clear()
    pickup_list.clear()

    generate_stars()

menu = Menu()
game = Menu()