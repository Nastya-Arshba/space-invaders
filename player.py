from pygame.sprite import Sprite
from pygame import Surface
from settings import *



class Player(Sprite):  # Класс Player расширяет, наследует возможности класса Sprite.
    def __init__(self, x, y, color):
        Sprite.__init__(self)  # Вызов родительского конструктора.
        self.image = Surface((PLAYER_WIDTH, PLAYER_HIGH))  # Квадрат 50 на 50 пикс.
        self.image.fill(color)  # Заливаем красным цветом.
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)

    def update(self, *arg, **kwargs) -> None:
        pass

