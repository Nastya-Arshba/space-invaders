import pygame
from pygame.sprite import Sprite
from pygame import Surface
from settings import *


class Player(Sprite):  # Класс Player расширяет, наследует возможности класса Sprite.

    def __init__(self, x, y, color=None, width=PLAYER_WIDTH, height=PLAYER_HEIGHT, image=None):
        Sprite.__init__(self)  # Вызов родительского конструктора.
        if image:
            self.image = pygame.image.load(f"assets/{image}.png")
            self.rect = self.image.get_rect()
        else:
            self.image = Surface((width, height))  # Квадрат 50 на 50 пикс.
            self.image.fill(color)  # Заливаем цветом.
            self.rect = self.image.get_rect()
        self.rect.center = (x, y)

    def update(self, *arg, **kwargs) -> None:
        pass

