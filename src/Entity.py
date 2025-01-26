import pygame
import pygame.draw as draw



class Entity:
    def render(self, display: pygame.Surface):
        pass


class ImageEntity(Entity):
    def __init__(self, size: tuple[int,int], image_path: str, pos: tuple[int, int]):
        self.size = size 
        self.surface = pygame.image.load(image_path).convert_alpha()
        self.imageRect = self.surface.get_rect()
        self.imageRect.topleft = pos


    def render(self, display: pygame.Surface):
        display.blit(self.surface, self.imageRect)


class RectEntity(Entity):
    def __init__(self, size: tuple[int,int], pos: list[int], color: tuple[int,int,int]):
        """
        size: (width, height)
        """
        self.size = size 
        self.pos = pos
        self.topleft = pos
        self.color = color 
        self.rect = pygame.Rect(pos[0], pos[1], size[0], size[1])
    
    def render(self, display: pygame.Surface):
        draw.rect(display, self.color, self.rect)


class CircleEntity(Entity):
    def __init__(self, radius: int, pos: list[int], color: tuple[int,int,int], width: int = 0):
        """
        pos: center of the circle
        """
        self.radius = radius 
        self.pos = pos
        self.color = color 
        self.width = width

    def render(self, display: pygame.Surface):
        draw.circle(display, self.color, self.pos, self.radius, self.width)


class TextEntity(Entity):
    def __init__(self, fontStr:str, fontSize:int, text:str, pos: list[int]):
        self.font = pygame.font.SysFont(fontStr, fontSize)
        self.textSurface = self.font.render(text, 0, (0,0,0))
        self.pos = pos
        self.text = text

    def reRenderText(self, newStr:str):
        self.textSurface = self.font.render(newStr, 0, (0,0,0))

    def render(self, display: pygame.Surface):
        display.blit(self.textSurface, self.pos)