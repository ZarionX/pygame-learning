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


    def __init__(self, image_path: str, position: Tuple[int, int], direction: str) -> None:
        super().__init__()
        self.convert(image_path)
        self.rect.x, self.rect.y = position
        self.max_health: int = 100
        self.health = self.max_health
        self.velocity: int = 3
        self.direction: str = direction


    