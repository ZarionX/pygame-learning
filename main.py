# -*- coding: utf-8 -*-
import pygame
import random
from models.window import Window
pygame.init()
pygame.mixer.pre_init(44100, 16, 2, 4096)

TITLE = "My First Game"
SIZE = (1080, 720)
BACKGROUND = "./assets/bg.jpg"
PLAYER = "./assets/player.png"
MUMMY = "./assets/mummy.png"
BANNER = "./assets/banner.png"
BUTTON = "./assets/button.png"
FPS = 30
clock = pygame.time.Clock()

game = Window(SIZE, TITLE)
game.set_background(BACKGROUND, (0, -220))
game.set_banner(BANNER, (int(game.screen.get_width() / 4), 0))
game.set_button(BUTTON, (int(game.screen.get_width() / 3.33), int(game.screen.get_width() / 3)))
game.set_player((450, 500))
for i in range(2):
    if random.randint(1, 2) == 1:
        game.add_mummy((game.screen.get_width(), 550), "left")
    else:
        game.add_mummy((0, 550), "right")
    
if random.randint(1, 2) == 1:
    game.add_alien((game.screen.get_width(), 400), "left")
else:
    game.add_alien((0, 400), "right")

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
                    game.sounds.play("click")
                    game.start()
        game.button.load(game.screen)
        game.banner.load(game.screen)
    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()