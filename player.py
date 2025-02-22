from ursina import *
from settings import Settings

class Player(Entity):
    def __init__(self):
        super().__init__(
            model='cube',
            texture='white_cube',
            scale=(1, 2, 1),
            collider='box',
            position=(0, 2, 0)
        )
        self.camera_pivot = Entity(parent=self)
        self.speed = Settings.MOVE_SPEED
        self.mouse_sensitivity = Settings.MOUSE_SENSITIVITY
        
        camera.parent = self.camera_pivot
        camera.position = (0, Settings.CAMERA_HEIGHT, -Settings.CAMERA_DISTANCE)
        camera.rotation = (0, 0, 0)
        camera.fov = 90
        
        mouse.locked = True
        self.mouse_traverse = False  # Для отладки

    def update(self):
        self.movement()
        self.camera_rotation()
        
        # Отслеживание позиции для отладки
        if self.mouse_traverse:
            print(f"Player rotation: {self.rotation_y}")
            print(f"Camera pivot rotation: {self.camera_pivot.rotation_x}")

    def movement(self):
        move_dir = Vec3(
            held_keys['d'] - held_keys['a'],
            0,
            held_keys['w'] - held_keys['s']
        ).normalized()
        
        self.position += self.forward * move_dir.z * self.speed * time.dt
        self.position += self.right * move_dir.x * self.speed * time.dt

    def camera_rotation(self):
        if mouse.locked:
            # Вращение персонажа по горизонтали
            self.rotation_y += mouse.velocity[0] * self.mouse_sensitivity * 100
            
            # Наклон камеры по вертикали
            self.camera_pivot.rotation_x -= mouse.velocity[1] * self.mouse_sensitivity * 100
            self.camera_pivot.rotation_x = clamp(self.camera_pivot.rotation_x, -60, 60)

    def input(self, key):
        if key == 'escape':
            mouse.locked = not mouse.locked
        if key == 't':  # Клавиша для отладки
            self.mouse_traverse = not self.mouse_traverse
