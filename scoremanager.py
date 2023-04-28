import json
import pyxel

class scoreManager:
    def __init__(self):
        self.data = json.load(open("scores.json", "r"))
        self.dic_data = {}
        for value in self.data.values():
            self.dic_data[str(value["name"])] = (value["score"])


    def update(self):
        i = 1
        for key,value in self.dic_data.items() :
            z = "player"
            z += " " + str(i)
            self.update({z , {"name" : key, "score" : value}})
            i += 1

        with open("scores.json", "w") as write_file:
            json.dump(self.data, write_file)
    
    def draw(self):
        i = 0
        for key in self.dic_data.keys():
            pyxel.rect(30, 65 + i , 12 , 8 , 0)
            pyxel.rect(50, 65 + i , 24 , 8 , 0)
            pyxel.text(30, 65 + i, key , 7)
            pyxel.text(50, 65 + i, str(self.dic_data[key]) , 7)
            i += 10

    def reset(self):
        self.data = {"player 1": {"name": "XXX", "score": "000000"},
                     "player 2": {"name": "XXX", "score": "000000"},
                     "player 3": {"name": "XXX", "score": "000000"}}
        with open("scores.json", "w") as write_file:
            json.dump(self.data, write_file)


Scores = scoreManager()