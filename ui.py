import pyxel

from constants import (BOTTOM_UI_BAR_SIZE, GAME_HEIGHT, GAME_WIDTH, MAX_LEVEL,
                       MAX_NUMBER_OF_BOMBS, XP_REQUIREMENTS, MINIBOSS_HP)
from miniboss import miniboss
from player import player
from globals import get_paused_state


class Ui:
    def __init__(self) -> None:
        self.cursor_position = [0,0]

    def update(self):
        global lenght
        lenght = len(player.inventory)

        if get_paused_state():
            if pyxel.btnp(pyxel.KEY_LEFT) and self.cursor_position[0] > 0:
                self.cursor_position[0] -= 1
            if pyxel.btnp(pyxel.KEY_UP) and self.cursor_position[1] > 0:
                self.cursor_position[1] -= 1
            if pyxel.btnp(pyxel.KEY_RIGHT) and self.cursor_position[0] < min(7, lenght - 1 - 8 * self.cursor_position[1]):
                self.cursor_position[0] += 1
            if pyxel.btnp(pyxel.KEY_DOWN) and (self.cursor_position[1] + 1) * 8 + self.cursor_position[0] < lenght:
                self.cursor_position[1] += 1

    def draw(self):
        if get_paused_state():

            pyxel.rect(10, 30, GAME_WIDTH - 20, max(24, 24 + 10 * ((lenght - 1) // 8)), 1) # Outer blue box
            pyxel.rect(12, 42, GAME_WIDTH - 24, max(10, 10 + 10 * ((lenght - 1) // 8)), 5) # Inner grey box
            pyxel.blt(12, 32, 0, 0, 120, 67, 8, 0) # INVENTORY:

            for i in range(lenght):
                pyxel.blt(13 + i % 8 * 10, 43 + i // 8 * 10, 2, player.inventory[i].coords[0]/2, 32 + player.inventory[i].coords[1]/2, 8, 8, 0)

            if lenght >= 1: pyxel.rectb(12 + self.cursor_position[0] * 10, 42 + self.cursor_position[1] * 10, 10, 10, 7) # Cursor

            if len(player.inventory) > 0: # Upgrade Description
                description_lenght = len(player.inventory[self.cursor_position[1] * 8 + self.cursor_position[0]].description)

                pyxel.rect(11, 71, GAME_WIDTH - 22, 4 + 10 * description_lenght, 1) # Outer blue box
                pyxel.rect(13, 73, GAME_WIDTH - 26, 10 * description_lenght, 5) # Inner grey box

                for i in range(description_lenght): # DESCRIPTION LINES
                    pyxel.text(15, 75 + 10 * i, player.inventory[self.cursor_position[1] * 8 + self.cursor_position[0]].description[i], 7)

        if miniboss.active:
            # Miniboss Healthbar Outline
            pyxel.rect(2, 2, GAME_WIDTH - 4, 8, 1)

            #Miniboss Healthbar
            pyxel.rect(3, 3, miniboss.hp * (GAME_WIDTH - 6) / MINIBOSS_HP, 6, 8)

        if player.active:
            # UI background
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