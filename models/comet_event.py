# -*- coding: utf-8 -*-
import pygame
import random
from models.comet import Comet


class CometFallEvent:
    comets: pygame.sprite.Group = pygame.sprite.Group()

    def add_percent(self) -> None:
        self.percent += self.percent_speed / 100

    def reset_percent(self) -> None:
        self.percent = 0

    def full_loaded(self) -> bool:
        return self.percent >= 100

    def add_comet(self, image_path: str, screen: pygame.Surface) -> None:
        self.comets.add(Comet(image_path, screen))

    def try_fall(self, image_path: str, game) -> None:
        if self.full_loaded() and len(game.monsters) == 0:
            self.falling = True
            for i in range(1, random.randint(5, 15)):
                self.add_comet(image_path, game.screen)

    def update_percent(self, screen: pygame.Surface) -> None:
        self.add_percent()
        pygame.draw.rect(screen, (0, 0, 0), (0, screen.get_height() - 20, screen.get_width(), 10))
        pygame.draw.rect(screen, (187, 11, 11), (0, screen.get_height() - 20, (screen.get_width() / 100) * self.percent, 10))

    def __init__(self) -> None:
        self.percent = 0
        self.percent_speed = 10
        self.falling = False