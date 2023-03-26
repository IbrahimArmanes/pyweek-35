import pygame, sys
from scripts.events.keydown import handle_keydown
from scripts.events.keyup import handle_keyup

def shutdown():
    pygame.quit()
    sys.exit()

events_dic = {pygame.QUIT:    shutdown,       # which function is called depending on the event type
              pygame.KEYDOWN: handle_keydown,
              pygame.KEYUP:   handle_keyup}

def handle_event(event):                      # call corresponding function
    if event.type in events_dic.keys():
        events_dic[event.type]() 