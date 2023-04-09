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
                pyxel.blt(2 + 8 * i, GAME_HEIGHT - 17, 0, 9, 8, 6, 8, 0) # Shields

            # Xp
            pyxel.blt(2, GAME_HEIGHT - 7, 0, 0, 80, 44, 5, 0) # Xp UI Outline
            pyxel.rect(15, GAME_HEIGHT - 6, min(player.xp, 30), 3, 10) #Xp UI Bar

ui = Ui()