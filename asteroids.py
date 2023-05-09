from random import randint

import pyxel

from constants import (ASTEROID_OFFSET_FROM_BORDERS, ASTEROIDS,
                       GAME_HEIGHT, GAME_WIDTH)
from particles import ScoreParticle, particle_list
from pickups import spawn_pickups
from player import player

asteroid_list = []

class Asteroid:
    def __init__(self, variety, speed):
        self.parameters = AsteroidParameters(ASTEROIDS[variety])
        
        self.x = randint(ASTEROID_OFFSET_FROM_BORDERS, GAME_WIDTH - self.parameters.size - ASTEROID_OFFSET_FROM_BORDERS)
        self.y = -self.parameters.size
        self.speed = speed
        self.maxhp = self.parameters.hp

    def take_damage(self, damage):
        self.parameters.hp -= damage
        if self.parameters.hp <= 0 and self in asteroid_list:
            player.score += self.parameters.score
            player.asteroids_destroyed += 1
            particle_list.append(ScoreParticle(self.x + self.parameters.size / 2, self.y, self.parameters.score))
            spawn_pickups(self)
            asteroid_list.remove(self)

    def update(self):
        self.y += self.speed
        if self.y > GAME_HEIGHT + self.parameters.size:
            if self in asteroid_list: asteroid_list.remove(self)
            
    def draw(self):
        pyxel.blt(self.x, self.y, 0, self.parameters.spritexcoord + self.parameters.size * ((self.maxhp - self.parameters.hp) // (self.maxhp/self.parameters.damaged_sprites)), 
                  self.parameters.spriteycoord, self.parameters.size, self.parameters.size, 0)


class AsteroidParameters:
    def __init__(self,parameters):
        self.size = parameters["size"]
        self.radius = (self.size - 1) / 2
        self.spritexcoord = parameters["coords"][0]
        self.spriteycoord = parameters["coords"][1]
        self.hp = parameters["hp"]
        self.xp = parameters["xp"]
        self.score = parameters["score"]
        self.damaged_sprites = parameters["damaged_sprites"]