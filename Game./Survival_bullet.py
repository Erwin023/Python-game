import pygame

class Bullet(object):
    def __init__(self, game, x, y):
        self.game = game
        self.pos_X = x
        self.pos_Y = y
        self.speed = 8
        self.hitbox = (self.pos_X - 5, self.pos_Y - 5, 10, 10)

    def tick(self):
        self.pos_X += self.speed
        if self.pos_X >= 1400:
            self.game.bullets.remove(self)

    def draw(self):
        pygame.draw.circle(self.game.screen, (255,0,0), (self.pos_X, int(self.pos_Y)), 5)
        self.hitbox = (self.pos_X - 5, self.pos_Y - 5, 10, 10)
        #pygame.draw.rect(self.game.screen, (0, 255, 0), self.hitbox, 2)
