# -*- coding: utf-8 -*-
from typing import Tuple
import pygame


class Projectile(pygame.sprite.Sprite):
    image: pygame.Surface
    rect: pygame.Rect

    def convert(self, image_path: str) -> None:
        self.image = pygame.image.load(image_path)
        self.image = pygame.transform.smoothscale(self.image, self.size)
        self.initial_image = self.image
        self.rect = self.image.get_rect()

    def rotate(self) -> None:
        self.angle += 3
        self.image = pygame.transform.rotozoom(self.initial_image, self.angle, 1)
        self.rect = self.image.get_rect(center=self.rect.center)

    def remove(self, player) -> None:
        player.projectiles.remove(self)

    def move(self,game) -> None:
        if self.direction == "left":
            if self.rect.x > 0:
                self.rotate()
                self.rect.x -= self.velocity
                if pygame.sprite.spritecollide(self, game.monsters, False, pygame.sprite.collide_mask):
                    self.remove(game.player)
            else:
                self.remove(game.player)
        else:
            if self.rect.x + self.rect.width < game.screen.get_width():
                self.rotate()
                self.rect.x += self.velocity
                if pygame.sprite.spritecollide(self, game.monsters, False, pygame.sprite.collide_mask):
                    self.remove(game.player)
            else:
                self.remove(game.player)

    def __init__(self, player, image_path: str, direction: str) -> None:
        super().__init__()
        self.size: Tuple[int, int] = (50, 50)
        self.convert(image_path)
        self.direction: str = direction
        if direction == "left":
            position = (player.rect.x, player.rect.centery)
        else:
            position = (player.rect.x + player.rect.width -50, player.rect.centery)
        self.rect.x, self.rect.y = position
        self.velocity: int = 6
        self.attack: int = 10
        self.angle: int = 0

    
    