import pyxel

def move_towards(sprite1_x, sprite1_y, sprite2_x, sprite2_y, speed, max_diff):
    dy = sprite2_y - sprite1_y
    dx = sprite2_x - sprite1_x
    if abs(dx) <= max_diff and abs(dy) <= max_diff: return sprite1_x, sprite1_y, True

    angle = pyxel.atan2(dy, dx)
    sprite1_x += pyxel.cos(angle) * speed
    sprite1_y += pyxel.sin(angle) * speed
    return sprite1_x, sprite1_y, False