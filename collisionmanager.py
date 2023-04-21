import pyxel

from player import player
from miniboss import miniboss
from bullets import bullet_list
from pickups import pickup_list
from bomb import bomb_list
from asteroids import asteroid_list
from constants import MAGNET_RANGE, MAGNET_UPGRADE_BOOST, ASTEROID_HITBOX_CORRECTION, MINIBOSS_FIRE_COOLDOWN, MINIBOSS_HEIGHT
from particles import ExplodingBulletsImpact, particle_list

def check_collisions():

    # Player Collisions
    range = MAGNET_RANGE + MAGNET_UPGRADE_BOOST * len([x for x in player.inventory if x.name == "Magnet"])
    for pickup in pickup_list:
        if round_collision((player.x + (player.size/2 - .5)), (player.y + (player.size/2 - .5)), pickup.x + 1, pickup.y + 1, range):
            pickup.activated = True

    if player.iFramesCooldown <= 0:
        for asteroid in asteroid_list:
            if round_collision(asteroid.x + (asteroid.parameters.size/2 - .5), asteroid.y + (asteroid.parameters.size/2 - .5), 
                            (player.x + (player.size/2 - .5)), (player.y + (player.size/2 - .5)), 
                            asteroid.parameters.size/2 + 3 - ASTEROID_HITBOX_CORRECTION):
                player.take_damage()
    
    # Bullet Collisions
    for bullet in bullet_list:
        for asteroid in [asteroid for asteroid in asteroid_list if asteroid not in bullet.things_hit]:
            if round_collision(asteroid.x + (asteroid.parameters.size/2 - .5), asteroid.y + (asteroid.parameters.size/2 - .5), 
                        (bullet.x + (bullet.xsize/2 - .5)), (bullet.y + (bullet.ysize/2 - .5)), 
                        asteroid.parameters.size/2 + 3):
                bullet.collide(asteroid)

    # Bullet Explosions Collisions
    for explosion in [x for x in particle_list if type(x) == ExplodingBulletsImpact]:
        for asteroid in [asteroid for asteroid in asteroid_list if asteroid not in explosion.things_hit]:
            if round_collision(asteroid.x + (asteroid.parameters.size/2 - .5), asteroid.y + (asteroid.parameters.size/2 - .5), explosion.x, explosion.y, explosion.radius):
                asteroid.take_damage(explosion.damage)
                explosion.things_hit.append(asteroid)

    # Miniboss Collisions
    for projectile in miniboss.projectiles_list:
        if round_collision(projectile.x + projectile.size / 2, projectile.y + projectile.size / 2, player.x + player.size / 2, player.y + player.size / 2, 5):
            player.take_damage()
            miniboss.projectiles_list.remove(projectile)

    if miniboss.y <= MINIBOSS_HEIGHT:
        for bullet in [bullet for bullet in bullet_list if miniboss not in bullet.things_hit]:
            if round_collision(miniboss.x + miniboss.size/2, miniboss.y + miniboss.size/2, 
                                    (bullet.x + (bullet.xsize/2 - .5)), (bullet.y + (bullet.ysize/2 - .5)), 
                                    miniboss.size/2 + 2):
                bullet.collide(miniboss)
                bullet.things_hit.append(miniboss)
            
        for explosion in [particle for particle in particle_list if type(particle) == ExplodingBulletsImpact and miniboss not in particle.things_hit]:
            if round_collision(miniboss.x + miniboss.size/2 + 1, miniboss.y + miniboss.size/2 + 1, 
                                    explosion.x, explosion.y, explosion.radius):
                miniboss.take_damage(explosion.damage)
                explosion.things_hit.append(miniboss)

    # Bomb collisions
    for bomb in bomb_list:
        for asteroid in asteroid_list:
            if asteroid not in bomb.things_hit and round_collision(asteroid.x + (asteroid.parameters.size/2 - .5), asteroid.y + (asteroid.parameters.size/2 - .5), bomb.x, bomb.y, bomb.radius):
                asteroid.take_damage(bomb.damage)

        if miniboss.active and miniboss not in bomb.things_hit and round_collision(miniboss.x + (miniboss.size/2 - .5), miniboss.y + (miniboss.size/2 - .5), bomb.x, bomb.y, bomb.radius):
            miniboss.take_damage(bomb.bossdamage)
            bomb.things_hit.append(miniboss)

        if miniboss.crosshair is not None and round_collision(miniboss.crosshair.x + (miniboss.crosshair.size/2 - .5), miniboss.crosshair.y + (miniboss.crosshair.size/2 - .5), bomb.x, bomb.y, bomb.radius):
            miniboss.crosshair = None
            miniboss.shoot_cooldown = MINIBOSS_FIRE_COOLDOWN

        for projectile in miniboss.projectiles_list:
            if round_collision(projectile.x + projectile.size / 2, projectile.y + projectile.size / 2, bomb.x, bomb.y, bomb.radius):
                miniboss.projectiles_list.remove(projectile)

def round_collision(sprite1_x, sprite1_y, sprite2_x, sprite2_y, radius):
    dx = sprite1_x - sprite2_x
    dy = sprite1_y - sprite2_y
    if pyxel.sqrt(dx**2 + dy**2) <= radius:
        return True
    return False