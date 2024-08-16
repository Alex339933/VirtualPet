
import os
import pygame as pg


SCREEN_WIDTH = os.environ.get("SCREEN_WIDTH")
SCREEN_HEIGHT = os.environ.get("SCREEN_HEIGHT")
DOG_WIDTH = os.environ.get("DOG_WIDTH")
DOG_HEIGHT = os.environ.get("DOG_HEIGHT")
DOG_Y = os.environ.get("DOG_Y")
ICON_SIZE = os.environ.get("ICON_SIZE")
PADDING = os.environ.get("PADDING")
BUTTON_WIDTH = os.environ.get("BUTTON_WIDTH")
BUTTON_HEIGHT = os.environ.get("BUTTON_HEIGHT")
FPS = os.environ.get("FPS")

MENU_NAV_XPAD = os.environ.get("MENU_NAV_XPAD")
MENU_NAV_YPAD = os.environ.get("MENU_NAV_YPAD")

FOOD_SIZE = os.environ.get("FOOD_SIZE")
TOY_SIZE = os.environ.get("TOY_SIZE")

INCREASE_OF_COINS = pg.USEREVENT + 1
DECREASE = pg.USEREVENT + 2
