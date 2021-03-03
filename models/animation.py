# -*- coding: utf-8 -*-
import pygame
import os
from typing import List


class AnimateSprite(pygame.sprite.Sprite):
    def __init__(self, name: str) -> None:
        super().__init__()
        self.image = pygame.image.load(f"./assets/{name}.png")
        self.images = animation.get(name)
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
            


def load_images(name: str) -> List:
    images = []
    for file in os.listdir(f"./assets/{name}"):
        images.append(pygame.image.load(f"./assets/{name}/{file}"))
    return images

def flip(images: List) -> None:
    result = []
    for image in images:
        result.append(pygame.transform.flip(image, True, False))
    return result

animation = {
    "player": {
        "left": flip(load_images("player")),
        "right": load_images("player")
    },
    "mummy": {
        "left": load_images("mummy"),
        "right": flip(load_images("mummy"))
    }
}