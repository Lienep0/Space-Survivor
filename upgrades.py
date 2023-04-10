upgrade_list = []

class Upgrade:
    def __init__(self, name, description, xcoord, ycoord, is_unique):
        self.name = name
        self.description = description
        self.coords = [xcoord, ycoord]
        self.is_unique = is_unique

upgrade_list.append(Upgrade("Damage", ["Boosts your damage", "by 20%"], 64, 0, False))
upgrade_list.append(Upgrade("Fire Rate", ["Boosts your fire", "rate by 20%"], 80, 0, False))
upgrade_list.append(Upgrade("Magnet", ["Boosts your magnet", "range by 50%"], 64, 16, False))
upgrade_list.append(Upgrade("Dash", ["Adds the ability to", "Dash by holding", "Shift. (+50% speed)"], 80, 16, True))