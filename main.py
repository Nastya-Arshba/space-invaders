# Компьютерная игра Space Invaders.
import pygame
import time

from pygame.font import Font  # Шрифт.
from alien import Alien
from gamer import Gamer
from settings import *

pygame.init()
screen = pygame.display.set_mode((GAME_WIDTH, GAME_HIGH))  # Устанавливается размер экрана.

running = True  # Пока эта переменная истинна, игра продолжается.
success = False  # Результат игры.
font = Font("assets/PressStart2P-Regular.ttf", 30)


def start_game():  # Главная функция, вызывается из точки входа. Нужна для тестирования.
    global running, screen, success  # Глобальные переменные.
    print(f'Игра начинается')
    pygame.display.set_caption(f"Сбей {MAX_DOWNED_ALIENS} инопланетян")  # Устанавливается заголовок окна.
    aliens = pygame.sprite.Group()  # Группа инопланетян для совместной обработки.
    gamers = pygame.sprite.Group()  # Группа снайпер и пули.
    alien = Alien(aliens, game_over)  # Первый инопланетянин.
    gamer = Gamer(aliens, gamers, game_over)  # Снайпер (игрок), 1 на всю игру.
    aliens.add(alien)  # Добавляем в группу.
    gamers.add(gamer)  # Добавляем в группу.
    last_alien_time = datetime.now()  # Запоминаем время вылета последнего инопланетянина.
    space = pygame.image.load("assets/space.jpg")  # Готовим фон (звезды).

    while running:  # "Бесконечный" цикл.
        pygame.time.delay(100)  # Время ожидания между перерисовками экрана (в миллисекундах).
        for event in pygame.event.get():  # Обработка событий.
            if event.type == pygame.QUIT:
                running = False
        now = datetime.now()  # Текущее время.
        if now - last_alien_time > BETWEEN_ALIENS:  # Интервал от вылета последнего инопланетянина.
            alien = Alien(aliens, game_over)  # Выпускаем нового инопланетянина каждые 3 сек.
            aliens.add(alien)  # Добавляем в группу.
            last_alien_time = now  # Отсчитываем время заново.
        screen.blit(space, (0, 0))  # Рисуем звезды.
        aliens.update()  # Обновляем данные.
        gamers.update()  # Обновляем данные.
        aliens.draw(screen)  # Рисуем персонажей.
        gamers.draw(screen)  # Рисуем персонажей.
        pygame.display.flip()  # Применяем изменения.
    color = SUCCESS_COLOR if success else FAILURE_COLOR
    text = SUCCESS_TEXT if success else FAILURE_TEXT
    text = font.render(text, True, color)
    text_x = GAME_WIDTH / 2 - text.get_rect().width / 2
    text_y = GAME_HIGH / 2 - text.get_rect().height / 2
    screen.blit(text, (text_x, text_y))  # Выводим результат игры.
    pygame.display.flip()

    time.sleep(5)
    pygame.quit()


def game_over(_success):  # Окончание игры: True - выиграл человек, False - выиграл компьютер.
    global running, screen, font, success
    print("Инопланетяне выиграли" if not success else "Стрелок выиграл")
    running = False
    success = _success


if __name__ == '__main__':  # Точка входа.
    start_game()
