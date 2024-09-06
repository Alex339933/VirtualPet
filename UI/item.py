

from Cofigs.config import DOG_HEIGHT, DOG_WIDTH
from Utilits.tools import load_image


class Item:
    def __init__(self, name, price, file, is_using=False, is_bought=False):
        self.file = file
        self.name = name
        self.price = price
        self.is_bought = is_bought
        self.is_using = is_using

        self.image = load_image(file, DOG_WIDTH // 1.7, DOG_HEIGHT // 1.7)
        self.full_image = load_image(file, DOG_WIDTH, DOG_HEIGHT)