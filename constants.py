framecount = 0

#Main
GAME_WIDTH = 104
GAME_HEIGHT = 140
FPS = 30
TITLE = "Space Survivor"

PLAYER_STARTING_X = 48
PLAYER_STARTING_Y = 120
PLAYER_HP = 3
PLAYER_IFRAMES = 30
PLAYER_DEATHFREEZE_DURATION = 30

BULLET_DAMAGE = 1
BULLET_COOLDOWN = 3
MAGNET_RANGE = 5

ASTEROID_COOLDOWN = 10
ASTEROID_OFFSET_FROM_BORDERS = 2
ASTEROID_HITBOX_CORRECTION = 0

XP_REQUIREMENTS = {
    0:30,
    1:40,
    2:50,
    3:60,
    4:70,
    5:80,
    6:90,
    7:100,
    8:110,
    9:120,
    10:130,
    11:-1 # No more xp
}

ASTEROIDS = {
    "SMALL_ASTEROID": {"type": 0, "size": 8, "spritexcoord": 32, "spriteycoord": 16, "hp": 6, "xp": 1},
    "MEDIUM_ASTEROID": {"type": 1, "size": 16, "spritexcoord": 48, "spriteycoord": 0, "hp": 12, "xp": 8},
    "LARGE_ASTEROID": {"type": 2, "size": 32, "spritexcoord": 0, "spriteycoord": 32, "hp": 24, "xp": 16}
}

#Sounds
BULLET_SOUND = 0
IMPACT_SOUND = 1
PICKUP_SOUND = 2
PLAYER_DEATH_SOUND = 3
PLAYER_DAMAGE_SOUND = 4