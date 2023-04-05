import pyxel

from game import App
from stars import *
from constants import *
from player import player
from particles import particle_list
from bullets import bullet_list
from asteroids import asteroid_list
from pickups import pickup_list

class Menu:
    def __init__(self):
        self.app = App()
        self.state = "MAIN_MENU"
        generate_stars()

        pyxel.init(GAME_WIDTH, GAME_HEIGHT, title=TITLE, fps=FPS)
        pyxel.load("game.pyxres")
        pyxel.run(self.update, self.draw)

    def update(self):
        if pyxel.btnp(pyxel.KEY_R):
            reset_game(self)
        for star in star_list:
            star.update()        
        if self.state == "MAIN_MENU":
            if pyxel.btnp(pyxel.KEY_SPACE):
                self.state = "GAME"
        elif self.state == "GAME_OVER":
            if pyxel.btnp(pyxel.KEY_SPACE):
                self.state = "MAIN_MENU"
        else: 
            for asteroid in asteroid_list:
                if abs(asteroid.x - player.x) < 8 and abs(asteroid.y - player.y) < 8:
                    reset_game(self)
            self.app.update()

    def draw(self):
        pyxel.cls(0)
        for star in star_list:
            star.draw()
        if self.state == "MAIN_MENU":
            pyxel.blt(32, 20, 0, 8, 64, 40, 8, 0) #SPACE
            pyxel.blt(23, 28, 0, 0, 72, 64, 8, 0) #SURVIVOR
            pyxel.text(27, 48, "High scores :", 7)
            pyxel.text(30, 60, "XXX  000000", 7)
            pyxel.text(30, 70, "XXX  000000", 7)
            pyxel.text(30, 80, "XXX  000000", 7)
            pyxel.text(10, 100, "Press SPACE to Start !", 7)
            pyxel.blt(PLAYER_STARTING_X, PLAYER_STARTING_Y, 0, 0, 8, 8, 8, 0) #PLAYER
        elif self.state == "GAME_OVER":
            pyxel.blt(20, 20, 1, 0, 0, 64, 16) #GAME
            pyxel.blt(20, 36, 1, 0, 16, 64, 16) #OVER
            pyxel.text(24, 42, ":/", 7)
            pyxel.text(24, 90, "Press SPACE to", 7)
            pyxel.text(22, 100, "go back to MENU", 7)
        else: 
            self.app.draw()

def reset_game(game):
    global framecount

    framecount = 0
    game.state = "GAME_OVER"
    star_list.clear()
    asteroid_list.clear()
    asteroid_list.clear()
    bullet_list.clear()
    pickup_list.clear()
    particle_list.clear()
    player.x = PLAYER_STARTING_X
    player.y = PLAYER_STARTING_Y

    generate_stars()

game = Menu()