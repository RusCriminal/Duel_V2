from ursina import *

class BodyPart(Entity):
    def __init__(self, parent, name, model, scale, position, rotation, health=100, **kwargs):
        super().__init__(
            parent=parent,
            model=model,
            scale=scale,
            position=position,
            rotation=rotation,
            collider='box',
            **kwargs
        )
        self.name = name
        self.max_health = health
        self.health = health
        self.visible = False  # Скрываем базовую модель для использования кастомной

    def take_damage(self, amount):
        self.health = max(0, self.health - amount)
        print(f"{self.name} получил {amount} урона! Осталось здоровья: {self.health}")
        
        if self.health <= 0:
            self.disable()
            print(f"{self.name} уничтожен!")
