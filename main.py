# -*- coding: utf-8 -*-
import pygame
import random

from pygame.constants import MOUSEBUTTONDOWN
from models.window import Window
pygame.init()

TITLE = "My First Game"
SIZE = (1080, 720)
BACKGROUND = "./assets/bg.jpg"
PLAYER = "./assets/player.png"
MUMMY = "./assets/mummy.png"
BANNER = "./assets/banner.png"
BUTTON = "./assets/button.png"

game = Window(SIZE, TITLE)
game.set_background(BACKGROUND, (0, -220))
game.set_banner(BANNER, (int(game.screen.get_width() / 4), 0))
game.set_button(BUTTON, (int(game.screen.get_width() / 3.33), int(game.screen.get_width() / 3)))
game.set_player(PLAYER, (450, 500))
for i in range(2):
    if random.randint(1, 2) == 1:
        game.add_monster(MUMMY, (game.screen.get_width(), 550), "left")
    else:
        game.add_monster(MUMMY, (0, 550), "right")

while game.running:
    game.background.load(game.screen)
    if game.playing:
        game.update()
    else:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game.running = False
                break
            if event.type == pygame.MOUSEBUTTONDOWN:
                if game.button.rect.collidepoint(event.pos):
                    game.start()
        game.button.load(game.screen)
        game.banner.load(game.screen)
    pygame.display.flip()

pygame.quit()