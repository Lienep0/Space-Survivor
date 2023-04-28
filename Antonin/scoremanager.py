import json
import pyxel

class scoreManager:
    def __init__(self):
        self.data = json.load(open("scores.json", "r"))
        self.dic_data = {}
        for x in self.data.values():
            self.dic_data[str(x["name"])] = (int(x["score"]))


    def update(self):
        i = 1
        self.data = {}
        for x,y in self.dic_data.items() :
            z = "player"
            z += " " + str(i)
            self.data[z]={"name" : x, "score" : str(y)}
            i += 1

        with open("scores.json", "w") as write_file:
            json.dump(self.data, write_file)
    
    def draw(self):
        i = 0
        for x in self.dic_data.keys():
            pyxel.text(30, 65 + i, x , 7)
            pyxel.text(50, 65 + i, str(self.dic_data[x]) , 7)
            i += 10

    def reset(self):
        self.data = json.load(open("scores.json", "r"))
        self.dic_data = {}
        for x in self.data.values():
            self.dic_data[str(x["name"])] = (int(x["score"]))


Scores = scoreManager()