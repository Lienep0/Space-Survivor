import pyxel

from constants import PLAYER_STARTING_X, PLAYER_STARTING_Y
from globals import set_game_state, get_asteroid_toggle
from Antonin.scoremanager import scoreManager


class MainMenu:
    def update(self):
        if pyxel.btnp(pyxel.KEY_SPACE):
            set_game_state("GAME")
        if pyxel.btnp(pyxel.KEY_9):
            scoreManager.update()
        if pyxel.btnp(pyxel.KEY_8):
            scoreManager.reset()

    def draw(self):
        if get_asteroid_toggle():
            pyxel.circ(5, 5, 3, 11)
        else:
            pyxel.circ(5, 5, 3, 8)

        pyxel.text(13, 3, "8 to reset high scores", 7)
        pyxel.blt(32, 16, 0, 8, 64, 40, 8, 0) #SPACE
        pyxel.blt(23, 24, 0, 0, 72, 64, 8, 0) #SURVIVOR

        pyxel.text(27, 48, "High scores :", 7)

        pyxel.text(30, 65, "XXX  000000", 7)
        pyxel.text(30, 75, "XXX  000000", 7)
        pyxel.text(30, 85, "XXX  000000", 7)
        scoreManager.draw_menu()

        pyxel.text(10, 105, "Press SPACE to Start !", 7)

        pyxel.blt(PLAYER_STARTING_X, PLAYER_STARTING_Y, 0, 64, 0, 8, 8, 0) #PLAYER
    
mainMenu = MainMenu()