import pyxel

# Main
GAME_WIDTH = 104
GAME_HEIGHT = 149
FPS = 30
TITLE = "Space Survivor"

BOSS_WAVES = 1500 # After how many frames a miniboss spawns

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

# Upgrades
UPGRADE_MENU_COOLDOWN = 30

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
ASTEROID_OFFSET_FROM_BORDERS = 2 # How far an asteroid can spawn from the border of the screen, in pixels
ASTEROIDS = [
    {"size": 8, "coords": [0, 128], "hp": 6, "xp": 1, "score": 100, "cooldown": 30, "weight": 90, "damaged_sprites" : 4},
    {"size": 16, "coords" :[0, 136], "hp": 12, "xp": 8, "score": 500, "cooldown": 60, "weight": 8, "damaged_sprites" : 4},
    {"size": 32, "coords": [0, 152], "hp": 24, "xp": 16, "score": 1000, "cooldown": 90, "weight": 2, "damaged_sprites" : 5}
]

# Miniboss
MINIBOSS_HP = 100
MINIBOSS_SCORE = 2000
MINIBOSS_HEIGHT = 20
MINIBOSS_FIRE_COOLDOWN = 60 # Number of frames it takes for the miniboss to re-shoot after shooting 
MINIBOSS_ENTRANCE_TIMER = 90

CROSSHAIR_SPEED = 1.25
CROSSHAIR_HITBOX_CORRECTION = 3 # How generous the crosshair hitbox is. The higher, the less generous. Default is 3. Full crosshair is 10.

# Xp
XP_REQUIREMENTS = [10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 75] # Number of xp required to level up per level
MAX_LEVEL = len(XP_REQUIREMENTS)

# Didier
DIDIER_HP = 12
DIDIER_WAVE = 300

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
MINIBOSS_DEATH_SOUND = 8
EXPLODING_BULLET_IMPACT_SOUND = 9