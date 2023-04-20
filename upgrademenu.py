from random import randrange

import pyxel

from constants import EXPLODING_UPGRADE_CHANCE, MAXIMUM_HEALTH, PLAYER_IFRAMES
from globals import set_state
from player import player
from upgrades import upgrade_list


class UpgradeMenu:
    def __init__(self):
        self.hasgeneratedupgrades = False
        self.upgradescursorposition = 0

    def generate_upgrades(self):
        global current_upgrade_list
        current_upgrade_list = []
        upgrade_list_buffer = list(upgrade_list)

        # Remove redundant upgrades
        if player.hasBomb: upgrade_list_buffer = [x for x in upgrade_list_buffer if x.name != "Bomb"]
        if player.hp >= MAXIMUM_HEALTH: upgrade_list_buffer = [x for x in upgrade_list_buffer if x.name != "Health"]
        if len([x for x in player.inventory if x.name == "Explosions"]) * EXPLODING_UPGRADE_CHANCE > 100:
            upgrade_list_buffer = [x for x in upgrade_list_buffer if x.name != "Explosions"]

        current_upgrade_list.append(upgrade_list_buffer.pop(randrange(0,len (upgrade_list_buffer))))
        current_upgrade_list.append(upgrade_list_buffer.pop(randrange(0,len (upgrade_list_buffer))))
        current_upgrade_list.append(upgrade_list_buffer.pop(randrange(0,len (upgrade_list_buffer))))

        self.hasgeneratedupgrades = True
    
    def update(self):
        if not self.hasgeneratedupgrades:
            self.generate_upgrades()
        
        if pyxel.btnp(pyxel.KEY_LEFT) and self.upgradescursorposition >= 0:
            self.upgradescursorposition -= 1
        if pyxel.btnp(pyxel.KEY_RIGHT) and self.upgradescursorposition <= 0:
            self.upgradescursorposition += 1
        if pyxel.btnp(pyxel.KEY_SPACE):
            self.hasgeneratedupgrades = False
            player.iFramesCooldown = PLAYER_IFRAMES
            chosen_upgrade = current_upgrade_list[self.upgradescursorposition + 1]
            player.inventory.append(chosen_upgrade)
            if chosen_upgrade.is_unique: upgrade_list.remove(chosen_upgrade)
            if chosen_upgrade.instant_effect:
                if chosen_upgrade.name == "Bomb": player.hasBomb = True
                if chosen_upgrade.name == "Health": player.hp += 1
            set_state("GAME")
    
    def draw(self):
        pyxel.text(13, 30, "Select your upgrade :", 7)

        pyxel.blt(25, 50, 0, current_upgrade_list[0].coords[0], current_upgrade_list[0].coords[1], 16, 16, 0) # UPGRADE 1
        pyxel.blt(45, 50, 0, current_upgrade_list[1].coords[0], current_upgrade_list[1].coords[1], 16, 16, 0) # UPGRADE 2
        pyxel.blt(65, 50, 0, current_upgrade_list[2].coords[0], current_upgrade_list[2].coords[1], 16, 16, 0) # UPGRADE 3
        
        for i in range(len(current_upgrade_list[self.upgradescursorposition + 1].description)): # DESCRIPTION LINES
            pyxel.text(15, 75 + 10 * i, current_upgrade_list[self.upgradescursorposition + 1].description[i], 7)

        pyxel.rectb(43 + 20 * self.upgradescursorposition, 48, 20, 20, 7) #CURSOR

upgradeMenu = UpgradeMenu()