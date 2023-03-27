import pygame, sys
from scripts.entities.player import player

def handle_keydown(event):
    if event.key == pygame.K_ESCAPE:
        pygame.quit()
        sys.exit()
    elif event.key == pygame.K_d:
        player.direction.x = 1
    elif event.key == pygame.K_z:
        player.direction.y = -1
    elif event.key == pygame.K_q:
        player.direction.x = -1
    elif event.key == pygame.K_s:
        player.direction.y = 1
