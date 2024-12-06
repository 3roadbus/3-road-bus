from pycat.core import Window, Sprite, Point, KeyCode
windows = Window()

class player(Sprite):
    def on_create(self):
        self.position = Point (1200, 300)
        self.image = 'taiwan.jpg'
        self.scale = 0.25

    def on_update(self, dt):
        if self.window.is_key_pressed(KeyCode.UP ):
            self.y += 5
        if self.window.is_key_pressed(KeyCode.DOWN ):
            self.y -= 5

windows.create_sprite(player)
windows.run()