import pygame as pg

from Cofigs.config import DOG_HEIGHT, DOG_WIDTH, MENU_NAV_YPAD, SCREEN_HEIGHT, SCREEN_WIDTH
from Utilits.tools import load_image

class Dog(pg.sprite.Sprite):
    def __init__(self):
        pg.sprite.Sprite.__init__(self)
        self.image = load_image("images/dog.png", DOG_WIDTH // 2, DOG_HEIGHT // 2)
        self.rect = self.image.get_rect()
        self.rect.centerx = SCREEN_WIDTH // 2
        self.rect.centery = SCREEN_HEIGHT - MENU_NAV_YPAD - 10

    def update(self):
        keys = pg.key.get_pressed()

        if keys[pg.K_a]:
            self.rect.x -= 2

        if keys[pg.K_d]:
            self.rect.x += 2