import pyxel

from constants import GAME_HEIGHT, GAME_WIDTH, XP_REQUIREMENTS, MAX_LEVEL, BOTTOM_UI_BAR_SIZE
from player import player

class Ui:
    def draw(self):
        if player.active:
            # Xp
            pyxel.rect(0, GAME_HEIGHT - BOTTOM_UI_BAR_SIZE, GAME_WIDTH, BOTTOM_UI_BAR_SIZE, 1)
            pyxel.blt(2, GAME_HEIGHT - 7, 0, 0, 80, 44, 5, 0) # Xp UI Outline
            if player.level <= MAX_LEVEL:
                pyxel.rect(15, GAME_HEIGHT - 6,
                            min(player.xp * 30/XP_REQUIREMENTS[player.level], 30), 
                            3, 10) #Xp UI Bar
            else:
                pyxel.rect(15, GAME_HEIGHT - 6, 30, 3, 3) #Xp UI Bar

            # Hp
            for i in range(player.hp):
                pyxel.blt(GAME_WIDTH - 9 * (i + 1), GAME_HEIGHT - 8, 0, 8, 9, 8, 7, 0) # Hearts

ui = Ui()