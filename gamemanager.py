import pyxel

from asteroids import Asteroid, asteroid_list
from bombs import bombs_list
from bullets import bullet_list
from collisionmanager import check_collisions
from constants import (ASTEROID_COOLDOWN, ASTEROIDS, LEVEL_UP_SOUND, MAX_LEVEL,
                       PLAYER_DEATH_SOUND, PLAYER_DEATHFREEZE_DURATION,
                       XP_REQUIREMENTS)
from gameinputmanager import manage_inputs, pause_input
from globals import (get_asteroid_toggle, get_framecount, get_paused_state,
                     set_game_state, update_framecount)
from miniboss import miniboss
from particles import PlayerExplosion, particle_list
from pickups import pickup_list
from player import player
from ui import ui
from upgrademenu import upgradeMenu


class GameManager:
    def __init__(self):
        self.reset()

    def check_player_upgrade(self, player):
        if player.level < MAX_LEVEL and player.xp >= XP_REQUIREMENTS[player.level]:
            pyxel.play(2, LEVEL_UP_SOUND)
            player.xp = 0
            player.level += 1
            upgradeMenu.generate_upgrades()
            set_game_state("UPGRADEMENU")

    def check_for_death(self):
        if player.hp <= 0 and self.time_of_death < 0:
            particle_list.append(PlayerExplosion(player.x + 3, player.y + 3))
            pyxel.play(0, PLAYER_DEATH_SOUND)
            player.active = False
            self.time_of_death = get_framecount()
        
        if self.time_of_death + PLAYER_DEATHFREEZE_DURATION == get_framecount() :
            set_game_state("GAMEOVER")

    def spawn_asteroids(self):
        if get_asteroid_toggle():
            if get_framecount() % ASTEROID_COOLDOWN == 0:
                asteroid_list.append(Asteroid(ASTEROIDS["SMALL_ASTEROID"]["type"]))

    def update(self):
        update_framecount()
        
        pause_input()
        self.paused = get_paused_state()

        if not self.paused:
            self.spawn_asteroids()
            self.check_player_upgrade(player)

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
        self.time_of_death = -100
        self.paused = False

gameManager = GameManager()