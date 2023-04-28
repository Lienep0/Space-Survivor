from random import randint

import pyxel

from asteroids import Asteroid, asteroid_list
from constants import (ASTEROID_OFFSET_FROM_BORDERS, ASTEROIDS,
                       BOTTOM_UI_BAR_SIZE, DASH_UPGRADE_SPEED_BOOST,
                       GAME_HEIGHT, GAME_WIDTH, MAX_NUMBER_OF_BOMBS,
                       PLAYER_DASH_SOUND, PLAYER_SPEED)
from globals import change_pause_status, set_game_state
from mainmenu import mainMenu
from miniboss import miniboss
from player import player
from ui import ui
from upgrades import upgrade_dic


def pause_input():
    # Pause
    if pyxel.btnp(pyxel.KEY_TAB):
        ui.cursor_position = [0,0]
        change_pause_status()

def manage_inputs():
    # Dash
    player.isDashing = pyxel.btn(pyxel.KEY_SHIFT) and player.has_dash
    if player.isDashing: pyxel.play(3, PLAYER_DASH_SOUND)
    speed = PLAYER_SPEED + (DASH_UPGRADE_SPEED_BOOST and player.isDashing) # MDRRRRRRR

    # Movement
    if pyxel.btn(pyxel.KEY_RIGHT):
        for i in range(speed):
            if player.x + i >= GAME_WIDTH - player.size: break
            player.x += 1
    if pyxel.btn(pyxel.KEY_LEFT):
        for i in range(speed):
            if player.x - i <= 0: break
            player.x -= 1
    if pyxel.btn(pyxel.KEY_DOWN):
        for i in range(speed):
            if player.y + i >= GAME_HEIGHT - player.size - BOTTOM_UI_BAR_SIZE: break
            player.y += 1
    if pyxel.btn(pyxel.KEY_UP):
        for i in range(speed):
            if player.y - i <= 0: break
            player.y -= 1

    # Shooting
    if pyxel.btn(pyxel.KEY_SPACE) and player.fireRateCooldown <= 0:
        player.shoot()

    # Bomb
    if pyxel.btnp(pyxel.KEY_B) and player.number_of_bombs >= 1:
        player.use_bomb()

    # Dev Shortcuts
    if pyxel.btnp(pyxel.KEY_R):
        set_game_state("GAMEOVER")
    if pyxel.btnp(pyxel.KEY_A): 
        mainMenu.asteroid_toggle = not mainMenu.asteroid_toggle
    if pyxel.btnp(pyxel.KEY_M):
        miniboss.reset()
        miniboss.active = True
    if pyxel.btnp(pyxel.KEY_U):
        player.inventory.extend(upgrade_dic.values())
        player.check_upgrades()
    if pyxel.btnp(pyxel.KEY_X):
        player.xp += 10
    if pyxel.btnp(pyxel.KEY_V) and player.number_of_bombs < MAX_NUMBER_OF_BOMBS:
        player.number_of_bombs += 1
    if pyxel.btnp(pyxel.KEY_1): 
        asteroid_list.append(Asteroid(randint(
            ASTEROID_OFFSET_FROM_BORDERS, GAME_WIDTH - ASTEROIDS["SMALL_ASTEROID"]["size"] - ASTEROID_OFFSET_FROM_BORDERS),ASTEROIDS["SMALL_ASTEROID"]["type"]))
    if pyxel.btnp(pyxel.KEY_2): 
        asteroid_list.append(Asteroid(randint(
            ASTEROID_OFFSET_FROM_BORDERS, GAME_WIDTH - ASTEROIDS["MEDIUM_ASTEROID"]["size"] - ASTEROID_OFFSET_FROM_BORDERS), ASTEROIDS["MEDIUM_ASTEROID"]["type"]))
    if pyxel.btnp(pyxel.KEY_3): 
        asteroid_list.append(Asteroid(randint(
            ASTEROID_OFFSET_FROM_BORDERS, GAME_WIDTH - ASTEROIDS["LARGE_ASTEROID"]["size"] - ASTEROID_OFFSET_FROM_BORDERS), ASTEROIDS["LARGE_ASTEROID"]["type"]))