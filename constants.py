#Main
GAME_WIDTH = 104
GAME_HEIGHT = 149
FPS = 30
TITLE = "Space Survivor"

PLAYER_STARTING_X = 48
PLAYER_STARTING_Y = 125
PLAYER_HP = 3
PLAYER_SPEED = 2
PLAYER_IFRAMES = 30 # The amount of frames the player has invincibility after getting hit
PLAYER_DEATHFREEZE_DURATION = 30 # The amount of time the screen freezes when the player dies

BULLET_DAMAGE = 2
BULLET_COOLDOWN = 10
MAGNET_RANGE = 5
EXPLODING_BULLET_RADIUS = 20

# Upgrade modifiers
DAMAGE_UPGRADE_BOOST = 0.5
FIRE_RATE_UPGRADE_BOOST = 1
MAGNET_UPGRADE_BOOST = 3
DASH_UPGRADE_SPEED_BOOST = 1
EXPLODING_UPGRADE_CHANCE = 0.15
QUAD_SHOT_FIRE_RATE_PENALTY = 1.7

ASTEROID_COOLDOWN = 10 # How many frames it takes for an asteroid to spawn
ASTEROID_OFFSET_FROM_BORDERS = 2 # How close an asteroid can spawn to the border of the screen, in pixels
ASTEROID_HITBOX_CORRECTION = 0 # How generous the asteroid hitbox is. The higher, the less generous. Default is 0

MINIBOSS_HEIGHT = 20
MINIBOSS_FIRE_COOLDOWN = 60 # Number of frames it takes for the miniboss to re-shoot after shooting 
CROSSHAIR_SPEED = 1.5
CROSSHAIR_HITBOX_CORRECTION = 0 # How generous the crosshair hitbox is. The higher, the less generous. Default is 0. Full crosshair is 8.

XP_REQUIREMENTS = [30, 40, 50, 60, 70, 80] # Number of xp required to level up per level
MAX_LEVEL = len(XP_REQUIREMENTS)

ASTEROIDS = {
    "SMALL_ASTEROID": {"type": 0, "size": 8, "coords": [8, 0], "hp": 6, "xp": 1},
    "MEDIUM_ASTEROID": {"type": 1, "size": 16, "coords" :[48, 16], "hp": 12, "xp": 8},
    "LARGE_ASTEROID": {"type": 2, "size": 32, "coords": [0, 32], "hp": 24, "xp": 16}
}
#Ui
BOTTOM_UI_BAR_SIZE = 10

#Sounds
BULLET_SOUND = 0
IMPACT_SOUND = 1
PICKUP_SOUND = 2
PLAYER_DEATH_SOUND = 3
PLAYER_DAMAGE_SOUND = 4
PLAYER_DASH_SOUND = 5
BOMB_SOUND = 6