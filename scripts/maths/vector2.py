from math import sqrt
class Vector2:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def normalized(self):
        if (self.x, self.y) == (0,0): 
            return self
        else:
            length = sqrt(self.x**2 + self.y**2)
            return Vector2(self.x/length, self.y/length)
    
    def ZERO(self=None):
        return Vector2(0,0)
    
    def __add__(self, vec2): # how to add two Vector2 instances
        assert type(vec2) == Vector2, "Type Vector2 can only be added to : 'Vector2'"
        return Vector2(self.x+vec2.x, self.y+vec2.y)