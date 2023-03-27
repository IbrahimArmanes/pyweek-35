from pygame import transform

class Spritesheet:
    def __init__(self, sprites, fps=60, reversed=False):
        self.sprites = sprites       # list of pygame images
        self.reversed_sprites = [transform.flip(sprite, True, False) for sprite in self.sprites]
        self.reversed = reversed
        
        self.frame = 0
        self.maxFrame = len(sprites)-1
        self.fps = fps                # at how much fps does the sprite update (1s=60frames)
        self.frame_count = 0

    def update(self):
        if self.fps > 0:
            self.frame_count += 1
            if self.frame_count >= 60/self.fps:
                self.set_next_frame()
                self.frame_count = 0

    def set_next_frame(self):
        self.frame += 1
        if self.frame > self.maxFrame:
            self.frame = 0
    
    def reset(self):
        self.frame = 0
    
    def draw(self, screen, pos):
        screen.blit(self.reversed_sprites[self.frame] if self.reversed else self.sprites[self.frame] , list(pos))