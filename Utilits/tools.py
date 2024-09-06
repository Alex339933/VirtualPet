import pygame as pg

pg.init()

font = pg.font.Font(None, 40)
font_maxi = pg.font.Font(None, 200)

def load_image(file, width, height):
    image = pg.image.load(file)
    image = pg.transform.scale(image, (width, height))
    return image


def text_render(text, font=font):
    return font.render(str(text), True, "Black")