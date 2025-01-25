import pygame 



class Entity:
    def __init__(self, size: tuple[int,int]):
        """Entity_size starts from the top left of the entity\n
        """
        self.size = size
        self.surface : pygame.Surface


class ImageEntity(Entity):
    def __init__(self, size: tuple[int,int], image_path: str):
        super().__init__(size)
        self.surface = pygame.image.load(image_path).convert_alpha()


class CircleEntity(Entity):
    def __init__(self, size: tuple[int,int], radius: int, pos: list[int]):
        super().__init__(size)
        self.radius = radius 
        self.pos = pos
