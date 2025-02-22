from ursina import *
from player import Player
from world import World

app = Ursina()

world = World()
player = Player()

# Включение отладки коллизий
window.collider_visible = True

def update():
    pass

app.run()
