# импортируем pygame и randint
import pygame
from random import randint


# определяем черный цвет в rgb
black = (0, 0, 0)


# создадим класс мяч он будет происходить от sprite в pygame
class Ball(pygame.sprite.Sprite):
    # зададим параметры мяча
    def __init__(self, color, width, height):
        # вызовем родительский класс sprite
        super().__init__()

        # создадим картинку мяча и сделаем ее по умолчанию прозрачной
        self.image = pygame.Surface([width, height])
        self.image.fill(black)
        self.image.set_colorkey(black)

        pygame.draw.rect(self.image, color, [0, 0, width, height])

        # создфдим массив с векторами скоростей по осям x и y
        self.velocity = [randint(4, 8), randint(-8, 8)]

        # создадим обЪект мяч по картинке
        self.rect = self.image.get_rect()

    # создадим функцию для движения мяча
    def update(self):
        self.rect.x += self.velocity[0]
        self.rect.y += self.velocity[1]

    # создадим функцию для осткока
    def bounce(self):
        self.velocity[0] = -self.velocity[0]
        self.velocity[1] = randint(-8, 8)
