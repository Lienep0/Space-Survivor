from random import uniform

import pyxel

from asteroids import Asteroid, asteroid_list
from bombs import bombs_list
from bullets import bullet_list
from collisionmanager import check_collisions
from constants import (ASTEROIDS, BOSS_WAVES, LEVEL_UP_SOUND, MAX_LEVEL,
                       MINIBOSS_DEATH_SOUND, MINIBOSS_SCORE,
                       PLAYER_DEATH_SOUND, PLAYER_DEATHFREEZE_DURATION,
                       XP_REQUIREMENTS)
from gameinputmanager import manage_inputs, pause_input
from globals import (get_asteroid_toggle, get_framecount, get_paused_state,
                     set_game_state, update_framecount)
from miniboss import miniboss
from particles import (MinibossExplosion, PlayerExplosion,
                       ScoreParticle, particle_list)
from pickups import pickup_list
from player import player
from ui import ui
from upgrademenu import upgradeMenu


class GameManager:
    def __init__(self):
        self.reset()

    def check_upgrade(self, player):
        if player.level < MAX_LEVEL and player.xp >= XP_REQUIREMENTS[player.level]:
            pyxel.play(2, LEVEL_UP_SOUND)
            player.xp = 0
            player.level += 1

            upgradeMenu.select_upgrade_cooldown = 0
            upgradeMenu.generate_upgrades()
            set_game_state("UPGRADEMENU")

    def check_for_death(self):
        if miniboss.hp <= 0:
            pyxel.play(0, MINIBOSS_DEATH_SOUND)
            particle_list.extend([ScoreParticle(miniboss.x + miniboss.radius, miniboss.y, MINIBOSS_SCORE),
                                  MinibossExplosion(miniboss.x + miniboss.radius, miniboss.y + miniboss.radius)])
            player.minibosses_destroyed += 1
            player.score += MINIBOSS_SCORE
            miniboss.reset()

        if player.hp <= 0 :
            if self.time_of_death == -1:
                particle_list.append(PlayerExplosion(player.x + 3, player.y + 3))
                pyxel.play(0, PLAYER_DEATH_SOUND)
                player.active = False
                self.time_of_death = PLAYER_DEATHFREEZE_DURATION
            else :
                self.time_of_death -= 1
                if self.time_of_death == 0: set_game_state("GAMEOVER")

    def spawn_asteroids(self):
        # asteroid_list.append(Asteroid(0,1))
        # self.asteroid_cooldown = ASTEROIDS[0]["cooldown"]
            cumulative_probs = []
            total_prob = 0
            for i in range(len(ASTEROIDS)):
                total_prob += ASTEROIDS[i]["weight"]
                cumulative_probs.append((i, total_prob))

            rand_num = uniform(0, total_prob)
            for variety, cum_prob in cumulative_probs:
                if rand_num < cum_prob:
                    asteroid_list.append(Asteroid(variety, 1))
                    self.asteroid_cooldown = ASTEROIDS[variety]["cooldown"]
                    return

    def update(self):
        pause_input()

        if not get_paused_state():

            if get_framecount() % BOSS_WAVES == 0:
                update_framecount()
                self.asteroid_cooldown = 0
                miniboss.reset()
                miniboss.active = True

            if not miniboss.active:
                if get_asteroid_toggle():
                    update_framecount()
                    if self.asteroid_cooldown <= 0:
                        self.spawn_asteroids()
                self.asteroid_cooldown -= 1

            self.check_upgrade(player)

            if player.active:
                manage_inputs()
                player.update()

            if miniboss.active: miniboss.update()

            for element in asteroid_list + particle_list + bullet_list + pickup_list + bombs_list:
                element.update()

            check_collisions()
            self.check_for_death()

        ui.update()

    def draw(self):
        if player.active:
            for element in asteroid_list + bullet_list + pickup_list + bombs_list:
                element.draw()

            player.draw()

        if miniboss.active: miniboss.draw()

        for particle in particle_list:
            particle.draw()

        ui.draw()

    def reset(self):
        self.time_of_death = -1
        self.asteroid_cooldown = 0

gameManager = GameManager()