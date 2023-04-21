import pyxel

from constants import PLAYER_STARTING_X, PLAYER_STARTING_Y
from globals import set_state


class MainMenu:
    def __init__(self):
        self.asteroid_toggle = True
        
    def update(self):
        if pyxel.btnp(pyxel.KEY_SPACE):
            set_state("GAME")
        if pyxel.btnp(pyxel.KEY_A):
            self.asteroid_toggle = not self.asteroid_toggle

    def draw(self):
        pyxel.blt(32, 16, 0, 8, 64, 40, 8, 0) #SPACE
        pyxel.blt(23, 24, 0, 0, 72, 64, 8, 0) #SURVIVOR
        pyxel.text(27, 48, "High scores :", 7)
        pyxel.text(30, 65, "XXX  000000", 7)
        pyxel.text(30, 75, "XXX  000000", 7)
        pyxel.text(30, 85, "XXX  000000", 7)
        pyxel.text(10, 105, "Press SPACE to Start !", 7)
        pyxel.blt(PLAYER_STARTING_X, PLAYER_STARTING_Y, 0, 0, 8, 8, 8, 0) #PLAYER
        if self.asteroid_toggle:
            pyxel.circ(5, 5, 3, 11)
        else:
            pyxel.circ(5, 5, 3, 8)
    
mainMenu = MainMenu()