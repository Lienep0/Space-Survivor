from random import randint

import pyxel

from asteroids import Asteroid, asteroid_list
from bullets import bullet_list
from constants import (ASTEROID_COOLDOWN, ASTEROID_OFFSET_FROM_BORDERS,
                       ASTEROIDS, GAME_WIDTH, LEVEL_UP_SOUND, MAX_LEVEL,
                       PLAYER_DEATH_SOUND, PLAYER_DEATHFREEZE_DURATION,
                       XP_REQUIREMENTS)
from gameinputmanager import manage_inputs
from globals import get_framecount, set_state, update_framecount
from mainmenu import mainMenu
from miniboss import miniboss
from particles import PlayerExplosion, particle_list
from pickups import pickup_list
from player import player
from ui import ui


class GameManager:
    def __init__(self):
        self.reset()

    def check_player_upgrade(self, player):
        if player.level < MAX_LEVEL and player.xp >= XP_REQUIREMENTS[player.level]:
            pyxel.play(2, LEVEL_UP_SOUND)
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

        if not self.paused:
            self.spawn_asteroids()
            self.check_player_upgrade(player)

            if player.active:
                inputs = manage_inputs()
                if inputs is not None: self.bombList.append(inputs)

                for bomb in self.bombList:
                    bomb.update()
                    if bomb.timer >= 22:
                        self.bombList.remove(bomb)

                player.update()

            if miniboss.active: miniboss.update()

            for element in asteroid_list + particle_list + bullet_list + pickup_list: #Evil python hack
                element.update()

            self.check_for_death()

    def draw(self):
        if player.active:
            for element in asteroid_list + bullet_list + pickup_list:
                element.draw()

            for bomb in self.bombList:
                    bomb.draw()

            player.draw()

        if miniboss.active: miniboss.draw()

        for particle in particle_list:
            particle.draw()

        ui.draw()

        if self.paused: pyxel.blt(28, 30, 0, 0, 112, 48, 8, 0) # PAUSED

    def reset(self):
        self.timeofdeath = -100
        self.paused = False
        self.bombList = []

gameManager = GameManager()