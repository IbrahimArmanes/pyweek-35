import pygame
from scripts.maths import Vector2

class Entity:
    def __init__(self, pos, dims, vel=Vector2(0,0)): # class to be expanded later
        self.pos = pos
        self.vel = vel
        self.width = dims.x
        self.height = dims.y
    
    def update(self):
        self.pos += self.vel
    
    def draw(self,screen):
        pygame.draw.rect(screen, (255,255,255), pygame.Rect(self.pos.x, self.pos.y, self.width, self.height))