# -*- coding: utf-8 -*-
import pygame
import random
from typing import Tuple
import models.animation as animation


class Monster(animation.AnimateSprite):
    image: pygame.Surface
    rect: pygame.Rect

    def forward(self, game) -> None:
        if not pygame.sprite.collide_mask(self, game.player):
            self.animating = True
            if self.direction == "right":
                self.rect.x += self.velocity
            elif self.direction == "left":
                self.rect.x -= self.velocity
        else:
            self.animating = False
            game.player.damage(self.attack, game)

    def update_animation(self) -> None:
        self.animate(self.direction, True)

    def update_health_bar(self, screen: pygame.Surface) -> None:
        back_bar_position = pygame.Surface((self.max_health, 5)).get_rect()
        back_bar_position.centerx = self.rect.centerx
        back_bar_position.y = self.rect.y - 10
        bar_position = (back_bar_position.x, back_bar_position.y, self.health, 5)
        pygame.draw.rect(screen, (142, 142, 142), back_bar_position)
        pygame.draw.rect(screen, (84, 223, 50), bar_position)

    def die(self, game) -> None:
        if random.randint(1, 2) == 1:
            self.rect.x = game.screen.get_width()
            self.direction = "left"
            self.image = self.initial_image
        else:
            self.rect.x = 0
            self.direction = "right"
            self.image = pygame.transform.flip(self.initial_image, True, False)
        self.health = self.max_health 
        self.velocity = random.randint(1, 5)
        if game.comet_event.full_loaded():
            game.monsters.remove(self)
            game.comet_event.try_fall("./assets/comet.png", game)

    def damage(self, damage: int, game) -> None:
        self.health -= damage
        if self.health <= 0:
            self.die(game)

    def __init__(self, image_path: str, position: Tuple[int, int], direction: str) -> None:
        super().__init__("mummy")
        self.direction: str = direction
        self.initial_image = self.image
        if direction == "right":
            self.image = pygame.transform.flip(self.image, True, False)
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = position
        self.max_health: int = 100
        self.health = self.max_health
        self.velocity: int = random.randint(1, 5)
        self.attack: float = 0.3
        


    