# -*- coding: utf-8 -*-
from typing import Tuple
import pygame


class Player(pygame.sprite.Sprite):
    surface: pygame.Surface
    rect: pygame.Rect

    def convert(self, image_path: str) -> None:
        self.surface = pygame.image.load(image_path)
        self.rect = self.surface.get_rect()
    
    def load(self, screen: pygame.Surface) -> None:
        screen.blit(self.surface, self.rect)

    def move_right(self) -> None:
        self.rect.x += self.velocity

    def move_left(self) -> None:
        self.rect.x -= self.velocity
    
    def __init__(self, image_path: str, initial_pos: Tuple[int, int]) -> None:
        super().__init__()
        self.convert(image_path)
        self.rect.x, self.rect.y = initial_pos
        self.MAX_HEALTH: int = 100
        self.health: int = self.MAX_HEALTH
        self.attack: int = 10
        self.velocity: int = 4