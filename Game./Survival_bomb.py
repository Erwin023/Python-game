import pygame
import random
from Survival_player import Player

class Bomb(object):
    def __init__(self, game):
        self.game = game
        self.icon = pygame.image.load('bomb.png')
        self.pos_X = 1280 # Position
        self.pos_Y = 510
        self.speed = 2
        self.is_boom = False
        self.hitbox = (self.pos_X, self.pos_Y, 65, 60)
        self.bomb_time = 0

    def tick(self):
        if self.is_boom == False:
            self.pos_X -= self.speed
            self.hitbox = (self.pos_X, self.pos_Y, 65, 60)
            if self.pos_X >= 1400:
                self.game.bomb.remove(self)
        else:
            self.speed = 0
            self.icon = pygame.image.load('rocket_boom.png')

    def draw(self):
        self.game.screen.blit(self.icon, (self.pos_X, self.pos_Y))
        #pygame.draw.rect(self.game.screen, (0, 255, 0), self.hitbox, 2)

    def collision(self):
        if self.hitbox[0] - self.game.player.hitbox[0] - self.game.player.hitbox[2] <= 0 and self.hitbox[0] + self.hitbox[2] - self.game.player.hitbox[0] >= 0:
            if self.hitbox[1] - self.game.player.hitbox[1] - self.game.player.hitbox[3] <= 0 and self.hitbox[1] + self.hitbox[3] - self.game.player.hitbox[1] >= 0:
                if self.is_boom == False:
                    self.is_boom = True
                    self.bomb_time = pygame.time.get_ticks()
                    self.game.player.count_hits += 20
                    self.game.player.health -= 40
        pass
