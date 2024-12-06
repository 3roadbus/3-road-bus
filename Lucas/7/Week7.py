from pydoc import pager
from pycat.core import Window, Sprite

window = Window(background_image = 'nice.png')

class bus(Sprite):
    def on_create(player):
        player.image = 'bus.png'
        player.y = 50
        player.x = 1300
    
    def on_update(self, dt):
        self.x -= 12
        if self.x <= 0:
            self.x = 1300

class passengers(Sprite):
    def on_create(player):
        player.image = 'japanball.png'
        player.y = 200
        player.x = 1300

window.create_sprite(bus, passengers)
window.run()