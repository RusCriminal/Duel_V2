from ursina import *
from body_part import BodyPart
from weapon import Sword

class Player(Entity):
    def __init__(self):
        super().__init__(
            model=None,  # Убираем стандартную модель
            scale=(1, 1, 1),
            position=(0, 2, 0),
            collider='box'
        )
        
        # Создаем визуальные компоненты
        self.model_parent = Entity(parent=self)  # Для вращения модели отдельно от коллайдера
        
        # Инициализация частей тела с видимыми моделями
        self.body_parts = {
            'head': BodyPart(self.model_parent, 'Голова', 'sphere', 
                           (0.8, 0.8, 0.8), (0, 1.5, 0), (0, 0, 0), health=50),
            'torso': BodyPart(self.model_parent, 'Туловище', 'cube', 
                            (1, 2, 0.5), (0, 0.5, 0), (0, 0, 0)),
            'left_arm': BodyPart(self.model_parent, 'Левая рука', 'cube', 
                               (0.4, 1.2, 0.4), (-0.7, 0.6, 0), (0, 0, -10)),
            'right_arm': BodyPart(self.model_parent, 'Правая рука', 'cube', 
                                (0.4, 1.2, 0.4), (0.7, 0.6, 0), (0, 0, 10)),
            'legs': BodyPart(self.model_parent, 'Ноги', 'cube', 
                           (0.8, 1.5, 0.6), (0, -1, 0), (0, 0, 0))
        }
        
        # Настройка материалов
        for part in self.body_parts.values():
            part.color = color.random_color()
            
        # Инициализация оружия
        self.sword = Sword(self.body_parts['right_arm'])
        
        # Настройки камеры
        self.camera_pivot = Entity(parent=self)
        camera.parent = self.camera_pivot
        camera.position = (0, 5, -8)
        camera.rotation = (15, 0, 0)
        
        # Настройки управления
        self.speed = 5
        self.mouse_sensitivity = 0.1
        mouse.locked = True

    def update(self):
        self.movement()
        self.camera_rotation()
        
    def movement(self):
        move_dir = Vec3(
            held_keys['d'] - held_keys['a'],
            0,
            held_keys['w'] - held_keys['s']
        ).normalized()
        
        self.position += self.forward * move_dir.z * self.speed * time.dt
        self.position += self.right * move_dir.x * self.speed * time.dt
        self.y = max(self.y, 2)  # Фиксируем высоту

    def camera_rotation(self):
        if mouse.locked:
            self.rotation_y += mouse.velocity[0] * self.mouse_sensitivity * 100
            self.camera_pivot.rotation_x -= mouse.velocity[1] * self.mouse_sensitivity * 100
            self.camera_pivot.rotation_x = clamp(self.camera_pivot.rotation_x, -60, 60)

    def input(self, key):
        if key == 'left mouse down':
            self.sword.attack()
        if key == 'escape':
            mouse.locked = not mouse.locked
