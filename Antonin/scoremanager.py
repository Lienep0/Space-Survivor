import json
import pyxel
from player import player
from constants import ALPHABET

class scoreManager:
    def __init__(self):
        self.data = json.load(open("Antonin/scores.json", "r"))
        self.dic_data = {}
        self.leter_amstr = [0,0,0]

        for value in self.data.values():
            self.dic_data[str(value["name"])] = value["score"]

    def update(self):
        size = 0
        name_player = scoreManager.input_name()
        self.dic_data[name_player] = player.level
        dict(sorted(self.dic_data.items(), key=lambda item: int(item[1]), reverse=True))
        for name in self.dic_data.keys():
            size += 1
            if size > 3:
                self.dic_data.pop(name)
        
        score_str = ""
        size = 0
        for name, score in self.dic_data.items() :
            for _ in str(score):
                size += 1
            if size > 6:
                score_str = "Win The Game"
            else:
                size = 6 - size
                for i in range(size):
                    score_str += "0"
                score_str += str(score)

        i = 1
        for name, score in self.dic_data.items() : 
            z = "player" # Pareil.
            z += " " + str(i)
            self.data[z] = {"name" : name, "score" : score}
            i += 1

        json.dump(self.data, open("Antonin/scores.json", "w"))
        self.__init__()
    
    def draw(self):
        offset = 0
        for name in self.dic_data.keys(): 
            pyxel.rect(30, 65 + offset , 12 , 8 , 0)
            pyxel.rect(50, 65 + offset , 24 , 8 , 0)
            pyxel.text(30, 65 + offset, name , 7)
            pyxel.text(50, 65 + offset, str(self.dic_data[name]) , 7)
            offset += 10

    def reset(self):
        self.data = {"player 1": {"name": "XXX", "score": "000000"},
                     "player 2": {"name": "XXX", "score": "000000"},
                     "player 3": {"name": "XXX", "score": "000000"}}
        
        json.dump(self.data, open("Antonin/scores.json", "w"))
        self.__init__()

    def input_name(self):
        name_player = ""
        for i in range(self.leter_amstr):
            pyxel.blt(i * 12 + 36, 70, 1, 0, 40, 8, 8, 0)
            pyxel.blt(i * 12 + 36, 85, 1, 0, 48, 8, 8, 0)
            exit = False
            while not exit:
                if pyxel.btn(pyxel.KEY_DOWN):
                    self.leter_amstr[i] = (self.leter_amstr[i]-1)%26
                elif pyxel.btn(pyxel.KEY_UP):
                    self.leter_amstr[i] = (self.leter_amstr[i]+1)%26
                elif pyxel.btn(pyxel.KEY_SPACE):
                    name_player += ALPHABET[self.leter_amstr[i]]
                    exit = True
        return name_player
    
    def draw_input_name(self):
        for i in range(self.leter_amstr):
            pyxel.blt(i * 12 + 36, 78, 1, self.leter_amstr[i] * 8, 32, 8, 8, 0)

scores = scoreManager()