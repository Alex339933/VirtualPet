import random
import json
from Cofigs.config import BUTTON_HEIGHT, BUTTON_WIDTH, DECREASE, DOG_HEIGHT, DOG_WIDTH, DOG_Y, FPS, ICON_SIZE, \
    INCREASE_OF_COINS, PADDING, SCREEN_HEIGHT, SCREEN_WIDTH
from GameMechanics.mini_games import MiniGame
from UI import clothes_menu
from UI.button import Button
from UI.clothes_menu import ClothesMenu
from UI.food_menu import FoodMenu
from Utilits.tools import load_image, text_render, font_maxi
import pygame as pg


class Game:
    def __init__(self):
        pg.init()

        mini_font = pg.font.Font(None, 15)
        pg.time.set_timer(INCREASE_OF_COINS, 2000)
        pg.time.set_timer(DECREASE, 1000)

        with open("Game/save.json", "r", encoding="UTF-8") as f:
            data = json.load(f)

        # Загрузка иконок
        self.health_image = load_image("images/health.png", ICON_SIZE, ICON_SIZE)
        self.happiness_image = load_image("images/happiness.png", ICON_SIZE, ICON_SIZE)
        self.satiety_image = load_image("images/satiety.png", ICON_SIZE, ICON_SIZE)
        self.money_image = load_image("images/money.png", ICON_SIZE, ICON_SIZE)
        self.dog_image = load_image("images/dog.png", DOG_WIDTH, DOG_HEIGHT)
        self.background = load_image("images/background.png", SCREEN_WIDTH, SCREEN_HEIGHT)
        self.money = data["money"]
        self.clock = pg.time.Clock()

        button_x = SCREEN_WIDTH - BUTTON_WIDTH - PADDING

        self.eat_button = Button("Еда", button_x, PADDING + ICON_SIZE, func=self.food_menu_on)
        self.games_button = Button("Игры", button_x, PADDING + ICON_SIZE * 2, func=self.game_on)
        self.cloth_button = Button("Одежда", button_x, PADDING + ICON_SIZE * 3, func=self.clothes_menu_on)
        self.upgrade_button = Button("Улучшить", SCREEN_WIDTH - ICON_SIZE, 0, width=BUTTON_WIDTH // 3,
                                     height=BUTTON_HEIGHT // 3, text_font=mini_font, func=self.increase_money)

        self.buttons = [self.eat_button, self.games_button, self.cloth_button, self.upgrade_button]

        self.coins_per_second = data["coins_per_second"]
        self.costs_of_upgrade = {}
        for key, value in data["costs_of_upgrade"].items():
            self.costs_of_upgrade[int(key)] = value
        self.mode = "Main"

        # Создание окна
        self.screen = pg.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pg.display.set_caption("Виртуальный питомец")

        self.health = data["health"]
        self.happiness = data["happiness"]
        self.satiety = data["satiety"]

        self.clothes_menu = ClothesMenu(self, data["clothes"])
        self.food_menu = FoodMenu(self)
        self.mini_game = MiniGame(self)
        self.run()

    def clothes_menu_on(self):
        self.mode = "Clothes menu"

    def game_on(self):
        self.mode = "Mini game"
        self.mini_game.new_game()

    def food_menu_on(self):
        self.mode = "Food menu"

    def run(self):
        while True:
            self.event()
            self.update()
            self.draw()
            self.clock.tick(FPS)

    def increase_money(self):
        for cost, check in self.costs_of_upgrade.items():
            if not check and self.money >= cost:
                self.coins_per_second += 1
                self.money -= cost
                self.costs_of_upgrade[cost] = True
                break

    def event(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                if self.mode == "Game over":
                    data = {
                        "happiness": 100,
                        "satiety": 100,
                        "health": 100,
                        "money": 10,
                        "coins_per_second": 1,
                        "costs_of_upgrade": {
                            "100": False,
                            "500": False,
                            "1000": False,
                            "5000": False,
                            "10000": False
                        },
                        "clothes": [{
                            "name": "Синяя футболка",
                            "price": 10,
                            "image": "images/items/blue t-shirt.png",
                            "is_using": False,
                            "is_bought": False

                        },

                            {

                                "name": "Ботинки",
                                "price": 50,
                                "image": "images/items/boots.png",
                                "is_using": False,
                                "is_bought": False
                            },
                            {
                                "name": "Шляпа",
                                "price": 50,
                                "image": "images/items/hat.png",
                                "is_using": False,
                                "is_bought": False,
                            }
                        ]
                    }
                else:
                    data = {
                        "happiness": self.happiness,
                        "satiety": self.satiety,
                        "health": self.health,
                        "money": self.money,
                        "coins_per_second": self.coins_per_second,
                        "costs_of_upgrade": {
                            "100": self.costs_of_upgrade[100],
                            "500": self.costs_of_upgrade[500],
                            "1000": self.costs_of_upgrade[1000],
                            "5000": self.costs_of_upgrade[5000],
                            "10000": self.costs_of_upgrade[10000]
                        },
                        "clothes": []
                    }
                    for item in self.clothes_menu.items:
                        data["clothes"].append({
                            "name": item.name,
                            "price": item.price,
                            "file": item.file,
                            "is_put_on": item.is_using,
                            "is_bought": item.is_bought
                        }
                        )
                with open("Game/save.json", "w", encoding="UTF-8") as f:
                    json.dump(data, f, ensure_ascii=False)
                pg.quit()
                exit()
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_ESCAPE:
                    self.mode = "Main"

            if self.mode == "Main":
                for button in self.buttons:
                    button.is_clicked(event)

            elif self.mode == "Clothes menu":
                self.clothes_menu.is_clicked(event)

            elif self.mode == "Food menu":
                self.food_menu.is_clicked(event)

            if event.type == INCREASE_OF_COINS:
                self.money += self.coins_per_second

            if event.type == DECREASE:
                chance = random.randint(1, 10)
                if chance <= 5:
                    self.satiety -= 1
                elif 5 <= chance <= 9:
                    self.happiness -= 1
                else:
                    self.health -= 1
            if event.type == pg.MOUSEBUTTONDOWN and event.button == 1:
                self.money += 1

    def update(self):
        if self.mode == "Main":
            for button in self.buttons:
                button.update()
        elif self.mode == "Clothes menu":
            self.clothes_menu.update()
        elif self.mode == "Food menu":
            self.food_menu.update()
        elif self.mode == "Mini game":
            self.mini_game.update()

        if self.satiety <= 0 or self.happiness <= 0 or self.health <= 0:
            self.mode = "Game over"

    def draw(self):
        # Отрисовка иконок
        self.screen.blit(self.background, (0, 0))
        self.screen.blit(self.satiety_image, (PADDING, PADDING * 2 + ICON_SIZE))
        self.screen.blit(self.happiness_image, (PADDING, PADDING))
        self.screen.blit(self.health_image, (PADDING, PADDING * 3 + ICON_SIZE * 2))
        self.screen.blit(self.money_image, (SCREEN_WIDTH - ICON_SIZE - PADDING, PADDING))

        # Отрисовка значений
        self.screen.blit(text_render(self.happiness), (PADDING + ICON_SIZE, PADDING * 6))
        self.screen.blit(text_render(self.satiety), (PADDING + ICON_SIZE, PADDING * 7 + ICON_SIZE))
        self.screen.blit(text_render(self.health), (PADDING + ICON_SIZE, PADDING * 8 + ICON_SIZE * 2))
        self.screen.blit(text_render(self.money), (SCREEN_WIDTH - ICON_SIZE - PADDING * 2, PADDING * 6))

        # Отрисовка собаки
        self.screen.blit(self.dog_image, (SCREEN_WIDTH // 2 - DOG_WIDTH // 2, DOG_Y))

        for item in self.clothes_menu.items:
            if item.is_using:
                self.screen.blit(item.full_image, (SCREEN_WIDTH // 2 - DOG_WIDTH // 2, DOG_Y))

        for button in self.buttons:
            button.draw(self.screen)

        if self.mode == "Clothes menu":
            self.clothes_menu.draw(self.screen)

        elif self.mode == "Food menu":
            self.food_menu.draw(self.screen)

        elif self.mode == "Mini game":
            self.mini_game.draw(self.screen)

        elif self.mode == "Game over":
            text = font_maxi.render("ПРОИГРЫШ", True, "red")
            text_rect = text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))
            self.screen.blit(text, text_rect)

        pg.display.flip()
