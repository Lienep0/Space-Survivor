import pyxel

pickup_list = []

class Pickup:   #collectible pour augmenter le score
    def __init__(self,x,y):
        self.x = x
        self.y = y

    def update(self):
        self.y += 1
        # if abs(self.x - (player.x + 8)) < 4 and abs(self.y - (player.y + 8)) < 4:
        #    pickup_list.remove(self)
        #    score += 50
        
        #On va la faire dans player la collision

    def draw(self):
        pyxel.circb(self.x, self.y, 2, 10)