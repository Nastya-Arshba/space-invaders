import random

import pygame.image

from player import Player
from settings import *


def get_random_x():  # Функция для нахождения случайной координаты x.
    return random.randint(PLAYER_WIDTH / 2, GAME_WIDTH - PLAYER_WIDTH / 2)


class Alien(Player):  # Наследование alien от player.

    def __init__(self, group, game_over):  # Конструктор.
        Player.__init__(self, get_random_x(), PLAYER_HEIGHT / 2, image="alien")
        self.group = group
        self.game_over = game_over


    def update(self, *arg, **kwargs) -> None:  # Метод.
        self.rect.top += 5
        if self.rect.bottom >= GAME_HIGH:
            self.game_over(False)
