from pycat.core import Window, Sprite, KeyCode

window = Window()

class bus(Sprite):
    def on_create(self):
        self.image = 'tnbuso13.jpg'
        self.x=0
        self.y = 100
        self.scale = 0.2
    
    def on_update(self, dt):
        self.x += 3

class italy(Sprite):
    def on_create(self):
        self.image = 'italyball.png'
        self.x=0
        self.y = 500
        self.scale = 0.25
    
    def on_update(self, dt):
        if self.window.is_key_down(KeyCode.SPACE):
            self.x += 25

window.create_sprite(bus)
window.create_sprite(italy)
window.run()

