import pyxel

from constants import (BOTTOM_UI_BAR_SIZE, DOWN_KEY, GAME_HEIGHT, GAME_WIDTH,
                       LEFT_KEY, MAX_LEVEL, MAX_NUMBER_OF_BOMBS, MINIBOSS_HP,
                       RIGHT_KEY, UP_KEY, XP_REQUIREMENTS, MINIBOSS_HEIGHT)
from globals import get_paused_state, get_framecount
from miniboss import miniboss
from player import player


class Ui:
    def __init__(self) -> None:
        self.cursor_position = [0,0]

    def update(self):
        global lenght
        lenght = len(player.inventory)

        if get_paused_state():
            if pyxel.btnp(RIGHT_KEY) and self.cursor_position[0] < min(7, lenght - 1 - 8 * self.cursor_position[1]):
                self.cursor_position[0] += 1
            if pyxel.btnp(LEFT_KEY) and self.cursor_position[0] > 0:
                self.cursor_position[0] -= 1
            if pyxel.btnp(DOWN_KEY) and (self.cursor_position[1] + 1) * 8 + self.cursor_position[0] < lenght:
                self.cursor_position[1] += 1
            if pyxel.btnp(UP_KEY) and self.cursor_position[1] > 0:
                self.cursor_position[1] -= 1

    def draw(self):
        if get_paused_state():

            pyxel.rect(10, 20, GAME_WIDTH - 20, max(24, 24 + 10 * ((lenght - 1) // 8)), 1) # Outer blue box
            pyxel.rect(12, 32, GAME_WIDTH - 24, max(10, 10 + 10 * ((lenght - 1) // 8)), 5) # Inner grey box
            pyxel.blt(12, 22, 0, 0, 120, 67, 8, 0) # INVENTORY:

            for i in range(lenght):
                pyxel.blt(13 + i % 8 * 10, 33 + i // 8 * 10, 2, player.inventory[i].coords[0]/2, 32 + player.inventory[i].coords[1]/2, 8, 8, 0) # Upgrades

            if lenght >= 1: pyxel.rectb(12 + self.cursor_position[0] * 10, 32 + self.cursor_position[1] * 10, 10, 10, 7) # Cursor

            if len(player.inventory) > 0: # Upgrade Description
                description_lenght = len(player.inventory[self.cursor_position[1] * 8 + self.cursor_position[0]].description)
                window_offset = max(24, 24 + 10 * ((lenght - 1) // 8))

                pyxel.rect(11, 24 + window_offset, GAME_WIDTH - 22, 4 + 10 * description_lenght, 1) # Outer blue box
                pyxel.rect(13, 26 + window_offset, GAME_WIDTH - 26, 10 * description_lenght, 5) # Inner grey box

                for i in range(description_lenght): # DESCRIPTION LINES
                    pyxel.text(15, 28 + window_offset + 10 * i, player.inventory[self.cursor_position[1] * 8 + self.cursor_position[0]].description[i], 7)

        if miniboss.y > MINIBOSS_HEIGHT:
            # Miniboss Healthbar Outline
            pyxel.rect(2, 2, GAME_WIDTH - 4, 8, 1)

            #Miniboss Healthbar
            pyxel.rect(3, 3, miniboss.hp * (GAME_WIDTH - 6) / MINIBOSS_HP, 6, 8)

        if player.active:
            # Score
            pyxel.text(2, 2, f"SCORE: {player.score}", 7)

            # Framecount : 
            pyxel.text(2, 10, f"FRAMECOUNT: {get_framecount()}", 7)

            # UI bottom bar
            pyxel.rect(0, GAME_HEIGHT - BOTTOM_UI_BAR_SIZE, GAME_WIDTH, BOTTOM_UI_BAR_SIZE, 1)

            # Xp
            pyxel.blt(2, GAME_HEIGHT - 7, 0, 0, 80, 44, 5, 0) # Xp UI Outline
            if player.level < MAX_LEVEL:
                pyxel.rect(15, GAME_HEIGHT - 6, min(player.xp * 30/XP_REQUIREMENTS[player.level], 30), 3, 10) #Xp UI Bar
            else:
                pyxel.rect(15, GAME_HEIGHT - 6, 30, 3, 3) #Xp UI Bar full

            # Hp
            for i in range(player.hp):
                pyxel.blt(GAME_WIDTH - 9 * (i + 1), GAME_HEIGHT - 9, 0, 8, 8, 8, 8, 0) # Hearts

            # Bomb
            for i in range(MAX_NUMBER_OF_BOMBS):
                if i < player.number_of_bombs:
                    pyxel.blt(47 + i * 8, GAME_HEIGHT - 9, 0, 32, 32, 8, 8, 0) # Full Bomb
                else:
                    pyxel.blt(47 + i * 8, GAME_HEIGHT - 9, 0, 40, 32, 8, 8, 0) # Empty Bomb

ui = Ui()