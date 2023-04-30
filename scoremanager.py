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
        self.data = json.load(open("scores.json", "r"))
        self.dic_data = {}
        self.leter_amstr = [0,0,0]
        self.ileter_amstr = 0
        self.name_player = ""

        for value in self.data.values():
            self.dic_data[str(value["name"])] = value["score"]

    def update(self):
        if pyxel.btnp(pyxel.KEY_DOWN):
            self.leter_amstr[self.ileter_amstr] = (self.leter_amstr[self.ileter_amstr]+1)%26
        elif pyxel.btnp(pyxel.KEY_UP):
            self.leter_amstr[self.ileter_amstr] = (self.leter_amstr[self.ileter_amstr]-1)%26
        elif pyxel.btnp(pyxel.KEY_SPACE):
            self.name_player += string.ascii_uppercase[self.leter_amstr[self.ileter_amstr]]
            self.ileter_amstr += 1
        if self.ileter_amstr == 3:
            self.ileter_amstr = 0
            self.update_json()
            self.reset_game()

        
    def draw(self):
        for i in range(len(self.leter_amstr)):
            pyxel.blt(36 + i * 12, 78, 1, self.leter_amstr[i] * 8, 32, 8, 8, 0)
        pyxel.blt(36 + self.ileter_amstr * 12, 70, 1, 0, 40, 8, 8, 0)
        pyxel.blt(36 + self.ileter_amstr * 12, 85, 1, 0, 48, 8, 8, 0)
        pyxel.text(20, 20,"Enter your name", 7)
        pyxel.text(20, 36, "Your score:", 7) 
        pyxel.text(64, 36, str(player.level) , 7) 


    def update_json(self):
        size = 0
        name_player = self.name_player
        self.name_player=""
        self.dic_data[name_player] = player.level
        dict(sorted(self.dic_data.items(), key=lambda item: int(item[1]), reverse=True))
        for name in self.dic_data.keys():
            size += 1
        While size < 4:
            self.dic_data.pop(name)
            size -= 1
        
        score_str = ""
        for name, score in self.dic_data.items() :
            size = 0
            for i in str(score):
                size += 1
            if size > 6:
                score_str = "Win The Game"
            else:
                size = 6 - size
                score_str += "0" * size
                score_str += str(score)
            self.dic_data[name] = score_str
            score_str = ""

        i = 1
        for name, score in self.dic_data.items() : 
            z = "player" # variable servant a mêtre dans le .json player 1, 2, ...
            z += " " + str(i)
            self.data[z] = {"name" : name, "score" : score}
            i += 1

        json.dump(self.data, open("scores.json", "w"))
        self.__init__()
    
    def draw_menu(self):
        offset = 0
        for name in self.dic_data.keys(): 
            pyxel.rect(30, 65 + offset , 12 , 8 , 0) # rectangle noir pour cacher ce qu'il y'a de base car il faut sur l'écrant start si il n'y a pas de high scor il faut quand même afficher des 0
            pyxel.rect(50, 65 + offset , 24 , 8 , 0)
            pyxel.text(30, 65 + offset, name , 7)
            pyxel.text(50, 65 + offset, str(self.dic_data[name]) , 7)
            offset += 10

    def reset(self):
        self.data = {"player 1": {"name": "XXX", "score": "000000"},
                     "player 2": {"name": "XXX", "score": "000000"},
                     "player 3": {"name": "XXX", "score": "000000"}}
        
        json.dump(self.data, open("scores.json", "w"))
        self.__init__()

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