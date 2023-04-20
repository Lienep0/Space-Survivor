import math

def move_towards(sprite1_x, sprite1_y, sprite2_x, sprite2_y, speed, max_diff):
    dy = sprite2_y - sprite1_y
    dx = sprite2_x - sprite1_x
    if abs(dx) <= max_diff and abs(dy) <= max_diff: return sprite1_x, sprite1_y, True

    angle = math.atan2(dy, dx)
    sprite1_x += math.cos(angle) * speed
    sprite1_y += math.sin(angle) * speed
    return sprite1_x, sprite1_y, False

def round_collision(sprite1_x, sprite1_y, sprite2_x, sprite2_y, radius):
    dx = sprite1_x - sprite2_x
    dy = sprite1_y - sprite2_y
    if math.sqrt(dx**2 + dy**2) <= radius:
        return True
    return False