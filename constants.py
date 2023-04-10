framecount = 0 # The number of frames since game start. Does not go up in menu and resets at game over.

#Main
GAME_WIDTH = 104
GAME_HEIGHT = 140
FPS = 30
TITLE = "Space Survivor"

PLAYER_STARTING_X = 48
PLAYER_STARTING_Y = 120
PLAYER_HP = 3
PLAYER_IFRAMES = 30 # The amount of frames the player has invincibility after getting hit
PLAYER_DEATHFREEZE_DURATION = 30 # The amount of time the screen freezes when the player dies

BULLET_DAMAGE = 1
BULLET_COOLDOWN = 3
MAGNET_RANGE = 5

ASTEROID_COOLDOWN = 10 # How many frames it takes for an asteroid to spawn
ASTEROID_OFFSET_FROM_BORDERS = 2 # How close an asteroid can spawn to the border of the screen, in pixels
ASTEROID_HITBOX_CORRECTION = 0 # How generous the asteroid hitbox is. The higher, the less generous. Default is 0

MINIBOSS_FIRE_COOLDOWN = 60 # Number of frames it takes for the miniboss to re-shoot after shooting 
CROSSHAIR_SPEED = 1.5
CROSSHAIR_HITBOX_CORRECTION = 0 # How generous the crosshair hitbox is. The higher, the less generous. Default is 0. Full crosshair is 8.

XP_REQUIREMENTS = { # How much xp is required per level up
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
    "SMALL_ASTEROID": {"type": 0, "size": 8, "spritexcoord": 8, "spriteycoord": 0, "hp": 6, "xp": 1},
    "MEDIUM_ASTEROID": {"type": 1, "size": 16, "spritexcoord": 48, "spriteycoord": 16, "hp": 12, "xp": 8},
    "LARGE_ASTEROID": {"type": 2, "size": 32, "spritexcoord": 0, "spriteycoord": 32, "hp": 24, "xp": 16}
}

#Sounds
BULLET_SOUND = 0
IMPACT_SOUND = 1
PICKUP_SOUND = 2
PLAYER_DEATH_SOUND = 3
PLAYER_DAMAGE_SOUND = 4