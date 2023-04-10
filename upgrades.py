upgrade_list = []

class Upgrade:
    def __init__(self, name, description1, description2, xcoord, ycoord):
        self.name = name
        self.description = [description1, description2]
        self.coords = [xcoord, ycoord]

upgrade_list.append(Upgrade("Damage", "Boosts your damage", "by 50%", 64, 0))
upgrade_list.append(Upgrade("Fire Rate", "Boosts your fire", "rate by 50%", 80, 0))
upgrade_list.append(Upgrade("Magnet", "Boosts your magnet", "range by 50%", 64, 16))