from scripts.maths.vector2 import Vector2
from scripts.entities.entity import Entity
from scripts.graphics.sprite_handler import load_spritesheet

idle_spritesheet = load_spritesheet('player/idle',1,4,fps=4)
run_spritesheet = load_spritesheet('player/run',1,6,fps=8)
class Player(Entity):
    def __init__(self, pos=Vector2(0,0), dims=Vector2(24,32), spritesheet=idle_spritesheet, vel=Vector2(0,0), speed=15):
        super().__init__(pos, dims, spritesheet, vel)
    
    def post_update(self):
        self.vel = self.direction.normalized()*self.speed
        print(self.vel, self.oldVel)
        if self.vel == Vector2.ZERO() and self.oldVel != Vector2.ZERO():
            idle_spritesheet.reset()  ;  player.spritesheet = idle_spritesheet
        elif self.vel != Vector2.ZERO() and self.oldVel == Vector2.ZERO():
            run_spritesheet.reset()  ; player.spritesheet = run_spritesheet
            

player = Player()