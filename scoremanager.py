import json

class scoreManager:
    def __init__(self):
        self.data = json.load(open("Test-Json.json", "r"))

    def update(self):
        pass