import json
import pyxel

class scoreManager:
    def __init__(self):
        self.data = json.load(open("scores.json", "r"))
        self.dic_data = {}

        for value in self.data.values():
            self.dic_data[str(value["name"])] = value["score"]


    def update(self):
        i = 1
        for key, value in self.dic_data.items() : # Pourquoi t'appelle ça key, value ?? Appelle ça name, score plutôt.
            z = "player" # Pareil.
            z += " " + str(i)
            self.update({z , {"name" : key, "score" : value}})
            i += 1

        json.dump(self.data, open("scores.json", "w"))
    
    def draw(self):
        i = 0 # Pareil. [i] tu peux l'appeler [offset] par exemple
        for key in self.dic_data.keys(): # Pareil ici je sais pas ce que c'est censé représenter mais donne un vrai nom stp.
            pyxel.rect(30, 65 + i , 12 , 8 , 0)
            pyxel.rect(50, 65 + i , 24 , 8 , 0)
            pyxel.text(30, 65 + i, key , 7)
            pyxel.text(50, 65 + i, str(self.dic_data[key]) , 7)
            i += 10

    def reset(self):
        self.data = {"player 1": {"name": "XXX", "score": "000000"},
                     "player 2": {"name": "XXX", "score": "000000"},
                     "player 3": {"name": "XXX", "score": "000000"}}
        
        json.dump(self.data, open("scores.json", "w"))


scores = scoreManager()