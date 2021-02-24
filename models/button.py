# -*- coding: utf-8 -*-
import pygame
from typing import Tuple
import time


class Button:
    image: pygame.Surface
    rect: pygame.Rect

    def convert(self, image_path: str) -> None:
        self.image = pygame.image.load(image_path)
        self.image = pygame.transform.smoothscale(self.image, self.size)
        self.rect = self.image.get_rect()

    def load(self, screen: pygame.Surface) -> None:
        screen.blit(self.image, self.rect)

    def __init__(self, image_path: str, position: Tuple[int, int]) -> None:
        self.size: Tuple[int, int] = (400, 150)
        self.convert(image_path)
        self.rect.x, self.rect.y = position