import json
import pyxel
from player import player

class scoreManager:
    def __init__(self):
        self.data = json.load(open("Antonin/scores.json", "r"))
        self.dic_data = {}

        for value in self.data.values():
            self.dic_data[str(value["name"])] = value["score"]


    def update(self):
        i = 1
        for name, score in self.dic_data.items() : 
            z = "player" # Pareil.
            z += " " + str(i)
            self.update({z , {"name" : name, "score" : score}})
            i += 1

        json.dump(self.data, open("Antonin/scores.json", "w"))
    
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


scores = scoreManager()