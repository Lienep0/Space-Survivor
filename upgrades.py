from constants import (CRITICAL_UPGRADE_CHANCE,
                       CRITICAL_UPGRADE_DAMAGE_MULTIPLIER,
                       DAMAGE_UPGRADE_BOOST, DASH_UPGRADE_SPEED_BOOST,
                       FIRE_RATE_UPGRADE_BOOST, MAGNET_UPGRADE_BOOST,
                       MAXIMUM_HEALTH, PIERCING_UPGRADE_CHANCE,
                       QUAD_SHOT_FIRE_RATE_PENALTY)

upgrade_dic = {}

class Upgrade:
    def __init__(self, name, description, xcoord, ycoord, is_unique, has_instant_effect, weight):
        self.name = name
        self.description = description
        self.coords = [xcoord, ycoord]
        self.is_unique = is_unique
        self.has_instant_effect = has_instant_effect
        self.weight = weight

# Normal Upgrades
upgrade_dic["Damage"] = Upgrade("Damage", ["Boosts your damage", f"by {DAMAGE_UPGRADE_BOOST}"], 0, 0, False, False, 1)
upgrade_dic["Fire Rate"] = Upgrade("Fire Rate", ["Boosts your fire", f"rate by {FIRE_RATE_UPGRADE_BOOST}"], 16, 0, False, False, 1)
upgrade_dic["Magnet"] = Upgrade("Magnet", ["Boosts your magnet", f"range by {MAGNET_UPGRADE_BOOST}"], 0, 16, False, False, 1)

# Chance upgrades
upgrade_dic["Piercing"] = Upgrade("Piercing", [f"+{int(PIERCING_UPGRADE_CHANCE * 100)}% chance to", "Fire an piercing", "shot that goes", "through asteroids"], 64, 0, False, False, .7)
upgrade_dic["Crit"] = Upgrade("Crit", [f"+{int(CRITICAL_UPGRADE_CHANCE * 100)}% chance to", "Fire an critical", "shot that deals", f"x{CRITICAL_UPGRADE_DAMAGE_MULTIPLIER} damage !"], 80, 0, False, False, .7)

# Unique Upgrades
upgrade_dic["Explosions"] = Upgrade("Explosions", ["All your shots now", "explode in a small", "burst that hits", "nearby asteroids"], 48, 0, True, False, .2)
upgrade_dic["Dash"] = Upgrade("Dash", ["Adds the ability to", "Dash by holding", f"Shift. (+{DASH_UPGRADE_SPEED_BOOST} speed)"], 16, 16, True, False, .5)
upgrade_dic["Quad Shot"] = Upgrade("Quad Shot", ["You fire Twice as", "Many bullets. Fire", "rate is reduced", f"by {-int((1 - QUAD_SHOT_FIRE_RATE_PENALTY) * 100)}%"], 48, 16, True, False, .1)
upgrade_dic["Explosive Shield"] = Upgrade("Explosive Shield", ["If you get hit and", "you still have a", "bomb, use a bomb", "instead"], 64, 16, True, False, .5)
upgrade_dic["Big"] = Upgrade("Big", ["Increases your size", "but gives you", "double damage in", "return!"], 80, 16, True, False, 1000)

# Instant Upgrades
upgrade_dic["Bomb"] = Upgrade("Bomb", ["Refills your bombs.", "They can clear all", "asteroids. Activate", "by pressing B."], 32, 0, False, True, 0)
upgrade_dic["Health"] = Upgrade("Health", ["Heals you up to 2", f"HP. Maximum is {MAXIMUM_HEALTH}"], 32, 16, False, True, 0)