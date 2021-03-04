# -*- coding: utf-8 -*-
import pygame
from typing import Tuple, Dict
from models.background import Background
from models.player import Player
from models.monster import Alien, Mummy
from models.bannner import Banner
from models.button import Button
from models.comet_event import CometFallEvent


class Window:
    size: Tuple[int, int]
    title: str
    running: bool = True
    playing: bool = False
    screen: pygame.Surface
    background: Background
    banner: Banner
    button: Button
    player: Player
    comet_event: CometFallEvent = CometFallEvent()
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

    def set_player(self, initial_pos: Tuple[int, int]) -> None:
        self.player = Player(initial_pos)

    def add_mummy(self, position: Tuple[int, int], direction: str) -> None:
        self.monsters.add(Mummy(position, direction))

    def add_alien(self, position: Tuple[int, int], direction: str) -> None:
        self.monsters.add(Alien(position, direction))

    def set_banner(self, image_path: str, position: Tuple[int, int]) -> None:
        self.banner = Banner(image_path, position)

    def set_button(self, image_path: str, position: Tuple[int, int]) -> None:
        self.button = Button(image_path, position)

    def start(self) -> None:
        self.playing = True

    def stop(self) -> None:
        self.player.health = self.player.max_health
        self.playing = False
        self.comet_event.reset_percent()
        self.comet_event.comets = pygame.sprite.Group()
        for monster in self.monsters:
            monster.die(self)
        

    def collision(self, sprite1, sprite2) -> Dict[str, bool]:
        result: Dict[str, bool] = {"left": False, "right": False, "top": False, "bottom": False}
        collision = pygame.sprite.collide_mask(sprite1, sprite2)
        if collision:
            x: int = collision[0]
            width: int = sprite1.rect.width
            if x < width / 2:
                result["left"] = True
            elif x > width / 2:
                result["right"] = True
            y: int = collision[1]
            height: int = sprite1.rect.height
            if y < height / 2:
                result["top"] = True
            elif y > height / 2:
                result["bottom"] = True
        return result

    def update(self) -> None:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
                break
            if event.type == pygame.KEYDOWN:
                self.pressed[event.key] = True
                if event.key == pygame.K_RIGHT:
                    self.player.launch_projectile("./assets/projectile.png", "right")
                if event.key == pygame.K_LEFT:
                    self.player.launch_projectile("./assets/projectile.png", "left")
            elif event.type == pygame.KEYUP:
                self.pressed[event.key] = False

        if self.pressed.get(pygame.K_a):
            if self.player.rect.x > 0:
                move: bool = True
                for monster in self.monsters:
                    if self.collision(self.player, monster)["left"]:
                        move = False
                if move:
                    self.player.move_left()
        if self.pressed.get(pygame.K_d):
            if self.player.rect.x + self.player.rect.width < self.screen.get_width():
                move: bool = True
                for monster in self.monsters:
                    if self.collision(self.player, monster)["right"]:
                        move = False
                if move:
                    self.player.move_right()
        self.player.update_animation()
        self.player.load(self.screen)
        self.player.update_health_bar(self.screen)
        self.comet_event.update_percent(self.screen)
        for comet in self.comet_event.comets:
            comet.fall(self)
        self.comet_event.comets.draw(self.screen)
        for projectile in self.player.projectiles:
            projectile.move(self)
        self.player.projectiles.draw(self.screen)
        for monster in self.monsters:
            monster.update_animation()
            monster.forward(self)
            monster.update_health_bar(self.screen)
        self.monsters.draw(self.screen)

    def __init__(self, size: Tuple[int, int], title: str) -> None:
        self.set_size(size)
        self.set_title(title)