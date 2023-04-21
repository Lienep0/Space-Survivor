from random import uniform

import pyxel

from constants import (BOMB_UPGRADE_WEIGHT, EXPLODING_UPGRADE_CHANCE,
                       HEALTH_UPGRADE_WEIGHT, PIERCING_UPGRADE_CHANCE,
                       PLAYER_IFRAMES)
from globals import set_game_state
from player import player
from upgrades import upgrade_dic


class UpgradeMenu:
    def __init__(self):
        self.hasgeneratedupgrades = False
        self.upgradescursorposition = 0

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
        upgrade_dic["Health"].weight = HEALTH_UPGRADE_WEIGHT[player.hp - 1]
        upgrade_dic["Bomb"].weight = BOMB_UPGRADE_WEIGHT[player.number_of_bombs]
        if len([x for x in player.inventory if x.name == "Explosions"]) * EXPLODING_UPGRADE_CHANCE > 1: 
            upgrade_dic["Explosion"].weight = 0
        if len([x for x in player.inventory if x.name == "Piercing"]) * PIERCING_UPGRADE_CHANCE > 1: 
            upgrade_dic["Piercing"].weight = 0

        upgrade_dic_values = [x for x in upgrade_dic.values()]
        for _ in range(3):
            current_upgrade_list.append(self.choose_upgrade(upgrade_dic_values))

        self.hasgeneratedupgrades = True
    
    def confirm_upgrade(self):
        chosen_upgrade = current_upgrade_list[self.upgradescursorposition + 1]

        player.inventory.append(chosen_upgrade)

        if chosen_upgrade.is_unique: upgrade_dic.pop(chosen_upgrade.name)
        
        if chosen_upgrade.instant_effect:
            if chosen_upgrade.name == "Bomb": player.number_of_bombs += 1
            if chosen_upgrade.name == "Health": player.hp += 1

        self.hasgeneratedupgrades = False
        self.upgradescursorposition = 0
        player.iFramesCooldown = PLAYER_IFRAMES

        set_game_state("GAME")
        
    def update(self):
        if not self.hasgeneratedupgrades:
            self.generate_upgrades()
        
        if pyxel.btnp(pyxel.KEY_LEFT) and self.upgradescursorposition >= 0:
            self.upgradescursorposition -= 1
        if pyxel.btnp(pyxel.KEY_RIGHT) and self.upgradescursorposition <= 0:
            self.upgradescursorposition += 1
    
    def draw(self):
        pyxel.text(13, 30, "Select your upgrade :", 7)

        pyxel.blt(25, 50, 2, current_upgrade_list[0].coords[0], current_upgrade_list[0].coords[1], 16, 16, 0) # UPGRADE 1
        pyxel.blt(45, 50, 2, current_upgrade_list[1].coords[0], current_upgrade_list[1].coords[1], 16, 16, 0) # UPGRADE 2
        pyxel.blt(65, 50, 2, current_upgrade_list[2].coords[0], current_upgrade_list[2].coords[1], 16, 16, 0) # UPGRADE 3
        
        for i in range(len(current_upgrade_list[self.upgradescursorposition + 1].description)): # DESCRIPTION LINES
            pyxel.text(15, 75 + 10 * i, current_upgrade_list[self.upgradescursorposition + 1].description[i], 7)

        pyxel.rectb(43 + 20 * self.upgradescursorposition, 48, 20, 20, 7) #CURSOR

        if pyxel.btnp(pyxel.KEY_SPACE):
            self.confirm_upgrade()

upgradeMenu = UpgradeMenu()