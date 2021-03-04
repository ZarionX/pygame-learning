# -*- coding: utf-8 -*-
import pygame


class SoundsManager:

    def __init__(self) -> None:
        self.sounds = {
            "click": pygame.mixer.Sound("./assets/sounds/click.wav"),
            "game_over": pygame.mixer.Sound("./assets/sounds/game_over.wav"),
            "meteorite": pygame.mixer.Sound("./assets/sounds/meteorite.wav"),
            "tir": pygame.mixer.Sound("./assets/sounds/tir.wav")
        }

    def play(self, name) -> None:
        self.sounds[name].play()