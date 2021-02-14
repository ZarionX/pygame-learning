# -*- coding: utf-8 -*-
import pygame
from typing import Tuple


class Background:
    SURFACE: pygame.Surface
    POSITION: Tuple[int, int]

    def convert(self, image_path: str) -> None:
        self.SURFACE = pygame.image.load(image_path)
    
    def load(self, screen: pygame.Surface) -> None:
        screen.blit(self.SURFACE, self.POSITION)
    
    def __init__(self, image_path: str, position: Tuple[int, int]) -> None:
        self.convert(image_path)
        self.POSITION = position