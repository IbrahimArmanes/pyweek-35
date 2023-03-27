import pygame
from scripts.entities.player import player

def handle_keyup(event):
    if event.key == pygame.K_d and player.direction.x==1:
        player.direction.x = 0
    elif event.key == pygame.K_z and player.direction.y==-1:
        player.direction.y = 0
    elif event.key == pygame.K_q and player.direction.x==-1:
        player.direction.x = 0
    elif event.key == pygame.K_s and player.direction.y==1:
        player.direction.y = 0