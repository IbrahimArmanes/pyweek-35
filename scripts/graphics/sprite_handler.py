from pygame import image, transform
from scripts.graphics.spritesheet import Spritesheet

def load_sprite(path):
    '''
    Load a single sprite from game folder
    '''
    sprite = image.load(f'././sprites/{path}.png') 
    return transform.scale(sprite, (sprite.get_width()*2,sprite.get_height()*2))

def load_spritesheet(path, first_index, last_index, fps):
    '''
    Load multiple sprites in a list (used for animates)
    first_index : first frame index
    last_index : last frame index (inclusive)
    '''
    return Spritesheet([load_sprite(path+'/'+str(i)) for i in range(first_index, last_index+1)], fps=fps)