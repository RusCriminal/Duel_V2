from ursina import *
from settings import Settings

class World(Entity):
    def __init__(self):
        super().__init__()
        self.ground = Entity(
            model='plane',
            texture='grass',
            scale=Settings.GROUND_SIZE,
            collider='box'
        )
        
        # Пример объекта в мире
        self.cube = Entity(
            model='cube', 
            texture='white_cube',
            scale=(2,1,2),
            position=(3,0.5,3),
            collider='box'
        )
