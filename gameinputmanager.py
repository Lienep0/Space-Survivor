from random import randint

import pyxel

from asteroids import Asteroid, asteroid_list
from constants import (ASTEROID_OFFSET_FROM_BORDERS, ASTEROIDS, BOMB_SOUND,
                       BOTTOM_UI_BAR_SIZE, DASH_UPGRADE_SPEED_BOOST,
                       GAME_HEIGHT, GAME_WIDTH, PLAYER_DASH_SOUND,
                       PLAYER_SPEED)
from mainmenu import mainMenu
from miniboss import miniboss
from particles import BombExplosion, particle_list
from player import player
from globals import set_state


def manage_inputs():
    # Dash
    player.isDashing = pyxel.btn(pyxel.KEY_SHIFT) and len([x for x in player.inventory if x.name == "Dash"])
    if player.isDashing: pyxel.play(3, PLAYER_DASH_SOUND)
    speed = PLAYER_SPEED + (DASH_UPGRADE_SPEED_BOOST and player.isDashing) # MDRRRRRRR

    # Movement
    if pyxel.btn(pyxel.KEY_RIGHT) and player.x < GAME_WIDTH - player.size - 1:
        player.x += speed
    if pyxel.btn(pyxel.KEY_LEFT) and player.x > 1:
        player.x -= speed
    if pyxel.btn(pyxel.KEY_DOWN) and player.y < GAME_HEIGHT - player.size - BOTTOM_UI_BAR_SIZE - 1:
        player.y += speed
    if pyxel.btn(pyxel.KEY_UP) and player.y > 1:
        player.y -= speed

    # Shooting
    if pyxel.btn(pyxel.KEY_SPACE) and player.fireRateCooldown <= 0:
        player.shoot()

    # Bomb
    if pyxel.btn(pyxel.KEY_B) and player.hasBomb:
        pyxel.play(1, BOMB_SOUND)
        particle_list.append(BombExplosion(player.x + 3, player.y + 3))
        player.hasBomb = False

    # Dev Shortcuts
    if pyxel.btnp(pyxel.KEY_R):
        set_state("GAMEOVER")
    if pyxel.btnp(pyxel.KEY_A): 
        mainMenu.asteroid_toggle = not mainMenu.asteroid_toggle
    if pyxel.btnp(pyxel.KEY_M):
        miniboss.active = True
    if pyxel.btnp(pyxel.KEY_X):
        player.xp += 10
    if pyxel.btnp(pyxel.KEY_V):
        player.hasBomb = True
    if pyxel.btnp(pyxel.KEY_1): 
        asteroid_list.append(Asteroid(randint(
            ASTEROID_OFFSET_FROM_BORDERS, GAME_WIDTH - ASTEROIDS["SMALL_ASTEROID"]["size"] - ASTEROID_OFFSET_FROM_BORDERS),ASTEROIDS["SMALL_ASTEROID"]["type"]))
    if pyxel.btnp(pyxel.KEY_2): 
        asteroid_list.append(Asteroid(randint(
            ASTEROID_OFFSET_FROM_BORDERS, GAME_WIDTH - ASTEROIDS["MEDIUM_ASTEROID"]["size"] - ASTEROID_OFFSET_FROM_BORDERS), ASTEROIDS["MEDIUM_ASTEROID"]["type"]))
    if pyxel.btnp(pyxel.KEY_3): 
        asteroid_list.append(Asteroid(randint(
            ASTEROID_OFFSET_FROM_BORDERS, GAME_WIDTH - ASTEROIDS["LARGE_ASTEROID"]["size"] - ASTEROID_OFFSET_FROM_BORDERS), ASTEROIDS["LARGE_ASTEROID"]["type"]))