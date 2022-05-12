import pygame, sys
from Survival_player import Player
from Survival_enemy import Enemy
from Survival_bomb import Bomb
from Survival_rocket import Rocket
from Survival_box import Box
from Survival_bullet import Bullet
from Survival_boss import Boss
import random


class Game(object):
    def __init__(self):
        # Configuration
        self.tps_max = 30

        # Initialization
        pygame.init()
        self.level = 0
        self.score = 0
        self.score_font = pygame.font.Font('freesansbold.ttf', 32)
        self.screen = pygame.display.set_mode((1280, 720))
        self.tps_clock = pygame.time.Clock()
        self.tps_delta = 0.0
        self.player = Player(self)
        self.enemy_speed = 2
        self.rocket_speed = 2
        self.enemy = [Enemy(self, self.enemy_speed) for i in range(1)]
        self.bomb = [Bomb(self) for i in range(1)]
        self.rocket = [Rocket(self, self.rocket_speed) for i in range(1)]
        self.box = [Box(self) for i in range(1)]
        self.icon = pygame.image.load('gun_logo.png')
        self.font = pygame.font.Font('freesansbold.ttf', 32)
        pygame.display.set_caption('Survive on the battlefield')
        pygame.display.set_icon(self.icon)
        self.bullets = []
        self.time = 0
        self.boss = [Boss(self) for i in range(0)]



    # Game loop
    def play_game(self):
        while True:
            # Handle events
            if self.player.health <= 0:
                print("Game Over")
                sys.exit(0)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit(0)
                elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                    sys.exit(0)
                elif event.type == pygame.KEYDOWN and event.key == pygame.K_z and len(self.bullets) < 10:
                    b = Bullet(self, self.player.pos_X + 35, self.player.pos_Y + 25)
                    self.bullets.append(b)


            # Ticking
            self.tps_delta += self.tps_clock.tick() / 1000.0
            while self.tps_delta > 1 / self.tps_max:
                self.tick()
                self.tps_delta -= 1 / self.tps_max
            # Adding objects
            if random.random() < 0.001 + self.level/1000 and self.time <= pygame.time.get_ticks() - 2000:
                self.enemy.append(Enemy(self, self.enemy_speed))
                self.time = pygame.time.get_ticks()
            if random.random() < 0.0001:
                self.bomb.append(Bomb(self))
            if random.random() < 0.001 + self.level/1000:
                self.rocket.append(Rocket(self, self.rocket_speed))
            if random.random() < 0.0001:
                self.box.append(Box(self))
            if (self.score == 100 and len(self.boss) == 0) or (self.score == 1000 and len(self.boss) == 0) or (self.score == 2000 and len(self.boss) == 0) or (self.score == 3000 and len(self.boss) == 0):
                self.boss.append(Boss(self))
            self.screen.fill((100, 50, 0))  # Orange colour
            self.draw()
            pygame.display.flip()

    def tick(self):
        self.player.tick()

        for boss in self.boss:
            boss.tick()
            boss.collision()
            if boss.health <= 0:
                self.boss.pop(self.boss.index(boss))

        for enemy in self.enemy:
            enemy.tick()
            enemy.collision()
            if enemy.health <= 0:
                self.enemy.pop(self.enemy.index(enemy))

        for bomb in self.bomb:
            bomb.tick()
            bomb.collision()
            if bomb.is_boom == True:
                if bomb.bomb_time < pygame.time.get_ticks() - 3000:
                    self.bomb.pop(self.bomb.index(bomb))

        for box in self.box:
            box.tick()
            if box.is_open == False:
                box.open()
                if box.is_open == True and self.player.can_move == True:
                    self.box.pop(self.box.index(box))
            elif box.is_open == True and box.box_time <= pygame.time.get_ticks() - 5000:
                self.player.can_move = True
                self.box.pop(self.box.index(box))
            else:
                pass

        for rocket in self.rocket:
            rocket.tick()
            if rocket.is_boom == True:
                rocket.collision()
                rocket.is_boom = False
                if rocket.boom_time < pygame.time.get_ticks() - 9000 and self.rocket_speed <= 2:
                    self.rocket.pop(self.rocket.index(rocket))
                elif rocket.boom_time < pygame.time.get_ticks() - 5500 and self.rocket_speed > 2:
                    self.rocket.pop(self.rocket.index(rocket))
        for bullet in self.bullets:
            for enemy in self.enemy:
                if enemy.hitbox[2] + enemy.hitbox[0] >= bullet.hitbox[0] >= enemy.hitbox[0]:
                    if enemy.hitbox[3] + enemy.hitbox[1] >= bullet.hitbox[1] >= enemy.hitbox[1]:
                        self.bullets.remove(bullet)
                        enemy.hit()
                        self.score += 10
                        if self.score == 500 or self.score == 1000 or self.score == 2000:
                            self.enemy_speed += 2
                            self.level += 1
                        if self.score == 5000:
                            self.level += 3
                            self.rocket_speed += 2
                        if enemy.health <= 0:
                            self.enemy.pop(self.enemy.index(enemy))
        #for bullet in self.bullets:
            for boss in self.boss:
                if boss.hitbox[2] + boss.hitbox[0] >= bullet.hitbox[0] >= boss.hitbox[0]:
                    if boss.hitbox[3] + boss.hitbox[1] >= bullet.hitbox[1] >= boss.hitbox[1]:
                        self.bullets.remove(bullet)
                        boss.hit()
                    if boss.health <= 0:
                        self.score += 100
                        self.boss.pop(self.boss.index(boss))
            bullet.tick()


    def draw(self):
        self.player.draw()
        text = self.score_font.render('Score: ' + str(self.score), 1, (0,255,0))
        self.screen.blit(text, (8, 8))
        for bomb in self.bomb:
            bomb.draw()
        for box in self.box:
            box.draw()
        for enemy in self.enemy:
            enemy.draw()
        for rocket in self.rocket:
            rocket.draw()
        for bullet in self.bullets:
            bullet.draw()
        for boss in self.boss:
            boss.draw()


if __name__ == "__main__":
    gra = Game()
    gra.play_game()