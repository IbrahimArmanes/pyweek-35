import pygame, sys

def handle_keydown(event):
    if event.key == pygame.K_ESCAPE:
        pygame.quit()
        sys.exit()
