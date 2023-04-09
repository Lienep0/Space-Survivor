import pyxel

from constants import GAME_HEIGHT
from player import player

class Ui:
    def __init__(self):
        pass

    def update(self):
        pass

    def draw(self):
        if player.active:
            # Hp
            for i in range(player.hp):
                pyxel.blt(2 + 8 * i, GAME_HEIGHT - 23, 0, 9, 8, 6, 8, 0) # Shields

            # Xp
            pyxel.blt(2, GAME_HEIGHT - 13, 0, 0, 80, 32, 11, 0) # Xp UI Outline
            pyxel.rect(3, GAME_HEIGHT - 6, min(player.xp, 30), 3, 10) #Xp UI Bar

ui = Ui()