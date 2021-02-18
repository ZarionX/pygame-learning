# -*- coding: utf-8 -*-
import pygame
from typing import Tuple


class Background:
    image: pygame.Surface
    position: Tuple[int, int]

    def convert(self, image_path: str) -> None:
        self.image = pygame.image.load(image_path)
    
    def load(self, screen: pygame.Surface) -> None:
        screen.blit(self.image, self.position)
    
    def __init__(self, image_path: str, position: Tuple[int, int]) -> None:
        self.convert(image_path)
        self.position = position