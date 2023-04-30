import pyxel

from globals import set_game_state

class GameOverMenu:
    def __init__(self):
        self.timer = 0

    def update(self):
        self.timer += 1
        if self.timer >= 60:
            set_game_state("SCOREMENU")


    def draw(self):
        pyxel.blt(20, 20, 1, 0, 0, 64, 16) #GAME
        pyxel.blt(20, 36, 1, 0, 16, 64, 16) #OVER
        pyxel.text(24, 100, "Wait for enter your", 7)
        pyxel.text(22, 110, "name in classment", 7)

gameOverMenu = GameOverMenu()