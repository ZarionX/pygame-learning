# -*- coding: utf-8 -*-
import pygame
from models.window import Window
pygame.init()

TITLE = "My First Game"
SIZE = (1080, 720)
BACKGROUND = "./assets/bg.jpg"
PLAYER = "./assets/player.png"

game = Window(SIZE, TITLE)
game.set_background(BACKGROUND, (0, -250))
game.set_player(PLAYER, (450, 500))

while game.running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game.running = False
            break
        if event.type == pygame.KEYDOWN:
            game.pressed[event.key] = True
        elif event.type == pygame.KEYUP:
            game.pressed[event.key] = False

    if game.pressed.get(pygame.K_LEFT):
        if game.player.rect.x > 0:
            game.player.move_left()
    elif game.pressed.get(pygame.K_RIGHT):
        if game.player.rect.x + game.player.rect.width < game.screen.get_width():
            game.player.move_right()

    game.background.load(game.screen)
    game.player.load(game.screen)
    pygame.display.flip()

pygame.quit()