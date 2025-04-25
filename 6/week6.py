from pycat.core import Sprite, Window, KeyCode, Color
import random
windows = Window()

select = []
letterlist = []

class Letter(Sprite):
    def on_create(self):
        self.scale = 0.3
        self.letter = ''
        self.goto_random_position()
        self.y = 320
    
    def on_update(self, dt):
        my_index = letterlist.index(self)
        self.x = my_index*100 +100
        if self== select:
            self.color = Color.ORANGE
        else:
            self.color = Color.WHITE

    def on_left_click(self):
        global select
        select = self
        print(self.letter)

mix_word ="GINGER"

for letter in mix_word:
    sprite = windows.create_sprite(Letter)
    sprite.letter = letter
    sprite.image = "Marble/letter_"+letter+".png"
    letterlist.append(sprite)

windows.run()