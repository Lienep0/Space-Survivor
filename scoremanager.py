import json
import string

import pyxel

from asteroids import asteroid_list
from bullets import bullet_list
from gamemanager import gameManager
from globals import reset_framecount, set_game_state
from miniboss import miniboss
from particles import particle_list
from pickups import pickup_list
from player import player


class ScoreManager:
    def __init__(self):
        self.reset()

    def update(self):
        if pyxel.btnp(pyxel.KEY_SPACE) and self.cursor_position == 2:
            for letter_id in self.letter_ids:
                self.player_name += string.ascii_uppercase[letter_id]

            self.update_json()
            self.reset_game()

        elif pyxel.btnp(pyxel.KEY_DOWN):
            self.letter_ids[self.cursor_position] = (self.letter_ids[self.cursor_position] + 1) % 26
        elif pyxel.btnp(pyxel.KEY_UP):
            self.letter_ids[self.cursor_position] = (self.letter_ids[self.cursor_position] - 1) % 26

        elif pyxel.btnp(pyxel.KEY_LEFT) and self.cursor_position >= 1:
            self.cursor_position -= 1
        elif (pyxel.btnp(pyxel.KEY_RIGHT) or pyxel.btnp(pyxel.KEY_SPACE)) and self.cursor_position <= 1:
            self.cursor_position += 1

    def update_json(self):
        if len(self.current_score) < 6:
            self.current_score = "0" * (6 - len(self.current_score)) + self.current_score

        self.data.append((self.player_name, self.current_score))

        self.data = sorted(self.data, key= lambda get_value: get_value[1], reverse=True) # Sort by score
        self.data.pop() # Remove the ejected score

        json.dump(self.data, open("scores.json", "w"))
        self.reset()
    
    def draw_scores(self):
        offset = 0
        for player in self.data: 
            pyxel.text(30, 65 + offset, player[0], 7)
            pyxel.text(50, 65 + offset, player[1], 7)
            offset += 10

    def draw(self):
        for i in range(len(self.letter_ids)):
            pyxel.blt(36 + i * 12, 78, 1, self.letter_ids[i] * 8, 32, 8, 8, 0) # Lettres

        pyxel.blt(36 + self.cursor_position * 12, 70, 1, 0, 40, 8, 8, 0) # Flèche haut
        pyxel.blt(36 + self.cursor_position * 12, 85, 1, 0, 48, 8, 8, 0) # Flèche bas

        pyxel.text(20, 20,"Enter your name", 7)
        pyxel.text(20, 36, "Your score:", 7) 
        pyxel.text(64, 36, self.current_score, 7) 

    def reset_data(self):
        self.data = [["XXX", "000000"], ["XXX", "000000"], ["XXX", "000000"]]
        
        json.dump(self.data, open("scores.json", "w"))
        self.reset()

    def reset_game(self):
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

    def reset(self):
        self.data = json.load(open("scores.json", "r"))
        self.letter_ids = [0,0,0]
        self.cursor_position = 0
        self.player_name = ""

scoreManager = ScoreManager()