import json
import pyxel

class scoreManager:
    def __init__(self):
        self.data = json.load(open("scores.json", "r"))
        self.dic_data = {}
        for value in self.data.values():
            self.dic_data[str(value["name"])] = (int(value["score"]))


    def update(self):
        i = 1
        self.data = {}
        for key,value in self.dic_data.items() :
            z = "player"
            z += " " + str(i)
            self.data[z]={"name" : key, "score" : str(value)}
            i += 1

        with open("scores.json", "w") as write_file:
            json.dump(self.data, write_file)
    
    def draw(self):
        i = 0
        for key in self.dic_data.keys():
            pyxel.text(30, 65 + i, key , 7)
            pyxel.text(50, 65 + i, str(self.dic_data[key]) , 7)
            i += 10

    def reset(self):
        self.data = {"player 1": {"name": "XXX", "score": "0000000"},
                "player 2": {"name": "XXX", "score": "0000000"},
                "player 3": {"name": "XXX", "score": "0000000"}}
        self.dic_data = {}
        for value in self.data.values():
            self.dic_data[str(value["name"])] = (int(value["score"]))
        self.update()


Scores = scoreManager()