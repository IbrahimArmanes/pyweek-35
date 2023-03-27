import pygame
from scripts.maths.vector2 import Vector2

class Entity:
    def __init__(self, pos, dims, spritesheet, vel=Vector2(0,0), speed=5): # class to be expanded later
        self.pos = pos
        self.oldVel = Vector2(0,0)
        self.vel = vel
        self.speed = speed
        self.direction = Vector2(0,0)

        self.width = dims.x
        self.height = dims.y
        self.spritesheet = spritesheet
    
    def update(self):
        self.pos += self.vel
        self.spritesheet.update()
        if self.direction.x > 0:
            self.spritesheet.reversed = False
        elif self.direction.x < 0:
            self.spritesheet.reversed = True

        self.post_update()
        self.oldVel = self.vel
        
    def post_update(self): pass

    def get_rect(self):
        return pygame.Rect(self.pos.x, self.pos.y, self.width, self.height)
    
    def draw(self,screen):
        self.spritesheet.draw(screen, self.pos.toTuple())