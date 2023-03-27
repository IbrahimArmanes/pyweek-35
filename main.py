import pygame, sys
from scripts.events.event_handler import handle_event
from scripts.entities.player import player

# constants
MAX_FPS = 60

# setup
pygame.init()
pygame.display.init()
pygame.display.set_caption('pyweek 35')
screen = pygame.display.set_mode((0,0), pygame.FULLSCREEN)
clock = pygame.time.Clock()

while True:
    # clear screen
    screen.fill((0,0,0))

    # instance updates
    player.update()

    # event handler
    for event in pygame.event.get():
        handle_event(event)

    # drawing
    player.draw(screen)

    # update
    pygame.display.update()
    clock.tick(MAX_FPS)
