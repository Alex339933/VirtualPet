import pygame as pg
import random
from Cofigs.config import MENU_NAV_XPAD, MENU_NAV_YPAD, SCREEN_HEIGHT, TOY_SIZE
from Utilits.tools import load_image

class Toy(pg.sprite.Sprite):
    def __init__(self):
        pg.sprite.Sprite.__init__(self)
        toys = ["images/toys/ball.png", "images/toys/blue bone.png", "images/toys/red bone.png"]
        self.image = load_image(random.choice(toys), TOY_SIZE, TOY_SIZE)
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(MENU_NAV_XPAD, SCREEN_HEIGHT - MENU_NAV_XPAD - self.image.get_width())
        self.rect.y = 30

    def update(self):
        self.rect.y += 2
        if self.rect.y == SCREEN_HEIGHT - MENU_NAV_YPAD - 10:
            self.kill()