import pygame
import pygame.draw as draw



class Entity:
    def render(self, display: pygame.Surface):
        pass


class ImageEntity(Entity):
    def __init__(self, size: tuple[int,int], image_path: str, pos: list[int]):
        self.size = size 
        self.pos = pos 
        self.surface = pygame.image.load(image_path).convert_alpha()

    def render(self, display: pygame.Surface):
        pass


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
    def __init__(self, radius: int, pos: list[int], color: tuple[int,int,int]):
        """
        pos: center of the circle
        """
        self.radius = radius 
        self.pos = pos
        self.color = color 

    def render(self, display: pygame.Surface):
        draw.circle(display, self.color, self.pos, self.radius)
