# -*- coding: utf-8 -*-
import pygame
from typing import Tuple, Dict
from models.background import Background
from models.player import Player
from models.monster import Monster


class Window:
    size: Tuple[int, int]
    title: str
    running: bool = True
    screen: pygame.Surface
    background: Background
    player: Player
    monsters = pygame.sprite.Group()
    pressed: Dict[int, bool] = {}

    def set_size(self, size: Tuple[int, int]) -> None:
        self.size = size
        self.screen = pygame.display.set_mode(size)
    
    def set_title(self, title: str) -> None:
        self.title = title
        pygame.display.set_caption(title)

    def set_background(self, image_path: str, position: Tuple[int, int]) -> None:
        self.background = Background(image_path, position)

    def set_player(self, image_path: str, initial_pos: Tuple[int, int]) -> None:
        self.player = Player(image_path, initial_pos)

    def add_monster(self, image_path: str, position: Tuple[int, int], direction: str) -> None:
        self.monsters.add(Monster(image_path, position, direction))

    def collision(self, sprite1, sprite2) -> None:
        result: Dict[str, bool] = {"left": False, "right": False}
        collision = pygame.sprite.collide_mask(sprite1, sprite2)
        if collision:
            x: int = collision[0]
            width: int = sprite1.rect.width
            if x < width / 2:
                result["left"] = True
            elif x > width / 2:
                result["right"] = True
        return result

    def __init__(self, size: Tuple[int, int], title: str) -> None:
        self.set_size(size)
        self.set_title(title)