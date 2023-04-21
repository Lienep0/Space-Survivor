# Main
GAME_WIDTH = 104
GAME_HEIGHT = 149
FPS = 30
TITLE = "Space Survivor"

# Player
PLAYER_STARTING_X = 48
PLAYER_STARTING_Y = 125
PLAYER_HP = 3
PLAYER_SPEED = 2
PLAYER_IFRAMES = 30 # The amount of frames the player has invincibility after getting hit
PLAYER_DEATHFREEZE_DURATION = 30 # The amount of time the screen freezes when the player dies

BULLET_DAMAGE = 1
BULLET_COOLDOWN = 10
MAGNET_RANGE = 15
EXPLODING_BULLET_RADIUS = 20

# Bomb
MAX_NUMBER_OF_BOMBS = 2
BOMB_DAMAGE = 1000
BOMB_BOSS_DAMAGE = 40

# Upgrade modifiers
DAMAGE_UPGRADE_BOOST = 0.5
FIRE_RATE_UPGRADE_BOOST = 1
MAGNET_UPGRADE_BOOST = 5
DASH_UPGRADE_SPEED_BOOST = 1
EXPLODING_UPGRADE_CHANCE = 0.2
PIERCING_UPGRADE_CHANCE = 0.2
QUAD_SHOT_FIRE_RATE_PENALTY = 1.7
MAXIMUM_HEALTH = 4

# Asteroids
ASTEROID_COOLDOWN = 10 # How many frames it takes for an asteroid to spawn
ASTEROID_OFFSET_FROM_BORDERS = 2 # How close an asteroid can spawn to the border of the screen, in pixels
ASTEROID_HITBOX_CORRECTION = 0 # How generous the asteroid hitbox is. The higher, the less generous. Default is 0

ASTEROIDS = {
    "SMALL_ASTEROID": {"type": 0, "size": 8, "coords": [8, 0], "hp": 6, "xp": 1},
    "MEDIUM_ASTEROID": {"type": 1, "size": 16, "coords" :[48, 16], "hp": 12, "xp": 8},
    "LARGE_ASTEROID": {"type": 2, "size": 32, "coords": [0, 32], "hp": 24, "xp": 16}
}

#Miniboss
MINIBOSS_HP = 100
MINIBOSS_HEIGHT = 20
MINIBOSS_FIRE_COOLDOWN = 60 # Number of frames it takes for the miniboss to re-shoot after shooting 
CROSSHAIR_SPEED = 1.25
CROSSHAIR_HITBOX_CORRECTION = 0 # How generous the crosshair hitbox is. The higher, the less generous. Default is 0. Full crosshair is 8.

# XP
XP_REQUIREMENTS = [30, 40, 50, 60, 70, 80] # Number of xp required to level up per level
MAX_LEVEL = len(XP_REQUIREMENTS)

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