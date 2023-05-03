import json

import pyxel

from constants import DOWN_KEY, LEFT_KEY, RIGHT_KEY, SHOOT_KEY, UP_KEY
from globals import set_game_state


class ScoreManager:
    def __init__(self):
        self.data = json.load(open("scores.json", "r"))
        self.reset()

    def update(self):
        if pyxel.btnp(SHOOT_KEY) and self.cursor_position == 2:
            player_name = ''.join([chr(65 + id) for id in self.letter_ids]) # Unicode uppercase letters start at 65
            self.update_json(player_name)

            set_game_state("RESET")

        elif pyxel.btnp(DOWN_KEY):
            self.letter_ids[self.cursor_position] = (self.letter_ids[self.cursor_position] + 1) % 26
        elif pyxel.btnp(UP_KEY):
            self.letter_ids[self.cursor_position] = (self.letter_ids[self.cursor_position] - 1) % 26

        elif pyxel.btnp(LEFT_KEY) and self.cursor_position >= 1:
            self.cursor_position -= 1
        elif (pyxel.btnp(RIGHT_KEY) or pyxel.btnp(SHOOT_KEY)) and self.cursor_position <= 1:
            self.cursor_position += 1

    def update_json(self, player_name):
        if len(self.player_score) < 6:
            self.player_score = "0" * (6 - len(self.player_score)) + self.player_score # Lenghten score if necessary

        self.data.append((player_name, self.player_score))

        self.data = sorted(self.data, key= lambda get_value: get_value[1], reverse=True) # Sort by score
        self.data.pop() # Remove the ejected score

        json.dump(self.data, open("scores.json", "w"))
    
    def draw_scores(self):
        for i in range(3): 
            pyxel.text(30, 65 + i * 10, f"{self.data[i][0]}  {self.data[i][1]}", 7) # Player Name + Score

    def draw(self):
        for i in range(len(self.letter_ids)):
            pyxel.blt(36 + i * 12, 78, 1, self.letter_ids[i] * 8, 32, 8, 8, 0) # Letters

        pyxel.blt(36 + self.cursor_position * 12, 70, 1, 0, 40, 8, 8, 0) # Up arrow
        pyxel.blt(36 + self.cursor_position * 12, 85, 1, 0, 48, 8, 8, 0) # Down arrow

        pyxel.text(20, 20,"Enter your name", 7)
        pyxel.text(20, 36, f"Your score: {self.player_score}", 7) 

    def reset_data(self):
        self.data = [["XXX", "000000"], ["XXX", "000000"], ["XXX", "000000"]]
        json.dump(self.data, open("scores.json", "w"))

    def reset(self):
        self.letter_ids = [0,0,0]
        self.cursor_position = 0

scoreManager = ScoreManager()