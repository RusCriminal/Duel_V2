from ursina import *
from settings import Settings

class Player(Entity):
    def __init__(self):
        super().__init__(
            model='assets/player',  # Создайте свою модель или используйте 'cube'
            texture='white_cube',
            scale=(1, 2, 1),
            collider='box',
            position=(0, 2, 0)
        )
        self.camera_pivot = Entity(parent=self)
        self.speed = Settings.MOVE_SPEED
        self.mouse_sensitivity = Settings.MOUSE_SENSITIVITY
        
        # Настройка камеры
        camera.parent = self.camera_pivot
        camera.position = (0, Settings.CAMERA_HEIGHT, -Settings.CAMERA_DISTANCE)
        camera.rotation = (0, 0, 0)
        camera.fov = 90
        
        mouse.locked = True
        self.target_rotation = 0
        
    def update(self):
        self.movement()
        self.camera_rotation()
        
    def movement(self):
        move_dir = Vec3(
            held_keys['d'] - held_keys['a'],
            0,
            held_keys['w'] - held_keys['s']
        ).normalized()
        
        self.position += move_dir * self.speed * time.dt
        
        # Ограничение движения по земле
        if self.y < 2:
            self.y = 2
            
    def camera_rotation(self):
        self.target_rotation += mouse.velocity[0] * self.mouse_sensitivity
        self.camera_pivot.rotation_y = self.target_rotation
        
        camera.rotation_x -= mouse.velocity[1] * self.mouse_sensitivity
        camera.rotation_x = clamp(camera.rotation_x, -30, 60)
