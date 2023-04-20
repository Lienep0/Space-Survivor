import json

class data:
    def __init__(self):
        self.data = json.load(open("Test-Json.json", "r"))

    def update(self):
        
