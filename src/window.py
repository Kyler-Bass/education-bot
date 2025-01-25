import pygame 
from pygame import draw 
from src.Entity import Entity 


class Window:
    def __init__(self, size: tuple[int, int]):
        
        # Set members 
        self.size = size
        self.entities: list[Entity] = []

        # Init pygame and create window 
        pygame.init()
        self.window = pygame.display
        self.display = self.window.set_mode(self.size)
    
        


    def updateScreen(self) -> None:
        """Updates back buffer and flips front and back buffers"""

        # Update back buffer with what's going on 
        # Fill buffer with black to clear last frame 
        self.display.fill((0,0,0))

        # Cycle through entities and add them to the screen 
        for entity in self.entities:
            pass
        
        

        # Flip front and back buffers 
        self.window.flip()