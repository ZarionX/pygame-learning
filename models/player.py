# -*- coding: utf-8 -*-
from typing import Tuple
import pygame
from models.projectile import Projectile
import models.animation as animation


class Player(animation.AnimateSprite):
    image: pygame.Surface
    rect: pygame.Rect
    projectiles = pygame.sprite.Group()
    
    def load(self, screen: pygame.Surface) -> None:
        screen.blit(self.image, self.rect)

    def move_right(self) -> None:
        self.rect.x += self.velocity

    def move_left(self) -> None:
        self.rect.x -= self.velocity

    def update_animation(self) -> None:
        self.animate(self.direction)

    def launch_projectile(self, image_path: str, direction: str) -> None:
        self.projectiles.add(Projectile(self, image_path, direction))
        self.direction = direction
        self.start_animation()

    def update_health_bar(self, screen: pygame.Surface) -> None:
        back_bar_position = pygame.Surface((self.max_health, 5)).get_rect()
        back_bar_position.centerx = self.rect.centerx
        back_bar_position.y = self.rect.y + 10
        bar_position = (back_bar_position.x, back_bar_position.y, self.health, 5)
        pygame.draw.rect(screen, (142, 142, 142), back_bar_position)
        pygame.draw.rect(screen, (84, 223, 50), bar_position)

    def damage(self, damage: int, game) -> None:
        self.health -= damage
        if self.health <= 0:
            game.stop()
    
    def __init__(self, image_path: str, initial_pos: Tuple[int, int]) -> None:
        super().__init__("player")
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = initial_pos
        self.max_health: int = 100
        self.health: int = self.max_health
        self.attack: int = 10
        self.velocity: int = 4
        self.direction = "right"