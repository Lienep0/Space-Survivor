import pyxel

from asteroids import asteroid_list
from bullets import bullet_list
from constants import FPS, GAME_HEIGHT, GAME_WIDTH, TITLE
from gamemanager import gameManager
from gameovermenu import gameOverMenu
from globals import (get_game_state, get_paused_state, reset_framecount,
                     set_game_state)
from mainmenu import mainMenu
from miniboss import miniboss
from particles import particle_list
from pickups import pickup_list
from player import player
from scoremanager import scoreManager
from stars import generate_stars, star_list
from upgrademenu import upgradeMenu


class Main:
    def __init__(self):
        self.state = get_game_state()
        generate_stars()

        pyxel.init(GAME_WIDTH, GAME_HEIGHT, title = TITLE, fps = FPS)
        pyxel.load("game.pyxres")
        pyxel.run(self.update, self.draw)

    def update(self):
        self.state = get_game_state()
        
        if not get_paused_state():
            for star in star_list:
                star.update()

        if self.state == "MENU":    
            mainMenu.update()
        elif self.state == "GAME":
            gameManager.update()
        elif self.state == "GAMEOVER":
            gameOverMenu.update()
        elif self.state == "UPGRADEMENU":
            upgradeMenu.update()
        elif self.state == "SCOREMENU":
            scoreManager.update()
        else: reset_game()

    def draw(self):
        pyxel.cls(0)

        for star in star_list:
            star.draw()

        if self.state == "MENU":
            mainMenu.draw()
        elif self.state == "GAME":
            gameManager.draw()
        elif self.state == "GAMEOVER":
            gameOverMenu.draw()
        elif self.state == "UPGRADEMENU":
            upgradeMenu.draw()
        elif self.state == "SCOREMENU":
            scoreManager.draw()

def reset_game():
    reset_framecount()
    set_game_state("MENU")
    
    asteroid_list.clear()
    asteroid_list.clear()
    bullet_list.clear()
    pickup_list.clear()
    particle_list.clear()

    player.reset()
    miniboss.reset()
    gameManager.reset()
    scoreManager.reset()
    
if __name__ == "__main__":
    game = Main()