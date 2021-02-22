# -*- coding: utf-8 -*-
import pygame
from typing import Tuple


class Monster(pygame.sprite.Sprite):
    image: pygame.Surface
    rect: pygame.Rect

    def convert(self, image_path: str) -> None:
        self.image = pygame.image.load(image_path)
        self.initial_image = self.image
        self.rect = self.image.get_rect()

    def forward(self, player) -> None:
        if not pygame.sprite.collide_mask(self, player):
            if self.direction == "rigth":
                self.rect.x += self.velocity
            elif self.direction == "left":
                self.rect.x -= self.velocity

    def update_health_bar(self, screen: pygame.Surface) -> None:
        back_bar_color = (142, 142, 142)
        bar_color = (84, 223, 50)
        back_bar_position = pygame.Surface((self.max_health, 5)).get_rect()
        back_bar_position.centerx = self.rect.centerx
        back_bar_position.y = self.rect.y - 10
        bar_position = (back_bar_position.x, back_bar_position.y, self.health, 5)
        pygame.draw.rect(screen, back_bar_color, back_bar_position)
        pygame.draw.rect(screen, bar_color, bar_position)

    def __init__(self, image_path: str, position: Tuple[int, int], direction: str) -> None:
        super().__init__()
        self.convert(image_path)
        self.rect.x, self.rect.y = position
        self.max_health: int = 100
        self.health = self.max_health
        self.velocity: int = 3
        self.direction: str = direction


    