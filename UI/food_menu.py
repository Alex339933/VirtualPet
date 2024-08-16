

from Cofigs.config import BUTTON_HEIGHT, BUTTON_WIDTH, MENU_NAV_XPAD, MENU_NAV_YPAD, SCREEN_HEIGHT, SCREEN_WIDTH
from GameObjects.food import Food
from UI.button import Button
from Utilits.tools import load_image, text_render


class FoodMenu:
    def __init__(self, game):
        self.is_using = False
        self.is_bought = False
        self.game = game
        self.menu_page = load_image("images/menu/menu_page.png", SCREEN_WIDTH, SCREEN_HEIGHT)

        self.bottom_label_off = load_image("images/menu/bottom_label_off.png", SCREEN_WIDTH, SCREEN_HEIGHT)
        self.bottom_label_on = load_image("images/menu/bottom_label_on.png", SCREEN_WIDTH, SCREEN_HEIGHT)
        self.top_label_off = load_image("images/menu/top_label_off.png", SCREEN_WIDTH, SCREEN_HEIGHT)
        self.top_label_on = load_image("images/menu/top_label_on.png", SCREEN_WIDTH, SCREEN_HEIGHT)

        self.items = [Food("Мясо", "images/food/meat.png", 30, 15),
                      Food("Корм", "images/food/dog food.png", 40, 40),
                      Food("Элитный корм", "images/food/dog food elite.png", 100, 25, medicine_power=2),
                      Food("Лекарство", "images/food/medicine.png", 200, 0, medicine_power=10),
                      Food("Яблоко", "images/food/apple.png", 35, 25, medicine_power=1),
                      Food("Кость", "images/food/bone.png", 5, 0, medicine_power=0, happiness=10)]

        self.current_item = 0

        self.item_rect = self.items[0].image.get_rect()
        self.item_rect.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)

        self.next_button = Button("Вперёд", SCREEN_WIDTH - MENU_NAV_XPAD - BUTTON_WIDTH, SCREEN_HEIGHT - MENU_NAV_YPAD,
                                  width=int(BUTTON_WIDTH // 1.2), height=int(BUTTON_HEIGHT // 1.2),
                                  func=self.to_next)
        self.previous_button = Button("Назад", MENU_NAV_XPAD + 30, SCREEN_HEIGHT - MENU_NAV_YPAD,
                                      width=int(BUTTON_WIDTH // 1.2), height=int(BUTTON_HEIGHT // 1.2),
                                      func=self.to_previous)

        self.eat_button = Button("Съесть", SCREEN_WIDTH // 2 - int(BUTTON_WIDTH // 1.5) // 2, SCREEN_HEIGHT // 2 + 95,
                                 width=int(BUTTON_WIDTH // 1.5), height=int(BUTTON_HEIGHT // 1.5), func=self.buy_and_eat)

        self.price_text = text_render(self.items[self.current_item].price)
        self.price_text_rect = self.price_text.get_rect()
        self.price_text_rect.center = (SCREEN_WIDTH // 2, 180)

        self.name_text = text_render(self.items[self.current_item].name)
        self.name_text_rect = self.name_text.get_rect()
        self.name_text_rect.center = (SCREEN_WIDTH // 2, 120)

    def to_next(self):
        if self.current_item != len(self.items) - 1:
            self.current_item += 1
        self.price_text = text_render(self.items[self.current_item].price)
        self.price_text_rect = self.price_text.get_rect()
        self.price_text_rect.center = (SCREEN_WIDTH // 2, 180)

        self.name_text = text_render(self.items[self.current_item].name)
        self.name_text_rect = self.name_text.get_rect()
        self.name_text_rect.center = (SCREEN_WIDTH // 2, 120)

    def to_previous(self):
        if self.current_item != 0:
            self.current_item -= 1
        self.price_text = text_render(self.items[self.current_item].price)
        self.price_text_rect = self.price_text.get_rect()
        self.price_text_rect.center = (SCREEN_WIDTH // 2, 180)

        self.name_text = text_render(self.items[self.current_item].name)
        self.name_text_rect = self.name_text.get_rect()
        self.name_text_rect.center = (SCREEN_WIDTH // 2, 120)

    def update(self):
        self.next_button.update()
        self.previous_button.update()
        self.eat_button.update()

    def is_clicked(self, event):
        self.next_button.is_clicked(event)
        self.previous_button.is_clicked(event)
        self.eat_button.is_clicked(event)

    def buy_and_eat(self):
        if self.game.money >= self.items[self.current_item].price:
            self.game.money -= self.items[self.current_item].price

            self.game.satiety += self.items[self.current_item].satiety
            if self.game.satiety > 100:
                self.game.satiety = 100

            self.game.health += self.items[self.current_item].medicine_power
            if self.game.health > 100:
                self.game.health = 100

            self.game.happiness += self.items[self.current_item].happiness
            if self.game.happiness > 100:
                self.game.happiness = 100

    def draw(self, screen):
        screen.blit(self.menu_page, (0, 0))

        screen.blit(self.items[self.current_item].image, self.item_rect)

        self.next_button.draw(screen)
        self.previous_button.draw(screen)
        self.eat_button.draw(screen)

        screen.blit(self.price_text, self.price_text_rect)
        screen.blit(self.name_text, self.name_text_rect)