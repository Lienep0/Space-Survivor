import pyxel
from random import randint

from constants import *
from player import player
from asteroids import *
from bullets import bullet_list
from pickups import pickup_list
from particles import particle_list, PlayerExplosion
from stars import generate_stars, star_list
from ui import *

class Main:
    def __init__(self):
        self.state = "MAIN_MENU"
        self.asteroid_toggle = True
        self.timeofdeath = -100

        generate_stars()

        pyxel.init(GAME_WIDTH, GAME_HEIGHT, title=TITLE, fps=FPS)
        pyxel.load("game.pyxres")
        pyxel.run(self.update, self.draw)

    def update(self):
        if pyxel.btnp(pyxel.KEY_R):
            reset_game(self)
        if pyxel.btnp(pyxel.KEY_A):
            self.asteroid_toggle = not self.asteroid_toggle
        for star in star_list:
            star.update()        
        if self.state == "MAIN_MENU":    
            if pyxel.btnp(pyxel.KEY_SPACE):
                self.state = "GAME"
        elif self.state == "GAME_OVER":
            if pyxel.btnp(pyxel.KEY_SPACE):
                self.state = "MAIN_MENU"
        else:
            global framecount
            framecount += 1

            if self.asteroid_toggle:
                if framecount % ASTEROID_COOLDOWN == 0: #Génère un astéroide toutes les "ASTEROID_COOLDOWN" frames
                    asteroid_list.append(Asteroid(randint(0, GAME_WIDTH - ASTEROIDS["MEDIUM_ASTEROID"]["size"]), ASTEROIDS["MEDIUM_ASTEROID"]["type"]))

            if pyxel.btnp(pyxel.KEY_1):asteroid_list.append(Asteroid(randint(ASTEROID_OFFSET_FROM_BORDERS, GAME_WIDTH - ASTEROIDS["SMALL_ASTEROID"]["size"] - ASTEROID_OFFSET_FROM_BORDERS), ASTEROIDS["SMALL_ASTEROID"]["type"]))
            if pyxel.btnp(pyxel.KEY_2):asteroid_list.append(Asteroid(randint(ASTEROID_OFFSET_FROM_BORDERS, GAME_WIDTH - ASTEROIDS["MEDIUM_ASTEROID"]["size"] - ASTEROID_OFFSET_FROM_BORDERS), ASTEROIDS["MEDIUM_ASTEROID"]["type"]))
            if pyxel.btnp(pyxel.KEY_3):asteroid_list.append(Asteroid(randint(ASTEROID_OFFSET_FROM_BORDERS, GAME_WIDTH - ASTEROIDS["LARGE_ASTEROID"]["size"] - ASTEROID_OFFSET_FROM_BORDERS), ASTEROIDS["LARGE_ASTEROID"]["type"]))

            player.update()
            for element in asteroid_list + particle_list + bullet_list + pickup_list: #Evil python hack
                element.update()
            ui.update()

            if player.hp <= 0:
                particle_list.append(PlayerExplosion(player.x + 3, player.y + 3))
                pyxel.play(CHANNEL_1,PLAYER_DEATH_SOUND)
                player.active = False
                player.hp = PLAYER_HP
                self.timeofdeath = framecount
            
            if self.timeofdeath + PLAYER_DEATHFREEZE_DURATION == framecount :
                reset_game(self)


    def draw(self):
        pyxel.cls(0)
        for star in star_list:
            star.draw()
        if self.state == "MAIN_MENU":
            pyxel.blt(32, 24, 0, 8, 64, 40, 8, 0) #SPACE
            pyxel.blt(23, 32, 0, 0, 72, 64, 8, 0) #SURVIVOR
            pyxel.text(27, 48, "High scores :", 7)
            pyxel.text(30, 60, "XXX  000000", 7)
            pyxel.text(30, 70, "XXX  000000", 7)
            pyxel.text(30, 80, "XXX  000000", 7)
            pyxel.text(10, 100, "Press SPACE to Start !", 7)
            pyxel.text(2, 2, "1/2/3 to spawn asteroid", 7)
            pyxel.text(2, 10, "A to spawn On/Off", 7)
            pyxel.text(2, 18, "R to Reset", 7)
            pyxel.blt(PLAYER_STARTING_X, PLAYER_STARTING_Y, 0, 0, 8, 8, 8, 0) #PLAYER
            if self.asteroid_toggle:
                pyxel.circ(75, 12, 3, 11)
            else:
                pyxel.circ(75, 12, 3, 8)
        elif self.state == "GAME_OVER":
            pyxel.blt(20, 20, 1, 0, 0, 64, 16) #GAME
            pyxel.blt(20, 36, 1, 0, 16, 64, 16) #OVER
            pyxel.text(24, 90, "Press SPACE to", 7)
            pyxel.text(22, 100, "go back to MENU", 7)
        else: 
            pyxel.cls(0)
            for star in star_list:
                star.draw()
            if player.active:
                for element in asteroid_list + bullet_list + pickup_list:
                    element.draw()
                player.draw()
            for particle in particle_list:
                particle.draw()
            ui.draw()

def reset_game(game):

    global framecount
    framecount = 0
    game.state = "GAME_OVER"
    game.timeofdeath = -100

    star_list.clear()
    asteroid_list.clear()
    asteroid_list.clear()
    bullet_list.clear()
    pickup_list.clear()
    particle_list.clear()
    
    player.x = PLAYER_STARTING_X
    player.y = PLAYER_STARTING_Y
    player.hp = PLAYER_HP
    player.xp = 0
    player.iFramesCooldown = 0
    player.visible = True
    player.active = True

    generate_stars()

game = Main()