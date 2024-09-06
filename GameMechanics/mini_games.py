import pygame as pg
import random
from Cofigs.config import MENU_NAV_XPAD, SCREEN_HEIGHT, SCREEN_WIDTH
from GameObjects.dog import Dog
from GameObjects.toy import Toy
from Utilits.tools import load_image, text_render


class MiniGame:
    def __init__(self, game):
        self.game = game
        self.background = load_image("images/game_background.png", SCREEN_WIDTH, SCREEN_HEIGHT)

        self.dog = Dog()
        self.toys = pg.sprite.Group()
        self.score = 0
        self.start_time = pg.time.get_ticks()
        self.interval = 30000

    def new_game(self):
        self.dog = Dog()
        self.toys = pg.sprite.Group()
        self.score = 0
        self.start_time = pg.time.get_ticks()
        self.interval = 30000

    def update(self):
        if random.randint(0, 100) == 0:
            self.toys.add(Toy())
        self.dog.update()
        self.toys.update()
        hits = pg.sprite.spritecollide(self.dog, self.toys, True, pg.sprite.collide_rect_ratio(0.6))
        self.score += len(hits)
        if pg.time.get_ticks() - self.start_time > self.interval:
            self.game.happiness += int(self.score // 2)
            self.game.mode = "Main"

    def draw(self, screen):
        screen.blit(self.background, (0, 0))
        screen.blit(self.dog.image, self.dog.rect)
        screen.blit(text_render(self.score), (MENU_NAV_XPAD + 20, 80))
        self.toys.draw(screen)
