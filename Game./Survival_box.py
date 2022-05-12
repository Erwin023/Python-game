import pygame
import random

class Box(object):
    def __init__(self, game):
        self.game = game
        self.icon = pygame.image.load('box.png')
        self.pos_X = 1280 # Position
        self.pos_Y = 510
        self.speed = 0.7
        self.hitbox = (self.pos_X, self.pos_Y, 65, 60)
        self.is_open = False
        self.box_time = 0

    def tick(self):
        # Input
        self.pos_X -= self.speed
        self.hitbox = (self.pos_X, self.pos_Y, 65, 60)
        if self.pos_X >= 1400:
            self.game.box.remove(self)

    def draw(self):
        self.game.screen.blit(self.icon, (self.pos_X, self.pos_Y))
        #pygame.draw.rect(self.game.screen, (0, 255, 0), self.hitbox, 2)

    def open(self):
        if self.hitbox[0] - self.game.player.hitbox[0] - self.game.player.hitbox[2] <= 0 and self.hitbox[0] + self.hitbox[2] - self.game.player.hitbox[0] >= 0:
            if self.hitbox[1] - self.game.player.hitbox[1] - self.game.player.hitbox[3] <= 0 and self.hitbox[1] + self.hitbox[3] - self.game.player.hitbox[1] >= 0:
                if self.is_open == False:
                    rand = random.random()
                    if rand < 0.7: # good things happen
                        if rand < 0.4:
                            print("health")
                            self.game.player.health = 100
                            self.is_open = True
                        elif rand >= 0.4 and rand < 0.7:
                            print("speed")
                            if self.game.player.speed <= 16:
                                self.game.player.speed += 2
                            self.is_open = True
                        else:
                            pass
                    else:
                        if rand >= 0.7 and rand < 0.8:
                            print("stuck")
                            self.game.player.can_move = False
                            self.box_time = pygame.time.get_ticks()
                            self.is_open = True
                        elif rand >= 0.9:
                            print("slow")
                            if self.game.player.speed >= 8:
                                self.game.player.speed -= 2
                            self.is_open = True
                        else:
                            pass

