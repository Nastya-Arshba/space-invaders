# Компьютерная игра Space Invaders.
import pygame

def start_game():  # Главная функция, вызывается из точки входа. Нужна для тестирования.
    print(f'Игра начинается')
    pygame.init()
    screen = pygame.display.set_mode((400, 400))  # Устанавливается размер экрана.
    pygame.display.set_caption("Space Invaders")  # Устанавливается заголовок окна.

    running = True  # Пока эта переменная истинна, игра продолжается.

    while running:  # "Бесконечный" цикл.
        pygame.time.delay(100)  # Время ожидания между перерисовками экрана (в миллисекундах).
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        screen.fill((255, 255, 255))  # Цвет экрана в RGB-кодировке (красный, зеленый, синий)
        pygame.display.flip()  # Применяем изменения.

    pygame.quit()


if __name__ == '__main__':  # Точка входа.
    start_game()
