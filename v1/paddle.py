# импортируем pygame
import pygame


# определяем черный цвет в rgb
black = (0, 0, 0)


# создадим класс ракетка он будет происходить от sprite в pygame
class Paddle(pygame.sprite.Sprite):
    # зададим параметры ракетки
    def __init__(self, color, width, height):
        # вызовем родительский класс sprite
        super().__init__()

        # создадим картинку ракетки и сделаем ее по умолчанию прозрачной
        self.image = pygame.Surface([width, height])
        self.image.fill(black)
        self.image.set_colorkey(black)

        pygame.draw.rect(self.image, color, [0, 0, width, height])

        # создадим обЪект мяч по картинке
        self.rect = self.image.get_rect()

    # создадим функцию для перемещения вверх
    def move_up(self, pixels):
        self.rect.y -= pixels
        # создадим условие чтобы не вылетать за экран
        if self.rect.y < 0:
            self.rect.y = 0

    # создадим функцию для движения вниз
    def move_down(self, pixels):
        self.rect.y += pixels
        # создадим условие чтобы не вылетать за экран
        if self.rect.y > 400:
            self.rect.y = 400
