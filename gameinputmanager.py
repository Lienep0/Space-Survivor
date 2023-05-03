from random import randint

import pyxel

from asteroids import Asteroid, asteroid_list
from constants import (ASTEROID_SPAWN_KEY, ASTEROIDS, BOMB_KEY, BOTTOM_UI_BAR_SIZE, DASH_KEY,
                       DASH_UPGRADE_SPEED_BOOST, DOWN_KEY, GAME_HEIGHT,
                       GAME_WIDTH, GIVE_BOMB_KEY, GIVE_UPGRADES_KEY,
                       GIVE_XP_KEY, LARGE_ASTEROID_KEY, LEFT_KEY,
                       MAX_NUMBER_OF_BOMBS, MEDIUM_ASTEROID_KEY,
                       MINIBOSS_SPAWN_KEY, PAUSE_KEY, PLAYER_DASH_SOUND,
                       PLAYER_SPEED, RESET_KEY, RIGHT_KEY, SHOOT_KEY,
                       SMALL_ASTEROID_KEY, UP_KEY)
from globals import change_pause_status, set_game_state, change_asteroid_toggle
from miniboss import miniboss
from player import player
from ui import ui
from upgrades import upgrade_dic


def pause_input():
    # Pause
    if pyxel.btnp(PAUSE_KEY):
        ui.cursor_position = [0,0]
        change_pause_status()

def manage_inputs():
    # Dash
    player.is_dashing = pyxel.btn(DASH_KEY) and player.has_dash
    if player.is_dashing: pyxel.play(3, PLAYER_DASH_SOUND)
    speed = PLAYER_SPEED + DASH_UPGRADE_SPEED_BOOST if player.is_dashing else PLAYER_SPEED

    # Movement
    if pyxel.btn(RIGHT_KEY):
        for i in range(speed):
            if player.x + i >= GAME_WIDTH - player.size: break
            player.x += 1
    if pyxel.btn(LEFT_KEY):
        for i in range(speed):
            if player.x - i <= 0: break
            player.x -= 1
    if pyxel.btn(DOWN_KEY):
        for i in range(speed):
            if player.y + i >= GAME_HEIGHT - player.size - BOTTOM_UI_BAR_SIZE: break
            player.y += 1
    if pyxel.btn(UP_KEY):
        for i in range(speed):
            if player.y - i <= 0: break
            player.y -= 1

    # Shooting
    if pyxel.btn(SHOOT_KEY) and player.fireRateCooldown <= 0:
        player.shoot()

    # Bomb
    if pyxel.btnp(BOMB_KEY) and player.number_of_bombs >= 1:
        player.use_bomb()

    # Dev Shortcuts
    if pyxel.btnp(ASTEROID_SPAWN_KEY): 
        change_asteroid_toggle()
    if pyxel.btnp(RESET_KEY):
        set_game_state("GAMEOVER")
        
    if pyxel.btnp(GIVE_UPGRADES_KEY):
        player.inventory.extend(upgrade_dic.values())
        player.check_upgrades()
    if pyxel.btnp(GIVE_XP_KEY):
        player.xp += 10
    if pyxel.btnp(GIVE_BOMB_KEY) and player.number_of_bombs < MAX_NUMBER_OF_BOMBS:
        player.number_of_bombs += 1

    if pyxel.btnp(MINIBOSS_SPAWN_KEY):
        miniboss.reset()
        miniboss.active = True
    if pyxel.btnp(SMALL_ASTEROID_KEY): 
        asteroid_list.append(Asteroid(0,1))
    if pyxel.btnp(MEDIUM_ASTEROID_KEY): 
        asteroid_list.append(Asteroid(1,1))
    if pyxel.btnp(LARGE_ASTEROID_KEY): 
        asteroid_list.append(Asteroid(2,1))