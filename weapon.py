from ursina import *

class Sword(Entity):
    def __init__(self, parent):
        super().__init__(
            parent=parent,
            model='cube',
            texture='sword_texture',
            scale=(0.3, 0.3, 1.5),
            rotation=(0, 0, 45),
            position=(0.5, -0.5, 0.5),
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
            self.animate_attack()

    def animate_attack(self):
        self.animate_rotation((0, 0, -45), duration=0.1)
        self.animate_rotation((0, 0, 45), duration=0.3, delay=0.1)
        
    def update(self):
        self.is_attacking = time.time() < self.last_attack + 0.2
