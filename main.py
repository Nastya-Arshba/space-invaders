# Компьютерная игра Space Invaders.
import pygame

from player import Player
from settings import *


def start_game():  # Главная функция, вызывается из точки входа. Нужна для тестирования.
    print(f'Игра начинается')
    pygame.init()
    screen = pygame.display.set_mode((GAME_WIDTH, GAME_HIGH))  # Устанавливается размер экрана.
    pygame.display.set_caption("Space Invaders")  # Устанавливается заголовок окна.
    player_group = pygame.sprite.Group()
    bot = Player(100, 100, RED)
    gamer = Player(200, 200, GREEN)
    player_group.add(bot)
    player_group.add(gamer)


    running = True  # Пока эта переменная истинна, игра продолжается.

    while running:  # "Бесконечный" цикл.
        pygame.time.delay(100)  # Время ожидания между перерисовками экрана (в миллисекундах).
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        player_group.update()
        screen.fill((255, 255, 255))  # Цвет экрана в RGB-кодировке (красный, зеленый, синий)
        player_group.draw(screen)
        pygame.display.flip()  # Применяем изменения.

    pygame.quit()


if __name__ == '__main__':  # Точка входа.
    start_game()
