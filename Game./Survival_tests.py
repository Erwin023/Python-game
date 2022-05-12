import unittest
import pygame
from Survival_player import Player
from Survival_enemy import Enemy
from Survival_bullet import Bullet
from Survival_game import Game
from Survival_box import Box
from Survival_bomb import Bomb
from Survival_boss import Boss
from Survival_rocket import Rocket

class Tests(unittest.TestCase):
    def setUp(self):
        self.game = Game()

    def test_player(self):
        self.assertEqual(self.game.player.pos_X, 150)
        self.assertEqual(self.game.player.pos_Y, 500)

    def test_bullet(self):
        b = Bullet(self.game, self.game.player.pos_X + 35, self.game.player.pos_Y + 25)
        c = Bullet(self.game, self.game.player.pos_X + 1150, self.game.player.pos_Y + 25)
        self.game.bullets.append(b)
        self.game.bullets.append(c)
        for i in range(150):
            b.tick()
        self.assertEqual(b.pos_X, 1385)
        self.game.tick()
        self.assertEqual(self.game.score, 10)
        self.assertNotIn(c, self.game.bullets)
        self.assertEqual(self.game.enemy[0].health, 80)
        self.assertEqual(self.game.enemy[0].pos_X, 1278)

    def test_collision_enemy(self):
        d = Enemy(self.game, 2)
        d.pos_X = 194
        self.game.enemy.append(d)
        self.game.tick()
        self.game.tick()
        self.assertEqual(d.pos_X, 192)
        self.assertNotIn(d, self.game.enemy)
        self.assertEqual(self.game.player.health, 80)

    def test_collision_box(self):
        e = Box(self.game)
        e.pos_X = 180
        self.game.box.append(e)
        self.game.tick()
        self.game.tick()
        self.assertEqual(e.is_open, True)

    def test_collision_bomb(self):
        f = Bomb(self.game)
        f.pos_X = 180
        self.game.bomb.append(f)
        self.game.tick()
        self.game.tick()
        self.assertEqual(self.game.player.health, 60)
        self.assertEqual(f.is_boom, True)

    def test_collision_boss(self):
        g = Boss(self.game)
        g.pos_X = 150
        self.game.boss.append(g)
        self.game.tick()
        self.assertEqual(self.game.player.health, 0)

    def test_collision_rocket(self):
        h = Rocket(self.game, 2)
        h.pos_Y = 509
        h.pos_X = 150
        self.game.rocket.append(h)
        self.game.tick()
        self.game.tick()
        self.assertEqual(self.game.player.health, 96)






if __name__ == "__main__":
    unittest.main()

