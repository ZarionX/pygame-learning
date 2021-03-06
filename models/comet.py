# -*- coding: utf-8 -*-
import pygame
import random


class Comet(pygame.sprite.Sprite):
    image: pygame.Surface
    rect: pygame.Rect

    def convert(self, image_path: str) -> None:
        self.image = pygame.image.load(image_path)
        self.rect = self.image.get_rect()

    def remove(self, game) -> None:
        game.sounds.play("meteorite")
        game.comet_event.comets.remove(self)

    def fall(self, game) -> None:
        self.rect.y += self.velocity
        if self.rect.y >= game.screen.get_height() - self.rect.height:
            self.remove(game)
        if True in game.collision(game.player, self).values():
            game.collision(game.player, self)
            self.remove(game)
            game.player.damage(self.attack, game)
        if len(game.comet_event.comets) == 0:
            game.comet_event.falling = False
            game.comet_event.reset_percent()
            for i in range(2):
                if random.randint(1, 2) == 1:
                    game.add_mummy((game.screen.get_width(), 550), "left")
                else:
                    game.add_mummy((0, 550), "right")
            if random.randint(1, 2) == 1:
                game.add_alien((game.screen.get_width(), 400), "left")
            else:
                game.add_alien((0, 400), "right")

    def __init__(self, image_path: str, screen: pygame.Surface) -> None:
        super().__init__()
        self.convert(image_path)
        self.rect.x = random.randint(0, screen.get_width() - self.rect.width)
        self.rect.y = random.randint(-800, 0)
        self.velocity = random.randint(3, 7)
        self.attack = 20