import pygame, sys
from scripts.events.event_handler import handle_event
from scripts.maths.vector2 import Vector2
from scripts.entities.player import Player

# setup
pygame.init()
pygame.display.init()
pygame.display.set_caption('pyweek 35')
screen = pygame.display.set_mode((0,0), pygame.FULLSCREEN)

player = Player(Vector2(50,50))
while True:
    # clear screen
    screen.fill((0,0,0))

    # event handler
    for event in pygame.event.get():
        handle_event(event)

    # update
    pygame.display.update()
