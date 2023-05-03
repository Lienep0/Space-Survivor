import pyxel

from globals import set_game_state
from player import player
from constants import GAME_HEIGHT
from scoremanager import scoreManager

class GameOverMenu:
    def update(self):
        if pyxel.btnp(pyxel.KEY_SPACE):
            scoreManager.player_score = str(player.score)
            set_game_state("SCOREMENU")

    def draw(self):
        pyxel.blt(20, 15, 1, 0, 0, 64, 16) #GAME
        pyxel.blt(20, 31, 1, 0, 16, 64, 16) #OVER

        pyxel.text(15, 70, f"LEVEL: {player.level}", 7)
        pyxel.text(15, 80, f"SCORE: {player.score}", 7)
        pyxel.text(15, 90, f"PICKUPS: {player.pickups_collected}", 7)
        pyxel.text(15, 100, f"ASTEROIDS: {player.asteroids_destroyed}", 7)
        pyxel.text(15, 110, f"MINIBOSSES: {player.minibosses_destroyed}", 7)
        pyxel.text(8, GAME_HEIGHT - 14, "PRESS SPACE TO CONTINUE", 7)

gameOverMenu = GameOverMenu()