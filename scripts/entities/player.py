from scripts.maths import Vector2
from scripts.entities.entity import Entity

class Player(Entity):
    def __init__(self, pos, vel=Vector2(0,0)):
        super().__init__(pos, vel)