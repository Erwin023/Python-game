import pygame
import random

class Enemy(object):
    def __init__(self, game, speed):
        self.game = game
        self.icon = pygame.image.load('enemy.png')
        self.pos_X = 1280  # Position
        self.pos_Y = 510
        #self.speed = random.uniform(1.5, 3)
        self.speed = speed
        self.hitbox = (self.pos_X + 5, self.pos_Y, 48, 65)
        self.health = 100
        self.healthbox = (self.pos_X, self.pos_Y - 20, 50, 15)
        self.injurebox = (self.pos_X + 50, self.pos_Y - 20, 0, 15)
        self.count_hits = 0

    def tick(self):
        # Input
        self.pos_X -= self.speed
        self.hitbox = (self.pos_X + 5, self.pos_Y, 48, 65)
        if self.pos_X >= 1400:
            self.game.enemy.remove(self)



    def draw(self):
        self.game.screen.blit(self.icon, (self.pos_X, self.pos_Y))
        self.injurebox = (self.pos_X + 50 - self.count_hits, self.pos_Y - 20, 0 + self.count_hits, 15)
        self.healthbox = (self.pos_X, self.pos_Y - 20, 50 - self.count_hits, 15)
        #pygame.draw.rect(self.game.screen, (0, 255, 0), self.hitbox, 2)
        pygame.draw.rect(self.game.screen, (255, 0, 0), self.injurebox)
        pygame.draw.rect(self.game.screen, (0, 255, 0), self.healthbox)


    def hit(self):
        self.health -= 20
        self.count_hits += 10
        pass

    def collision(self):
        if self.hitbox[0] - self.game.player.hitbox[0] - self.game.player.hitbox[2] <= 0 and self.hitbox[0] + self.hitbox[2] - self.game.player.hitbox[0] >= 0:
            if self.hitbox[1] - self.game.player.hitbox[1] - self.game.player.hitbox[3] <= 0 and self.hitbox[1] + self.hitbox[3] - self.game.player.hitbox[1] >= 0:
                self.game.player.count_hits += 10
                self.game.player.health -= 20
                self.health -= 100
        pass