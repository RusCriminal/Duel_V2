from ursina import *
from player import Player
from world import World

app = Ursina()

# Создание мира
world = World()

# Создание игрока
player = Player()

# Настройка освещения
DirectionalLight(parent=player, direction=Vec3(1, -1, 1), color=color.white)

def update():
    pass  # Общая логика игры

def input(key):
    if key == 'escape':
        application.quit()

app.run()
