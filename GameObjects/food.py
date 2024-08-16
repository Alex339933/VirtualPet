

from Cofigs.config import FOOD_SIZE
from Utilits.tools import load_image


class Food:
    def __init__(self, name, image, price, satiety, medicine_power=6, happiness=0):
        self.name = name
        self.price = price
        self.satiety = satiety
        self.medicine_power = medicine_power
        self.happiness = happiness
        self.image = load_image(image, FOOD_SIZE, FOOD_SIZE)