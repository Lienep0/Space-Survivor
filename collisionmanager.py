import pyxel

from asteroids import asteroid_list
from bombs import bombs_list
from bullets import bullet_list
from constants import (CROSSHAIR_HITBOX_CORRECTION, CROSSHAIR_SPEED,
                       MAGNET_RANGE, MAGNET_UPGRADE_BOOST,
                       MINIBOSS_FIRE_COOLDOWN, MINIBOSS_HEIGHT)
from miniboss import miniboss
from particles import ExplodingImpact, particle_list
from pickups import pickup_list
from player import player
from didier import didier


def check_collisions():

    # Player Collisions
    range = MAGNET_RANGE + MAGNET_UPGRADE_BOOST * player.magnet_range_mod
    for pickup in list(pickup_list):
        if round_collision(player.x + player.radius, player.y + player.radius, pickup.x, pickup.y, range, pickup.radius, custom_sprite1= False):
            pickup.activated = True

        if pickup.activated:
            pickup.x, pickup.y, collected = move_towards(pickup.x, pickup.y, player.x + player.radius - pickup.radius, player.y + player.radius - pickup.radius, pickup.speed, player.size)
            if collected:
                pickup.collect()

    # Ateroid Collisions
    for asteroid in list(asteroid_list):
        if player.iframes_cooldown <= 0 and round_collision(asteroid.x, asteroid.y, player.x, player.y, asteroid.parameters.radius, player.radius):
                player.take_damage()

        for bullet in list(bullet_list):
            if asteroid not in bullet.things_hit and round_collision(asteroid.x, asteroid.y, bullet.x, bullet.y, asteroid.parameters.radius, bullet.radius):
                bullet.collide(asteroid)
        
        for explosion in [explosion for explosion in particle_list if type(explosion) == ExplodingImpact and asteroid not in explosion.things_hit]:
            if round_collision(asteroid.x, asteroid.y, explosion.x, explosion.y, asteroid.parameters.radius, explosion.radius, custom_sprite2= False):
                asteroid.take_damage(explosion.damage)
                explosion.things_hit.append(asteroid)

    # Miniboss Collisions
    if not miniboss.y <= MINIBOSS_HEIGHT:
        for projectile in list(miniboss.projectiles_list):
            if round_collision(projectile.x, projectile.y, player.x, player.y, projectile.radius, player.radius):
                player.take_damage()
                miniboss.projectiles_list.remove(projectile)

        if round_collision(miniboss.x, miniboss.y, player.x, player.y, miniboss.radius, player.radius):
            player.take_damage()

        for bullet in [bullet for bullet in bullet_list if miniboss not in bullet.things_hit]:
            if round_collision(miniboss.x, miniboss.y, bullet.x, bullet.y, miniboss.radius, bullet.radius):
                bullet.collide(miniboss)
        
        for explosion in [explosion for explosion in particle_list if type(explosion) == ExplodingImpact and miniboss not in explosion.things_hit]:
                if round_collision(miniboss.x, miniboss.y, explosion.x, explosion.y, miniboss.radius, explosion.radius, custom_sprite2= False):
                    miniboss.take_damage(explosion.damage)
                    explosion.things_hit.append(miniboss)

        if miniboss.crosshair is not None: 
            miniboss.crosshair.x, miniboss.crosshair.y, miniboss.crosshair.hasHit = move_towards(miniboss.crosshair.x, miniboss.crosshair.y,
                                                                                                 player.x + player.radius - miniboss.crosshair.radius, 
                                                                                                 player.y + player.radius - miniboss.crosshair.radius,
                                                                                                 CROSSHAIR_SPEED, CROSSHAIR_HITBOX_CORRECTION)
            if miniboss.crosshair.hasHit and player.iframes_cooldown <= 0:
                miniboss.shoot_crosshair()

    # Bomb collisions
    for bomb in list(bombs_list):
        for asteroid in [asteroid for asteroid in asteroid_list if asteroid not in bomb.things_hit]:
            if round_collision(asteroid.x, asteroid.y, bomb.x, bomb.y, asteroid.parameters.radius, bomb.radius, custom_sprite2= False):
                asteroid.take_damage(bomb.damage)
                bomb.things_hit.append(asteroid)

        if not miniboss.y <= MINIBOSS_HEIGHT and miniboss not in bomb.things_hit and round_collision(miniboss.x, miniboss.y, bomb.x, bomb.y, miniboss.radius, bomb.radius, custom_sprite2= False):
            miniboss.take_damage(bomb.bossdamage)
            bomb.things_hit.append(miniboss)

        if miniboss.crosshair is not None and round_collision(miniboss.crosshair.x, miniboss.crosshair.y, bomb.x, bomb.y, miniboss.crosshair.radius, bomb.radius, custom_sprite2= False):
            miniboss.crosshair = None
            miniboss.crosshair_cooldown = MINIBOSS_FIRE_COOLDOWN

        for projectile in list(miniboss.projectiles_list):
            if round_collision(projectile.x, projectile.y, bomb.x, bomb.y,projectile.radius, bomb.radius, custom_sprite2= False):
                miniboss.projectiles_list.remove(projectile)

        if didier.active and round_collision(didier.x, didier.y, bomb.x, bomb.y, didier.radius, bomb.radius, custom_sprite2= False):
            didier.take_damage(bomb.damage)

        for projectile in list(didier.projectiles_list):
            if round_collision(projectile.x, projectile.y, bomb.x, bomb.y,projectile.radius, bomb.radius, custom_sprite2= False):
                didier.projectiles_list.remove(projectile)

    # Didier collisions
    if didier.active:
        if round_collision(didier.x, didier.y, player.x, player.y, didier.radius, player.radius):
            player.take_damage()

        for bullet in list(bullet_list):
            if didier not in bullet.things_hit and round_collision(didier.x, didier.y, bullet.x, bullet.y, didier.radius, bullet.radius):
                bullet.collide(didier)
        
        for projectile in list(didier.projectiles_list):
            if round_collision(projectile.x, projectile.y, player.x, player.y, projectile.radius, player.radius):
                player.take_damage()
                didier.projectiles_list.remove(projectile)
        

def round_collision(sprite1_x, sprite1_y, sprite2_x, sprite2_y, radius1, radius2, custom_sprite1= True, custom_sprite2 = True):
    if custom_sprite1: 
        sprite1_x += radius1
        sprite1_y += radius1
    if custom_sprite2: 
        sprite2_x += radius2
        sprite2_y += radius2

    dx = sprite1_x - sprite2_x
    dy = sprite1_y - sprite2_y
    if int(pyxel.sqrt(dx**2 + dy**2)) <= radius1 + radius2:
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