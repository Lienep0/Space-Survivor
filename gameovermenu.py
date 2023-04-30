import pyxel

from globals import set_game_state
from player import player
from constants import GAME_HEIGHT

class GameOverMenu:
    def update(self):
        if pyxel.btnp(pyxel.KEY_SPACE):
            set_game_state("SCOREMENU")

    def draw(self):
        pyxel.blt(20, 20, 1, 0, 0, 64, 16) #GAME
        pyxel.blt(20, 36, 1, 0, 16, 64, 16) #OVER

        pyxel.text(10, 70, f"LEVEL: {player.level}", 7)
        pyxel.text(10, 80, f"SCORE: {player.score}", 7)
        pyxel.text(10, 90, f"PICKUPS COLLECTED: {player.pickups_collected}", 7)
        pyxel.text(10, 100, f"ASTEROIDS DESTROYED: {player.asteroids_destroyed}", 7)
        pyxel.text(10, 110, f"MINIBOSSES DEFEATED: {player.minibosses_destroyed}", 7)
        pyxel.text(8, GAME_HEIGHT - 14, "PRESS SPACE TO CONTINUE", 7)

gameOverMenu = GameOverMenu()