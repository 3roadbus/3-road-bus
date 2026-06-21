'meow'
from pycat.core import Window,Label
import pyglet
window = Window()
pyglet.font.add_file('highway.ttf')

class text(Label):
    def on_create(self):
        self.text = 'abc123'
        self.font = 'Highway Gothic Wide'
        self.font_size =45
        self.x = 320
        self.y =160
window.create_label(text)
window.run()