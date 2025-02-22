from ursina import *

class Sword(Entity):
    def __init__(self, parent):
        super().__init__(
            parent=parent,
            model='cube',
            color=color.gray,
            scale=(0.3, 0.3, 1.5),
            position=(0.7, 0.5, 0),  # Новая позиция
            rotation=(35, -10, 45),
            collider='box'
        )
        self.attack_cooldown = 0.5
        self.last_attack = 0
        self.damage = 25
        self.is_attacking = False

    def attack(self):
        if time.time() > self.last_attack + self.attack_cooldown:
            self.is_attacking = True
            self.last_attack = time.time()
            self.start_attack_animation()

    def start_attack_animation(self):
        self.animate_position(self.position + Vec3(0,0,1), duration=0.2)
        self.animate_rotation((35, -10, -45), duration=0.2)
        self.animate_rotation((35, -10, 45), duration=0.3, delay=0.2)

    def update(self):
        self.is_attacking = time.time() < self.last_attack + 0.3
