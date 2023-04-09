import pyxel

def move_towards(sprite1_x, sprite1_y, sprite2_x, sprite2_y, speed):
    angle = pyxel.atan2(sprite2_y - sprite1_y, sprite2_x - sprite1_x)
    sprite1_x += pyxel.cos(angle) * speed
    sprite1_y += pyxel.sin(angle) * speed
    return sprite1_x, sprite1_y