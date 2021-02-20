# -*- coding: utf-8 -*-
import pygame
from models.window import Window
pygame.init()

TITLE = "My First Game"
SIZE = (1080, 720)
BACKGROUND = "./assets/bg.jpg"
PLAYER = "./assets/player.png"
PROJECTILE = "./assets/projectile.png"
MUMMY = "./assets/mummy.png"

game = Window(SIZE, TITLE)
game.set_background(BACKGROUND, (0, -220))
game.set_player(PLAYER, (450, 500))
game.add_monster(MUMMY, (game.screen.get_width(), 550), "left")

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
            move: bool = True
            for monster in game.monsters:
                if game.collision(game.player, monster)["left"]:
                    move = False
            if move:
                game.player.move_left()
    if game.pressed.get(pygame.K_d):
        if game.player.rect.x + game.player.rect.width < game.screen.get_width():
            move: bool = True
            for monster in game.monsters:
                if game.collision(game.player, monster)["right"]:
                    move = False
            if move:
                game.player.move_right()

    game.background.load(game.screen)
    game.player.load(game.screen)
    for projectile in game.player.projectiles:
        projectile.move(game)
    game.player.projectiles.draw(game.screen)
    for monster in game.monsters:
        monster.forward(game.player)
    game.monsters.draw(game.screen)
    pygame.display.flip()

pygame.quit()