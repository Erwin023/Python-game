import pygame
import random

class Rocket(object):
    def __init__(self, game, speed):
        self.game = game
        self.icon = pygame.image.load('rocket.png')
        self.pos_X = random.uniform(20, 1260) # Position
        self.pos_Y = 0
        self.speed = speed
        self.hitbox = (self.pos_X - 45, self.pos_Y - 720, 150, 790)
        self.is_boom = False
        self.boom_time = pygame.time.get_ticks()

    def tick(self):
        # Input
        if self.pos_Y <= 510:
            self.pos_Y += self.speed
            self.hitbox = (self.pos_X - 45, self.pos_Y - 720, 150, 790)
        else:
            self.speed = 0
            self.icon = pygame.image.load('rocket_boom.png')
            self.is_boom = True

    def draw(self):
        self.game.screen.blit(self.icon, (self.pos_X, self.pos_Y))
        #pygame.draw.rect(self.game.screen, (0, 255, 0), self.hitbox, 2)

    def collision(self):
        if (self.hitbox[0] - self.game.player.hitbox[0] - self.game.player.hitbox[2] <= 0 and self.hitbox[0] + self.hitbox[2] - self.game.player.hitbox[0] >= 0) and self.is_boom == True:
            self.game.player.count_hits += 2
            self.game.player.health -= 4
        pass
