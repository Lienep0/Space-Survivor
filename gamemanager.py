from random import randint

import pyxel

from asteroids import Asteroid, asteroid_list
from bullets import bullet_list
from constants import (ASTEROID_COOLDOWN, ASTEROID_OFFSET_FROM_BORDERS,
                       ASTEROIDS, BOMB_SOUND, GAME_WIDTH, MAX_LEVEL,
                       PLAYER_DEATH_SOUND, PLAYER_DEATHFREEZE_DURATION,
                       XP_REQUIREMENTS)
from gameovermenu import gameOverMenu
from globals import get_framecount, set_state, update_framecount
from mainmenu import mainMenu
from miniboss import miniboss
from particles import BombExplosion, PlayerExplosion, particle_list
from pickups import pickup_list
from player import player
from ui import ui


class GameManager:
    def __init__(self):
        self.reset()

    def check_dev_shortcuts(self): # DEV SHORTCUTS, NEED TO REMOVE BEFORE IT'S DONE
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

    def check_player_upgrade(self, player):
        if player.level < MAX_LEVEL and player.xp >= XP_REQUIREMENTS[player.level]:
            player.xp = 0
            player.level += 1
            set_state("UPGRADEMENU")

    def check_for_death(self):
        if player.hp <= 0 and self.timeofdeath < 0:
            particle_list.append(PlayerExplosion(player.x + 3, player.y + 3))
            pyxel.play(0, PLAYER_DEATH_SOUND)
            player.active = False
            self.timeofdeath = get_framecount()
        
        if self.timeofdeath + PLAYER_DEATHFREEZE_DURATION == get_framecount() :
            set_state("GAMEOVER")

    def spawn_asteroids(self):
        if mainMenu.asteroid_toggle:
            if get_framecount() % ASTEROID_COOLDOWN == 0: #Génère un astéroide toutes les "ASTEROID_COOLDOWN" frames
                asteroid_list.append(Asteroid(randint(
                    ASTEROID_OFFSET_FROM_BORDERS, GAME_WIDTH - ASTEROIDS["SMALL_ASTEROID"]["size"]- ASTEROID_OFFSET_FROM_BORDERS), ASTEROIDS["SMALL_ASTEROID"]["type"]))

    def update(self):
        update_framecount()

        if pyxel.btnp(pyxel.KEY_P):
            self.paused = not self.paused

        self.check_dev_shortcuts()

        if not self.paused:
            # Bomb
            if pyxel.btn(pyxel.KEY_B) and player.hasBomb:
                pyxel.play(1, BOMB_SOUND)
                self.explosion = BombExplosion(player.x + 3, player.y + 3)
                particle_list.append(self.explosion)
                player.hasBomb = False

            if self.explosion is not None:
                for asteroid in asteroid_list:
                    dx = asteroid.x + (asteroid.parameters.size/2 - .5) - self.explosion.x
                    dy = asteroid.y + (asteroid.parameters.size/2 - .5) - self.explosion.y
                    if pyxel.sqrt(dx ** 2 + dy ** 2) <= self.explosion.radius:
                        asteroid.parameters.hp -= 100
                if self.explosion.timer == 22:
                    particle_list.remove(self.explosion)
                    self.explosion = None

            self.spawn_asteroids()
            self.check_player_upgrade(player)

            if player.active: player.update()
            if miniboss.active: miniboss.update()

            for element in asteroid_list + particle_list + bullet_list + pickup_list: #Evil python hack
                element.update()

            self.check_for_death()

    def draw(self):
        if player.active:
            for element in asteroid_list + bullet_list + pickup_list:
                element.draw()
            player.draw()
        if miniboss.active: miniboss.draw()
        for particle in particle_list:
            particle.draw()
        ui.draw()
        if self.paused: pyxel.blt(28, 30, 0, 0, 112, 48, 8, 0) # PAUSED

    def reset(self):
        self.timeofdeath = -100
        self.paused = False
        self.explosion = None

gameManager = GameManager()