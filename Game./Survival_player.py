import pygame

class Player(object):
    def __init__(self, game):
        self.game = game
        self.icon = pygame.image.load('solider_stand2.png')
        self.pos_X = 150  # Position
        self.pos_Y = 500
        self.isJump = False
        self.jumpCount = 10
        self.can_move = True
        self.hitbox = (self.pos_X + 10, self.pos_Y - 5, 40, 70)
        self.health = 100
        self.healthbox = (self.pos_X + 7, self.pos_Y - 20, 50, 15)
        self.injurebox = (self.pos_X + 57, self.pos_Y - 20, 0, 15)
        self.count_hits = 0
        self.speed = 6

    def tick(self):
        # Input
        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_RIGHT] and self.pos_X < 1280 and self.can_move == True:
            self.pos_X += self.speed
        if pressed[pygame.K_LEFT] and self.pos_X > 0 and self.can_move == True:
            self.pos_X -= self.speed
        if not (self.isJump):
            if pressed[pygame.K_SPACE] and self.can_move == True:
                self.isJump = True
        else:
            if self.jumpCount >= -10:
                neg = 1
                if self.jumpCount < 0:
                    neg = -1
                self.pos_Y -= (self.jumpCount ** 2) / 2.5 * neg
                self.jumpCount -= 1
            else:
                self.isJump = False
                self.jumpCount = 10


    def draw(self):
        self.game.screen.blit(self.icon, (self.pos_X, self.pos_Y))
        self.hitbox = (self.pos_X + 10, self.pos_Y - 5, 40, 70)
        self.injurebox = (self.pos_X + 57 - (100 - self.health)/2, self.pos_Y - 20, 0 + (100 - self.health)/2, 15)
        self.healthbox = (self.pos_X + 7, self.pos_Y - 20, 50 - (100 - self.health)/2, 15)
        #pygame.draw.rect(self.game.screen, (255, 0, 0), self.hitbox, 2)
        pygame.draw.rect(self.game.screen, (255, 0, 0), self.injurebox)
        pygame.draw.rect(self.game.screen, (0, 255, 0), self.healthbox)









