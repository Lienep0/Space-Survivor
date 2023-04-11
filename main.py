import pyxel
from random import randint, randrange

from constants import *
from player import player
from miniboss import *
from asteroids import *
from bullets import bullet_list
from pickups import pickup_list
from particles import particle_list, PlayerExplosion
from stars import generate_stars, star_list
from ui import ui
from upgrades import upgrade_list

class Main:
    def __init__(self):
        self.state = "MENU"
        self.asteroid_toggle = True
        self.timeofdeath = -100
        self.miniboss = None
        self.paused = False
        self.hasgeneratedupgrades = False
        self.upgradescursorposition = 0

        generate_stars()

        pyxel.init(GAME_WIDTH, GAME_HEIGHT, title=TITLE, fps=FPS)
        pyxel.load("game.pyxres")
        pyxel.run(self.update, self.draw)

    def check_player_upgrade(self,player):
        if player.level <= MAX_LEVEL and player.xp >= XP_REQUIREMENTS[player.level]:
            player.xp = 0
            player.level += 1
            self.state = "UPGRADE_MENU"

    def check_for_death(self):
        if player.hp <= 0 and self.timeofdeath < 0:
            particle_list.append(PlayerExplosion(player.x + 3, player.y + 3))
            pyxel.play(0, PLAYER_DEATH_SOUND)
            player.active = False
            self.timeofdeath = framecount
        
        if self.timeofdeath + PLAYER_DEATHFREEZE_DURATION == framecount :
            reset_game(self)

    def spawn_asteroids(self):
        global framecount
        framecount += 1

        if self.asteroid_toggle:
            if framecount % ASTEROID_COOLDOWN == 0: #Génère un astéroide toutes les "ASTEROID_COOLDOWN" frames
                asteroid_list.append(Asteroid(randint(
                    ASTEROID_OFFSET_FROM_BORDERS, GAME_WIDTH - ASTEROIDS["SMALL_ASTEROID"]["size"]- ASTEROID_OFFSET_FROM_BORDERS), ASTEROIDS["SMALL_ASTEROID"]["type"]))

    def update(self):
        # ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
        # DEV SHORTCUTS
        # ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
        if pyxel.btnp(pyxel.KEY_R):
            reset_game(self)
        if pyxel.btnp(pyxel.KEY_A):
            self.asteroid_toggle = not self.asteroid_toggle
        if pyxel.btnp(pyxel.KEY_M):
            self.miniboss = Miniboss()
        if pyxel.btnp(pyxel.KEY_X):
            player.xp += 10
        if pyxel.btnp(pyxel.KEY_1): 
            asteroid_list.append(Asteroid(randint(
                ASTEROID_OFFSET_FROM_BORDERS, GAME_WIDTH - ASTEROIDS["SMALL_ASTEROID"]["size"] - ASTEROID_OFFSET_FROM_BORDERS),ASTEROIDS["SMALL_ASTEROID"]["type"]))
        if pyxel.btnp(pyxel.KEY_2): 
            asteroid_list.append(Asteroid(randint(
                ASTEROID_OFFSET_FROM_BORDERS, GAME_WIDTH - ASTEROIDS["MEDIUM_ASTEROID"]["size"] - ASTEROID_OFFSET_FROM_BORDERS), ASTEROIDS["MEDIUM_ASTEROID"]["type"]))
        if pyxel.btnp(pyxel.KEY_3): 
            asteroid_list.append(Asteroid(randint(
                ASTEROID_OFFSET_FROM_BORDERS, GAME_WIDTH - ASTEROIDS["LARGE_ASTEROID"]["size"] - ASTEROID_OFFSET_FROM_BORDERS), ASTEROIDS["LARGE_ASTEROID"]["type"]))
        # ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
        # DEV SHORTCUTS
        # ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

        if pyxel.btnp(pyxel.KEY_P):
            self.paused = not self.paused
        if not self.paused:
            for star in star_list:
                star.update()
        if self.state == "MENU":    
            if pyxel.btnp(pyxel.KEY_SPACE):
                self.state = "GAME"
        elif self.state == "GAME_OVER":
            if pyxel.btnp(pyxel.KEY_SPACE):
                self.state = "MENU"
        elif self.state == "UPGRADE_MENU":
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
                self.state = "GAME"
        elif not self.paused:
            self.spawn_asteroids()
            self.check_player_upgrade(player)

            player.update()
            for element in asteroid_list + particle_list + bullet_list + pickup_list: #Evil python hack
                element.update()
            if self.miniboss is not None: self.miniboss.update()

        self.check_for_death()

    def draw(self):
        pyxel.cls(0)
        for star in star_list:
            star.draw()
        if self.state == "MENU":
            self.draw_menu()
        elif self.state == "GAME_OVER":
            self.draw_game_over()
        elif self.state == "UPGRADE_MENU":
            self.draw_upgrade_menu()
        else: 
            for star in star_list:
                star.draw()
            if player.active:
                for element in asteroid_list + bullet_list + pickup_list:
                    element.draw()
                player.draw()
            if self.miniboss is not None: self.miniboss.draw()
            for particle in particle_list:
                particle.draw()
            ui.draw()
            if self.paused: pyxel.blt(28, 30, 0, 0, 112, 48, 8, 0) # PAUSED

    def draw_menu(self):
        pyxel.blt(32, 34, 0, 8, 64, 40, 8, 0) #SPACE
        pyxel.blt(23, 42, 0, 0, 72, 64, 8, 0) #SURVIVOR
        pyxel.text(27, 58, "High scores :", 7)
        pyxel.text(30, 70, "XXX  000000", 7)
        pyxel.text(30, 80, "XXX  000000", 7)
        pyxel.text(30, 90, "XXX  000000", 7)
        pyxel.text(10, 110, "Press SPACE to Start !", 7)
        pyxel.text(2, 2, "1/2/3 to spawn asteroid", 7)
        pyxel.text(2, 10, "A to spawn On/Off", 7)
        pyxel.text(2, 18, "R to Reset, M for miniboss", 7)
        pyxel.blt(PLAYER_STARTING_X, PLAYER_STARTING_Y, 0, 0, 8, 8, 8, 0) #PLAYER
        if self.asteroid_toggle:
            pyxel.circ(75, 12, 3, 11)
        else:
            pyxel.circ(75, 12, 3, 8)
    
    def draw_game_over(self):
        pyxel.blt(20, 20, 1, 0, 0, 64, 16) #GAME
        pyxel.blt(20, 36, 1, 0, 16, 64, 16) #OVER
        pyxel.text(24, 100, "Press SPACE to", 7)
        pyxel.text(22, 110, "go back to MENU", 7)

    def draw_upgrade_menu(self):
        if not self.hasgeneratedupgrades:
            global current_upgrade_list
            current_upgrade_list = []
            upgrade_list_buffer = list(upgrade_list)

            current_upgrade_list.append(upgrade_list_buffer.pop(randrange(0,len (upgrade_list_buffer))))
            current_upgrade_list.append(upgrade_list_buffer.pop(randrange(0,len (upgrade_list_buffer))))
            current_upgrade_list.append(upgrade_list_buffer.pop(randrange(0,len (upgrade_list_buffer))))

            self.hasgeneratedupgrades = True

        pyxel.blt(25, 50, 0, current_upgrade_list[0].coords[0], current_upgrade_list[0].coords[1], 16, 16, 0) # UPGRADE 1
        pyxel.blt(45, 50, 0, current_upgrade_list[1].coords[0], current_upgrade_list[1].coords[1], 16, 16, 0) # UPGRADE 2
        pyxel.blt(65, 50, 0, current_upgrade_list[2].coords[0], current_upgrade_list[2].coords[1], 16, 16, 0) # UPGRADE 3
        
        pyxel.text(13, 30, "Select your upgrade :", 7)
        for i in range(len(current_upgrade_list[self.upgradescursorposition + 1].description)):
            pyxel.text(15, 75 + 10 * i, current_upgrade_list[self.upgradescursorposition + 1].description[i], 7) # DESCRIPTION LINES
        pyxel.rectb(43 + 20 * self.upgradescursorposition, 48, 20, 20, 7) #CURSOR

def reset_game(game):
    global framecount
    framecount = 0
    game.state = "GAME_OVER"
    game.timeofdeath = -100
    game.miniboss = None
    game.paused = False
    game.hasgeneratedupgrades = False
    
    star_list.clear()
    asteroid_list.clear()
    asteroid_list.clear()
    bullet_list.clear()
    pickup_list.clear()
    particle_list.clear()
    
    player.x = PLAYER_STARTING_X
    player.y = PLAYER_STARTING_Y
    player.hp = PLAYER_HP
    player.level = 0
    player.xp = 0
    player.iFramesCooldown = 0
    player.visible = True
    player.active = True
    player.inventory = []
    player.isDashing = False

    generate_stars()

game = Main()