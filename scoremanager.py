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

    def reset(self):
        self.data = json.load(open("scores.json", "r"))
        self.high_scores = []
        self.letter_ids = [0,0,0]
        self.cursor_position = 0
        self.player_name = ""

        for value in self.data[1].values():
            self.high_scores.append((str(value["name"]), value["score"]))
        self.high_scores = self.high_scores[:3]

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

    def draw(self):
        for i in range(len(self.letter_ids)):
            pyxel.blt(36 + i * 12, 78, 1, self.letter_ids[i] * 8, 32, 8, 8, 0) # Lettres

        pyxel.blt(36 + self.cursor_position * 12, 70, 1, 0, 40, 8, 8, 0) # Flèche haut
        pyxel.blt(36 + self.cursor_position * 12, 85, 1, 0, 48, 8, 8, 0) # Flèche bas

        pyxel.text(20, 20,"Enter your name", 7)
        pyxel.text(20, 36, "Your score:", 7) 
        pyxel.text(64, 36, self.current_score, 7) 

    def update_json(self):
        if len(self.current_score) > 6:
            self.current_score = "0" * (6 - len(self.current_score)) + self.current_score

        self.high_scores.append((self.player_name, self.current_score))
        self.high_scores = sorted(self.high_scores, key=lambda x: int(x[1]), reverse=True)

        player_name = "player" 
        player_name += " " + str(len(self.data[0]))
        self.data[0][player_name] = {"name" : self.player_name, "score" : self.current_score}
        
        while len(self.high_scores) > 3:
            self.high_scores.pop()

        i = 1
        for player_in_list in self.high_scores : 
            player_name = "player"
            player_name += " " + str(i)
            self.data[1][player_name] = {"name" : player_in_list[0], "score" : player_in_list[1]}
            i += 1

        json.dump(self.data, open("scores.json", "w"))
        self.reset()
    
    def draw_menu(self):
        offset = 0
        for player_in_list in self.high_scores: 
            pyxel.rect(30, 65 + offset, 12, 8, 0) # rectangle noir pour cacher ce qu'il y'a de base car il faut sur l'écrant start si il n'y a pas de high scor il faut quand même afficher des 0
            pyxel.rect(50, 65 + offset, 24, 8, 0)
            pyxel.text(30, 65 + offset, player_in_list[0], 7)
            pyxel.text(50, 65 + offset, player_in_list[1], 7)
            offset += 10

    def reset_data(self):
        self.data = [{}, {"player 1": {"name": "XXX", "score": "000000"}, "player 2": {"name": "XXX", "score": "000000"}, "player 3": {"name": "XXX", "score": "000000"}}]
        
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

scoreManager = ScoreManager()