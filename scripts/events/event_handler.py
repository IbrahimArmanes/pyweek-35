import pygame, sys
from scripts.events.keydown import handle_keydown
from scripts.events.keyup import handle_keyup
from scripts.events.mousedown import handle_mousedown
from scripts.events.mouseup import handle_mouseup

def shutdown():
    pygame.quit()
    sys.exit()

events_dic = {pygame.QUIT:            shutdown,       # which function is called depending on the event type
              pygame.KEYDOWN:         handle_keydown,
              pygame.KEYUP:           handle_keyup,
              pygame.MOUSEBUTTONDOWN: handle_mousedown,
              pygame.MOUSEBUTTONUP:   handle_mouseup}

def handle_event(event):                      # call corresponding function
    if event.type in events_dic.keys():
        events_dic[event.type](event) 
