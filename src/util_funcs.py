import pygame

def programShouldExit():
    """Return a bool representing if the program should terminate"""
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            return True
    return False


