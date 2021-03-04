# -*- coding: utf-8 -*-
import pygame
from typing import List, Tuple


class AnimateSprite(pygame.sprite.Sprite):
    def __init__(self, name: str, size: Tuple[int, int]) -> None:
        super().__init__()
        self.size = size
        self.image = pygame.image.load(f"./assets/{name}.png")
        self.image = pygame.transform.smoothscale(self.image, size)
        self.rect = self.image.get_rect()
        self.images = animation[name]
        self.current_image = 0
        self.animating = False

    def start_animation(self) -> None:
        self.animating = True

    def animate(self, direction: str, loop: bool = False) -> None:
        if self.animating:
            self.current_image += 1
            if self.current_image >= len(self.images[direction]):
                self.current_image = 0
                if not loop:
                    self.animating = False
            self.image = self.images[direction][self.current_image]
            self.image = pygame.transform.smoothscale(self.image, self.size)
            


def load_images(name: str) -> List[pygame.Surface]:
    images = [pygame.image.load(f"./assets/{name}/{name}{i}.png") for i in range(1, 24)]
    return images

def flip(images: List[pygame.Surface]) -> List[pygame.Surface]:
    result = [pygame.transform.flip(image, True, False) for image in images]
    return result

animation = {
    "player": {
        "left": flip(load_images("player")),
        "right": load_images("player")
    },
    "mummy": {
        "left": load_images("mummy"),
        "right": flip(load_images("mummy"))
    },
    "alien": {
        "left": load_images("alien"),
        "right": flip(load_images("alien"))
    }
}