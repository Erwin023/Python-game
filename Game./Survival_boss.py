import pygame
import random

class Boss(object):
    def __init__(self, game):
        self.game = game
        self.icon = pygame.image.load('boss.png')
        self.pos_X = 1280  # Position
        self.pos_Y = 440
        #self.speed = random.uniform(1.5, 3)
        self.speed = 2
        self.hitbox = (self.pos_X + 30, self.pos_Y + 10, 58, 115)
        self.health = 100
        self.healthbox = (self.pos_X + 35, self.pos_Y - 20, 50, 15)
        self.injurebox = (self.pos_X + 85, self.pos_Y - 20, 0, 15)
        self.count_hits = 0

    def tick(self):
        # Input
        self.pos_X -= self.speed
        self.hitbox = (self.pos_X + 30, self.pos_Y + 10, 58, 115)


    def draw(self):
        self.game.screen.blit(self.icon, (self.pos_X, self.pos_Y))
        self.injurebox = (self.pos_X + 85 - self.count_hits, self.pos_Y - 20, 0 + self.count_hits, 15)
        self.healthbox = (self.pos_X + 35, self.pos_Y - 20, 50 - self.count_hits, 15)
        #pygame.draw.rect(self.game.screen, (0, 255, 0), self.hitbox, 2)
        pygame.draw.rect(self.game.screen, (255, 0, 0), self.injurebox)
        pygame.draw.rect(self.game.screen, (0, 255, 0), self.healthbox)


    def hit(self):
        self.health -= 2
        self.count_hits += 1
        pass

    def collision(self):
        if self.hitbox[0] - self.game.player.hitbox[0] - self.game.player.hitbox[2] <= 0:
            self.game.player.count_hits += 50
            self.game.player.health -= 100
        pass