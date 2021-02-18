# -*- coding: utf-8 -*-
import pygame
from models.window import Window
pygame.init()

TITLE = "My First Game"
SIZE = (1080, 720)
BACKGROUND = "./assets/bg.jpg"
PLAYER = "./assets/player.png"
PROJECTILE = "./assets/projectile.png"

game = Window(SIZE, TITLE)
game.set_background(BACKGROUND, (0, -220))
game.set_player(PLAYER, (450, 500))

while game.running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game.running = False
            break
        if event.type == pygame.KEYDOWN:
            game.pressed[event.key] = True
            if event.key == pygame.K_RIGHT:
                game.player.launch_projectile(PROJECTILE, "right")
            if event.key == pygame.K_LEFT:
                game.player.launch_projectile(PROJECTILE, "left")
        elif event.type == pygame.KEYUP:
            game.pressed[event.key] = False

    if game.pressed.get(pygame.K_a):
        if game.player.rect.x > 0:
            game.player.move_left()
    if game.pressed.get(pygame.K_d):
        if game.player.rect.x + game.player.rect.width < game.screen.get_width():
            game.player.move_right()

    game.background.load(game.screen)
    game.player.load(game.screen)
    for projectile in game.player.projectiles:
        projectile.move(game.player, game.screen)
    game.player.projectiles.draw(game.screen)
    pygame.display.flip()

pygame.quit()