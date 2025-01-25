import pygame 
from pygame import draw 
from src.Entity import Entity, CircleEntity, RectEntity, ImageEntity

class Window:
    def __init__(self, size: tuple[int, int], fontSize:int):
        
        # Init 
        pygame.init()
        pygame.font.init()

        # Set members 
        self.size = size
        self.running = True
        self.state : int = 0
        self.entities: dict[str,Entity] = {}
        self.font = pygame.font.SysFont('Arial', fontSize)

        # Create window 
        self.window = pygame.display
        self.display = self.window.set_mode(self.size)


    def updateScreen(self) -> None:
        """Updates back buffer and flips front and back buffers"""

        # Update back buffer with what's going on 
        # Fill buffer with black to clear last frame 
        self.display.fill((0,0,0))

        # Cycle through entities and add them to the screen 
        
        for entity in self.entities.values():
            entity.render(self.display)
        
        

        # Flip front and back buffers 
        self.window.flip()


    def addEntity(self, name: str, type: str, kwargs: dict):
        """Args are different for each entity. 
        """

        # Skip adding entity if it already exists 
        if self.entities.get(name, None) != None:
            return 
        
        if type == "circle":
            entity = CircleEntity(**kwargs)
        elif type == "rect":
            entity = RectEntity(**kwargs)
        elif type == "image":
            entity = ImageEntity(**kwargs)
        else:
            raise ValueError("Entity type can only be: circle | rect | image")

        self.entities[name] = entity

    def removeEntity(self):
        pass

    def displayStartMenu(self):
        self.addEntity("c1", "circle", {"radius": 10, "pos": [100,100], "color": (255,0,0)})
        self.addEntity("c2", "circle", {"radius": 10, "pos": [120,100], "color": (255,0,255)})
        self.addEntity("c3", "circle", {"radius": 10, "pos": [140,100], "color": (0,0,255)})
        self.addEntity("c4", "circle", {"radius": 10, "pos": [160,100], "color": (5,255,0)})
        self.addEntity("r1", "rect", {"size": [100,10], "pos": [100,130], "color": (0,255,0)})