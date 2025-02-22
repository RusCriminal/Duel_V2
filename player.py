from ursina import *
from body_part import BodyPart
from weapon import Sword

class Player(Entity):
    def __init__(self):
        super().__init__(
            model='assets/player',
            scale=(1, 2, 1),
            position=(0, 2, 0)
        )
        
        # Инициализация частей тела
        self.body_parts = {
            'head': BodyPart(self, 'Голова', 'sphere', (0.8, 0.8, 0.8), (0, 1.5, 0), (0, 0, 0), health=50),
            'torso': BodyPart(self, 'Туловище', 'cube', (1, 2, 0.5), (0, 0.5, 0), (0, 0, 0)),
            'left_arm': BodyPart(self, 'Левая рука', 'cube', (0.4, 1.2, 0.4), (-0.7, 0.6, 0), (0, 0, -10)),
            'right_arm': BodyPart(self, 'Правая рука', 'cube', (0.4, 1.2, 0.4), (0.7, 0.6, 0), (0, 0, 10)),
            'legs': BodyPart(self, 'Ноги', 'cube', (0.8, 1.5, 0.6), (0, -1, 0), (0, 0, 0))
        }
        
        # Инициализация оружия
        self.sword = Sword(self.body_parts['right_arm'])
        self.sword.enabled = False  # Скрываем пока не нужно
        
        # Настройки управления
        self.attack_key = 'left mouse down'
        
    def input(self, key):
        if key == self.attack_key:
            self.attack()
            
    def attack(self):
        self.sword.attack()
        
    def update(self):
        # Проверка попаданий по частям тела
        if self.sword.is_attacking:
            for entity in self.sword.intersects().entities:
                if isinstance(entity, BodyPart) and entity != self.body_parts:
                    entity.take_damage(self.sword.damage)
