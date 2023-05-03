from random import uniform

import pyxel

from constants import (BOMB_UPGRADE_WEIGHT, CRITICAL_UPGRADE_CHANCE,
                       HEALTH_UPGRADE_WEIGHT, LEFT_KEY, MAXIMUM_HEALTH,
                       PIERCING_UPGRADE_CHANCE, PLAYER_IFRAMES, RIGHT_KEY,
                       UPGRADE_MENU_COOLDOWN)
from globals import set_game_state
from player import player
from upgrades import upgrade_dic


class UpgradeMenu:
    def __init__(self):
        self.upgrades_cursor_position = 0
        self.available_upgrades = dict(upgrade_dic)
        self.select_upgrade_cooldown = 0

    def choose_upgrade(self, upgrade_pool):
        # Calculate the cumulative probabilities
        cumulative_probs = []
        total_prob = 0
        for upgrade in upgrade_pool:
            total_prob += upgrade.weight
            cumulative_probs.append((upgrade, total_prob))

        # Choose a random upgrade based on the probabilities
        rand_num = uniform(0, total_prob)
        for upgrade, cum_prob in cumulative_probs:
            if rand_num < cum_prob:
                upgrade_pool.remove(upgrade)
                return upgrade

    def generate_upgrades(self):
        global current_upgrade_list
        current_upgrade_list = []

        # Dynamic weight handling
        self.available_upgrades["Health"].weight = HEALTH_UPGRADE_WEIGHT[player.hp - 1]
        self.available_upgrades["Bomb"].weight = BOMB_UPGRADE_WEIGHT[player.number_of_bombs]
        if player.crit_chance * CRITICAL_UPGRADE_CHANCE > 1: self.available_upgrades["Crit"].weight = 0
        if player.piercing_chance * PIERCING_UPGRADE_CHANCE > 1: self.available_upgrades["Piercing"].weight = 0

        abailable_upgrades_values = [upgrade for upgrade in self.available_upgrades.values()]
        for _ in range(3):
            current_upgrade_list.append(self.choose_upgrade(abailable_upgrades_values))

        self.upgrades_cursor_position = 0
    
    def confirm_upgrade(self):
        chosen_upgrade = current_upgrade_list[self.upgrades_cursor_position + 1]

        player.inventory.append(chosen_upgrade)

        if chosen_upgrade.is_unique: self.available_upgrades.pop(chosen_upgrade.name)
        
        if chosen_upgrade.has_instant_effect:
            if chosen_upgrade.name == "Bomb": player.number_of_bombs = 2
            if chosen_upgrade.name == "Health": player.hp = min(MAXIMUM_HEALTH, player.hp + 2)

        self.has_generated_upgrades = False

        player.iframes_cooldown = PLAYER_IFRAMES
        player.check_upgrades()

        set_game_state("GAME")
        
    def update(self):
        self.select_upgrade_cooldown += 1

        if pyxel.btnp(LEFT_KEY) and self.upgrades_cursor_position >= 0:
            self.upgrades_cursor_position -= 1
        if pyxel.btnp(RIGHT_KEY) and self.upgrades_cursor_position <= 0:
            self.upgrades_cursor_position += 1
        if self.select_upgrade_cooldown >= UPGRADE_MENU_COOLDOWN:
            if pyxel.btnp(pyxel.KEY_SPACE):
                self.confirm_upgrade()
    
    def draw(self):
        pyxel.text(13, 30, "Select your upgrade :", 7)

        for i in range(3):
            pyxel.blt(25 + i * 20, 50, 2, current_upgrade_list[i].coords[0], current_upgrade_list[i].coords[1], 16, 16, 0) # Upgrades
        
        for i in range(len(current_upgrade_list[self.upgrades_cursor_position + 1].description)):
            pyxel.text(15, 75 + 10 * i, current_upgrade_list[self.upgrades_cursor_position + 1].description[i], 7) # Description

        pyxel.rectb(43 + 20 * self.upgrades_cursor_position, 48, 20, 20, 7) #Cursor


upgradeMenu = UpgradeMenu()