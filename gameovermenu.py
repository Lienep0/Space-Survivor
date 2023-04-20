import pyxel

from asteroids import asteroid_list
from bullets import bullet_list
from gamemanager import gameManager
from globals import reset_framecount, set_state
from miniboss import miniboss
from particles import particle_list
from pickups import pickup_list
from player import player


class GameOverMenu:
    def update(self):
        if pyxel.btnp(pyxel.KEY_SPACE): self.reset_game

    def draw(self):
        pyxel.blt(20, 20, 1, 0, 0, 64, 16) #GAME
        pyxel.blt(20, 36, 1, 0, 16, 64, 16) #OVER
        pyxel.text(24, 100, "Press SPACE to", 7)
        pyxel.text(22, 110, "go back to MENU", 7)

    def reset_game(self):
        reset_framecount()
        set_state("MENU")
        
        gameManager.timeofdeath = -100
        gameManager.explosion = None
        gameManager.paused = False
        
        asteroid_list.clear()
        asteroid_list.clear()
        bullet_list.clear()
        pickup_list.clear()
        particle_list.clear()

        miniboss.reset()
        player.reset()

gameOverMenu = GameOverMenu()