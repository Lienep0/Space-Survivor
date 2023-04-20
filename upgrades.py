from constants import (DAMAGE_UPGRADE_BOOST, DASH_UPGRADE_SPEED_BOOST,
                       EXPLODING_UPGRADE_CHANCE, FIRE_RATE_UPGRADE_BOOST,
                       MAGNET_UPGRADE_BOOST, MAXIMUM_HEALTH,
                       QUAD_SHOT_FIRE_RATE_PENALTY)

upgrade_list = []

class Upgrade:
    def __init__(self, name, description, xcoord, ycoord, is_unique, instant_effect, weight):
        self.name = name
        self.description = description
        self.coords = [xcoord, ycoord]
        self.is_unique = is_unique
        self.instant_effect = instant_effect
        self.weight = weight

# Normal Upgrades
upgrade_list.append(Upgrade("Damage", ["Boosts your damage", f"by {DAMAGE_UPGRADE_BOOST}"], 64, 0, False, False, 1))
upgrade_list.append(Upgrade("Fire Rate", ["Boosts your fire", f"rate by {FIRE_RATE_UPGRADE_BOOST}"], 80, 0, False, False, 1))
upgrade_list.append(Upgrade("Magnet", ["Boosts your magnet", f"range by {MAGNET_UPGRADE_BOOST}"], 64, 16, False, False, 1))
upgrade_list.append(Upgrade("Explosions", [f"+{int(EXPLODING_UPGRADE_CHANCE * 100)}% chance to", "Fire an explosive", "shot that deals", "Double damage !"], 112, 0, False, False, 1))

# Unique Upgrades
upgrade_list.append(Upgrade("Dash", ["Adds the ability to", "Dash by holding", f"Shift. (+{DASH_UPGRADE_SPEED_BOOST} speed)"], 80, 16, True, False, .5))
upgrade_list.append(Upgrade("Quad Shot", ["You fire Twice as", "Many bullets. Fire", "rate is reduced", f"by {-int((1 - QUAD_SHOT_FIRE_RATE_PENALTY) * 100)}%"], 112, 16, True, False, .2))

# Instant Upgrades
upgrade_list.append(Upgrade("Bomb", ["Gives you a bomb", "That can clear all", "asteroids. Activate", "by pressing B."], 96, 0, False, True, 2))
upgrade_list.append(Upgrade("Health", ["Heals you 1 HP", f"Maximum is {MAXIMUM_HEALTH}"], 96, 16, False, True, 1))