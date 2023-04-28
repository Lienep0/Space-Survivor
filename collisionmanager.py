import pyxel

from asteroids import asteroid_list
from bombs import bombs_list
from bullets import bullet_list
from constants import (ASTEROID_HITBOX_CORRECTION, CROSSHAIR_HITBOX_CORRECTION,
                       CROSSHAIR_SPEED, MAGNET_RANGE, MAGNET_UPGRADE_BOOST,
                       MINIBOSS_FIRE_COOLDOWN, MINIBOSS_HEIGHT, PICKUP_SOUND)
from miniboss import miniboss
from particles import ExplodingBulletsImpact, MinibossShotLine, particle_list
from pickups import pickup_list
from player import player


def check_collisions():

    # Player Collisions
    range = MAGNET_RANGE + MAGNET_UPGRADE_BOOST * player.magnet_range_mod
    for pickup in list(pickup_list):
        if round_collision((player.x + (player.size/2 - .5)), (player.y + (player.size/2 - .5)), pickup.x + 1, pickup.y + 1, range):
            pickup.activated = True

        if pickup.activated:
            pickup.x, pickup.y, collected = move_towards(pickup.x, pickup.y, player.x + 3, player.y + 3, pickup.speed, 5)
            if collected:
                pyxel.play(2, PICKUP_SOUND)
                player.xp += 1
                pickup_list.remove(pickup)

    # Ateroid Collisions
    for asteroid in list(asteroid_list):
        if player.iframes_cooldown <= 0 and round_collision(asteroid.x + (asteroid.parameters.size/2 - .5), asteroid.y + (asteroid.parameters.size/2 - .5),
                                                            (player.x + (player.size/2 - .5)), (player.y + (player.size/2 - .5)), 
                                                            asteroid.parameters.size/2 + 3 - ASTEROID_HITBOX_CORRECTION):
                player.take_damage()

        for bullet in list(bullet_list):
            if asteroid not in bullet.things_hit and round_collision(asteroid.x + (asteroid.parameters.size/2 - .5), 
                               asteroid.y + (asteroid.parameters.size/2 - .5), 
                               (bullet.x + (bullet.xsize/2 - .5)), (bullet.y + (bullet.ysize/2 - .5)), 
                               asteroid.parameters.size/2 + 3):
                bullet.collide(asteroid)
        
        for explosion in [explosion for explosion in particle_list if type(explosion) == ExplodingBulletsImpact]:
            if asteroid not in explosion.things_hit and round_collision(asteroid.x + (asteroid.parameters.size/2 - .5), 
                                                                        asteroid.y + (asteroid.parameters.size/2 - .5), 
                                                                        explosion.x, explosion.y, explosion.radius):
                asteroid.take_damage(explosion.damage)
                explosion.things_hit.append(asteroid)

    # Miniboss Collisions
    if not miniboss.y <= MINIBOSS_HEIGHT:
        for projectile in list(miniboss.projectiles_list):
            if round_collision(projectile.x + projectile.size / 2, projectile.y + projectile.size / 2, player.x + player.size / 2, player.y + player.size / 2, 5):
                player.take_damage()
                miniboss.projectiles_list.remove(projectile)

        if round_collision(miniboss.x + miniboss.size/2, miniboss.y + miniboss.size/2, 
                                    player.x + player.size / 2, player.y + player.size / 2, 
                                    miniboss.size/2 + 2):
            player.take_damage()

        for bullet in [bullet for bullet in bullet_list if miniboss not in bullet.things_hit]:
            if round_collision(miniboss.x + miniboss.size/2, miniboss.y + miniboss.size/2, 
                                    bullet.x + bullet.xsize / 2, bullet.y + bullet.ysize / 2, 
                                    miniboss.size/2 + 2):
                bullet.collide(miniboss)
        
        for explosion in [explosion for explosion in particle_list if type(explosion) == ExplodingBulletsImpact]:
            if round_collision(miniboss.x + miniboss.size/2 + 1, miniboss.y + miniboss.size/2 + 1, 
                                explosion.x, explosion.y, explosion.radius):
                miniboss.take_damage(explosion.damage)
                explosion.things_hit.append(miniboss)

        if miniboss.crosshair is not None: 
            miniboss.crosshair.x, miniboss.crosshair.y, miniboss.crosshair.hasHit = move_towards(miniboss.crosshair.x, miniboss.crosshair.y,
                                                                                                 player.x - miniboss.crosshair.size/4, player.y - miniboss.crosshair.size/4,
                                                                                                 CROSSHAIR_SPEED, 2 + CROSSHAIR_HITBOX_CORRECTION)
            if miniboss.crosshair.hasHit and player.iframes_cooldown <= 0:
                player.take_damage()
                particle_list.append(MinibossShotLine(miniboss.x + 8 + (miniboss.sprite_offset/8), miniboss.y + 8, player.x + 3, player.y))
                miniboss.crosshair = None
                miniboss.shoot_cooldown = MINIBOSS_FIRE_COOLDOWN

    # Bomb collisions
    for bomb in list(bombs_list):
        for asteroid in list(asteroid_list):
            if asteroid not in bomb.things_hit and round_collision(asteroid.x + (asteroid.parameters.size/2 - .5), 
                                                                   asteroid.y + (asteroid.parameters.size/2 - .5), 
                                                                   bomb.x, bomb.y, bomb.radius):
                asteroid.take_damage(bomb.damage)

        if miniboss.active and miniboss not in bomb.things_hit and round_collision(miniboss.x + (miniboss.size/2 - .5), 
                                                                                   miniboss.y + (miniboss.size/2 - .5), 
                                                                                   bomb.x, bomb.y, bomb.radius):
            miniboss.take_damage(bomb.bossdamage)
            bomb.things_hit.append(miniboss)

        if miniboss.crosshair is not None and round_collision(miniboss.crosshair.x + (miniboss.crosshair.size/2 - .5), 
                                                              miniboss.crosshair.y + (miniboss.crosshair.size/2 - .5), 
                                                              bomb.x, bomb.y, bomb.radius):
            miniboss.crosshair = None
            miniboss.shoot_cooldown = MINIBOSS_FIRE_COOLDOWN

        for projectile in list(miniboss.projectiles_list):
            if round_collision(projectile.x + projectile.size / 2, projectile.y + projectile.size / 2, bomb.x, bomb.y, bomb.radius):
                miniboss.projectiles_list.remove(projectile)

def round_collision(sprite1_x, sprite1_y, sprite2_x, sprite2_y, radius):
    dx = sprite1_x - sprite2_x
    dy = sprite1_y - sprite2_y
    if pyxel.sqrt(dx**2 + dy**2) <= radius:
        return True
    return False

def move_towards(sprite1_x, sprite1_y, sprite2_x, sprite2_y, speed, max_diff):
    dy = sprite2_y - sprite1_y
    dx = sprite2_x - sprite1_x
    if abs(dx) <= max_diff and abs(dy) <= max_diff: return sprite1_x, sprite1_y, True

    angle = pyxel.atan2(dy, dx)
    sprite1_x += pyxel.cos(angle) * speed
    sprite1_y += pyxel.sin(angle) * speed
    return sprite1_x, sprite1_y, False