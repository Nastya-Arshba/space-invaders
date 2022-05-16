import pygame
from datetime import datetime, timedelta
from player import Player
from settings import *
from bullet import Bullet


class Gamer(Player):

    def __init__(self, aliens, gamers, game_over):
        Player.__init__(self, GAME_WIDTH - PLAYER_WIDTH / 2, GAME_HIGH - PLAYER_HEIGHT / 2, image="sniper")
        self.aliens = aliens
        self.gamers = gamers
        self.last_shot = datetime.now()
        self.game_over = game_over

    def update(self, *arg, **kwargs) -> None:
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.rect.left -= 5
            if self.rect.left < 0:
                self.rect.left = 0
        if keys[pygame.K_RIGHT]:
            self.rect.right += 5
            if self.rect.right > GAME_WIDTH:
                self.rect.right = GAME_WIDTH
        if keys[pygame.K_UP]:
            now = datetime.now()
            if now - self.last_shot < BETWEEN_SHOTS:
                return
            print("Пиу-пиу")
            bullet = Bullet(self, self.aliens, self.gamers, self.game_over)
            self.last_shot = now
            self.gamers.add(bullet)
