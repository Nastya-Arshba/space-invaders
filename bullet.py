import pygame
from player import Player
from settings import *

downed_aliens = MAX_DOWNED_ALIENS


class Bullet(Player):

    def __init__(self, gamer, aliens, gamers, game_over):
        Player.__init__(self, gamer.rect.center[0], gamer.rect.top, color=BULLET_COLOR, width=4, height=4)
        self.gamers = gamers
        self.aliens = aliens
        self.game_over = game_over

    def update(self, *arg, **kwargs) -> None:
        global downed_aliens
        self.rect.y -= 5
        if self.rect.bottom < 0:
            self.gamers.remove(self)
        for alien in self.aliens:
            if alien.rect.left < self.rect.left and alien.rect.right > self.rect.right and alien.rect.bottom > self.rect.top:
                self.aliens.remove(alien)
                downed_aliens -= 1
                pygame.display.set_caption(f"Осталось сбить {downed_aliens}")
                if downed_aliens == 0:
                    self.game_over(True)
