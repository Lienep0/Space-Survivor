import json
import pyxel
from player import player

class scoreManager:
    def __init__(self):
        self.data = json.load(open("Antonin/scores.json", "r"))
        self.dic_data = {}

        for value in self.data.values():
            self.dic_data[str(value["name"])] = int(value["score"])


    def update(self):
        size = 0
        self.dic_data[scoreManager.input_name()] = player.level
        dict(sorted(self.dic_data.items(), key=lambda item: item[1], reverse=True))
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
            z = "player" # Je sais toujours pas ce que cette variable fait
            z += " " + str(i)
            self.data[z] = {"name" : name, "score" : score}
            i += 1

        json.dump(self.data, open("Antonin/scores.json", "w"))
    
    def draw(self):
        offset = 0
        for name in self.dic_data.keys(): 
            pyxel.rect(30, 65 + offset , 12 , 8 , 0) # Quand tu dessines des trucs avec pyxel hésite pas à mettre en commentaire ce que tu dessines, c'est mieux pour s'y retrouver
            pyxel.rect(50, 65 + offset , 24 , 8 , 0)
            pyxel.text(30, 65 + offset, name , 7)
            pyxel.text(50, 65 + offset, str(self.dic_data[name]) , 7)
            offset += 10

    def reset(self):
        self.data = {"player 1": {"name": "XXX", "score": "000000"},
                     "player 2": {"name": "XXX", "score": "000000"},
                     "player 3": {"name": "XXX", "score": "000000"}}
        
        json.dump(self.data, open("Antonin/scores.json", "w"))

    def input_name(self):
        pass

scores = scoreManager()