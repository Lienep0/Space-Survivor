import pyxel

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

PICKUP_SCORE = 10

# Bomb
START_NUMBER_OF_BOMBS = 2
MAX_NUMBER_OF_BOMBS = 2
BOMB_DAMAGE = 1000
BOMB_BOSS_DAMAGE = 40

# Upgrade modifiers
DAMAGE_UPGRADE_BOOST = 0.5
FIRE_RATE_UPGRADE_BOOST = 1
MAGNET_UPGRADE_BOOST = 15
DASH_UPGRADE_SPEED_BOOST = 1
CRITICAL_UPGRADE_CHANCE = 0.2
CRITICAL_UPGRADE_DAMAGE_MULTIPLIER = 2
PIERCING_UPGRADE_CHANCE = 0.2
QUAD_SHOT_FIRE_RATE_PENALTY = 1.7
BIG_UPGRADE_DAMAGE_MULTIPLIER = 2

HEALTH_UPGRADE_WEIGHT = [3, 2, 1, 0] # The weight of the health upgrade in the pool, based on the player's health (1-4 hp)
BOMB_UPGRADE_WEIGHT = [1.5, .5, 0] # The weight of the bomb upgrade in the pool, based on the player's number of bombs (0-2)

MAXIMUM_HEALTH = len(HEALTH_UPGRADE_WEIGHT)

# Asteroids
ASTEROID_SPEED = 1
ASTEROID_COOLDOWN = 10 # How many frames it takes for an asteroid to spawn
ASTEROID_OFFSET_FROM_BORDERS = 2 # How close an asteroid can spawn to the border of the screen, in pixels
ASTEROID_HITBOX_CORRECTION = 0 # How generous the asteroid hitbox is. The higher, the less generous. Default is 0

ASTEROIDS = {
    "SMALL_ASTEROID": {"type": 0, "size": 8, "coords": [8, 0], "hp": 6, "xp": 1, "score": 100},
    "MEDIUM_ASTEROID": {"type": 1, "size": 16, "coords" :[48, 16], "hp": 12, "xp": 8, "score": 500},
    "LARGE_ASTEROID": {"type": 2, "size": 32, "coords": [0, 32], "hp": 24, "xp": 16, "score": 1000}
}

# Miniboss
MINIBOSS_HP = 100
MINIBOSS_SCORE = 2000
MINIBOSS_HEIGHT = 20
MINIBOSS_FIRE_COOLDOWN = 60 # Number of frames it takes for the miniboss to re-shoot after shooting 
CROSSHAIR_SPEED = 1.25
CROSSHAIR_HITBOX_CORRECTION = 1 # How generous the crosshair hitbox is. The higher, the less generous. Default is 0. Full crosshair is 8.

# Xp
XP_REQUIREMENTS = [30, 40, 50, 60, 70, 80] # Number of xp required to level up per level
MAX_LEVEL = len(XP_REQUIREMENTS)

# Ui
BOTTOM_UI_BAR_SIZE = 10

# Controls
LEFT_KEY = pyxel.KEY_LEFT
RIGHT_KEY = pyxel.KEY_RIGHT
UP_KEY = pyxel.KEY_UP
DOWN_KEY = pyxel.KEY_DOWN

SHOOT_KEY = pyxel.KEY_SPACE
DASH_KEY = pyxel.KEY_SHIFT
BOMB_KEY = pyxel.KEY_B

PAUSE_KEY = pyxel.KEY_TAB
RESET_KEY = pyxel.KEY_R

GIVE_XP_KEY = pyxel.KEY_X
GIVE_UPGRADES_KEY = pyxel.KEY_U
GIVE_BOMB_KEY = pyxel.KEY_V

ASTEROID_SPAWN_KEY = pyxel.KEY_A
MINIBOSS_SPAWN_KEY = pyxel.KEY_M
SMALL_ASTEROID_KEY = pyxel.KEY_1
MEDIUM_ASTEROID_KEY = pyxel.KEY_2
LARGE_ASTEROID_KEY = pyxel.KEY_3

# Sounds
BULLET_SOUND = 0
IMPACT_SOUND = 1
PICKUP_SOUND = 2
PLAYER_DEATH_SOUND = 3
PLAYER_DAMAGE_SOUND = 4
PLAYER_DASH_SOUND = 5
BOMB_SOUND = 6
LEVEL_UP_SOUND = 7