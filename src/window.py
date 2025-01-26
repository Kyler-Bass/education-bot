from tkinter import Image
import pygame 
from pygame import draw 
from src.Entity import Entity, CircleEntity, RectEntity, ImageEntity, TextEntity

class Window:
    def __init__(self, size: tuple[int, int], fontSize:int):
        
        # Init 
        pygame.init()
        pygame.font.init()

        # Set members 
        self.size = size
        self.background_color = (255,179,81)
        self.mode = "none"
        self.running = True
        self.state : int = 0
        self.entities: dict[str, ImageEntity | TextEntity | CircleEntity | RectEntity] = {}

        # Create window 
        self.window = pygame.display
        self.display = self.window.set_mode(self.size)


    def updateScreen(self, mouse_clicked, mouse_pos) -> None:
        """Updates back buffer and flips front and back buffers"""

        # Change state if clicked on start button
        if (self.state == 0 and mouse_clicked[0] and self.entities.get('start_button',None) != None): 
            if (self.entities.get("start_button").imageRect.collidepoint(mouse_pos)): # type: ignore
                self.state = 1
                self.entities.clear()
                return

        if (self.state == 1 and mouse_clicked[0] and self.entities.get('history_button',None) != None):
            for button in ["history_button", "science_button", "math_button", "english_button"]:
                button_obj = self.entities.get(button)
                if (button_obj.imageRect.collidepoint(mouse_pos)): # type: ignore
                    self.state = 2
                    self.entities.clear()
                    self.mode = button # type: ignore
                    return


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
        elif type == "text":
            entity = TextEntity(**kwargs)
        else:
            raise ValueError("Entity type can only be: circle | rect | image")

        self.entities[name] = entity


    def removeEntity(self, name: str):
        self.entities.pop(name)


    def displayStartMenu(self):

        # Fill buffer with black to clear last frame 
        self.display.fill(self.background_color)
        self.addEntity("title", "text", {"fontStr": "Arial", "text": "Educator", "fontSize": 40, "pos": (230,100)})
        self.addEntity("start_button", "image", {"size": (160,80), "image_path": "images/start_button.png", "pos": [220,600]})


    def chooseMode(self):
        self.display.fill(self.background_color)
        self.addEntity("history_button", "image", {"size": (160,80), "image_path": "images/history_button.png", "pos": [220,200]})
        self.addEntity("science_button", "image", {"size": (160,80), "image_path": "images/science_button.png", "pos": [220,300]})
        self.addEntity("math_button", "image", {"size": (160,80), "image_path": "images/math_button.png", "pos": [220,400]})
        self.addEntity("english_button", "image", {"size": (160,80), "image_path": "images/english_button.png", "pos": [220,500]})


    def displayGame(self):
        self.display.fill(self.background_color)
        self.addEntity("A_button", "circle", {"radius": 20, "pos": [50,250], "color": (255,255,255)})
        self.addEntity("B_button", "circle", {"radius": 20, "pos": [50,350], "color": (255,255,255)})
        self.addEntity("C_button", "circle", {"radius": 20, "pos": [50,450], "color": (255,255,255)})
        self.addEntity("D_button", "circle", {"radius": 20, "pos": [50,550], "color": (255,255,255)})

        self.addEntity("A_button_border", "circle", {"radius": 20, "pos": [50,250], "color": (0,0,0), "width": 2})
        self.addEntity("B_button_border", "circle", {"radius": 20, "pos": [50,350], "color": (0,0,0), "width": 2})
        self.addEntity("C_button_border", "circle", {"radius": 20, "pos": [50,450], "color": (0,0,0), "width": 2})
        self.addEntity("D_button_border", "circle", {"radius": 20, "pos": [50,550], "color": (0,0,0), "width": 2})

        self.addEntity("A_button_label", "text", {"pos": [42,232], "text": "A", "fontStr": "Arial", "fontSize": 30})
        self.addEntity("B_button_label", "text", {"pos": [42,332], "text": "B", "fontStr": "Arial", "fontSize": 30})
        self.addEntity("C_button_label", "text", {"pos": [42,432], "text": "C", "fontStr": "Arial", "fontSize": 30})
        self.addEntity("D_button_label", "text", {"pos": [42,532], "text": "D", "fontStr": "Arial", "fontSize": 30})

        self.addEntity("A_text", "text", {"pos": [100,250], "text": "TEsting testing", "fontStr": "Arial", "fontSize": 40})
        self.addEntity("B_text", "text", {"pos": [100,350], "text": "TEsting testing", "fontStr": "Arial", "fontSize": 40})
        self.addEntity("C_text", "text", {"pos": [100,450], "text": "TEsting testing", "fontStr": "Arial", "fontSize": 40})
        self.addEntity("D_text", "text", {"pos": [100,550], "text": "TEsting testing", "fontStr": "Arial", "fontSize": 40})
