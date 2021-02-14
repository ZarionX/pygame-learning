# -*- coding: utf-8 -*-
import pygame
from typing import Tuple, Dict
from models.background import Background
from models.player import Player


class Window:
    SIZE: Tuple[int, int]
    TITLE: str
    running: bool = True
    screen: pygame.Surface
    background: Background
    player: Player
    pressed: Dict[int, bool] = {}

    def set_size(self, size: Tuple[int, int]) -> None:
        self.SIZE = size
        self.screen = pygame.display.set_mode(size)
    
    def set_title(self, title: str) -> None:
        self.TITLE = title
        pygame.display.set_caption(title)

    def set_background(self, image_path: str, position: Tuple[int, int]) -> None:
        self.background = Background(image_path, position)

    def set_player(self, imaget_path: str, initial_pos: Tuple[int, int]) -> None:
        self.player = Player(imaget_path, initial_pos)
    
    def __init__(self, size: Tuple[int, int], title: str) -> None:
        self.set_size(size)
        self.set_title(title)