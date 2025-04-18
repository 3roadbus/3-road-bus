from tkinter import Label
from pycat.core import Window, Sprite, Point
import random
hp = 100
windows = Window(draw_sprite_rects= True)
Limited = []


class idk1(Sprite):
        def on_create(self):
                self.opacity = 0
                self.animation = False
                
        def on_update(self, dt):
                if not self.animation == True:
                        return
                
                
                self.opacity-=10
                self.rotation += 15
                self.scale = self.scale * 0.75
                if self.scale >0.1:
                        return
                self.delete()
                        
        def on_left_click(self):
                if self not in Limited and len(Limited)<2 :
                        Limited.append(self)
                        self.opacity = 255

picture = ['ccc.png','fin.png','ger.png','pol.png']*4
random.shuffle(picture)
for x in range(1, 5):
        for y in range(1, 5):
                windows.create_sprite(idk1, x= x*110, y=y*110,image = picture.pop())

class check(Sprite):
        def on_create(self):
                self.position = Point(1000,320)
                self.image = 'CHECK.png'
                self.animation = False
                self.label = windows.create_label(text = str(hp))

        def on_update(self, dt):
                self.label.text = str(hp)
                if hp < 0:
                        windows.delete()

        

        def on_left_click(self):
                global hp
                if Limited[0].image==Limited[1].image:
                        Limited[0].animation = True
                        Limited[1].animation = True 
                        hp += 10
                else:
                        Limited[0].opacity = 0
                        Limited[1].opacity = 0
                        hp -=10

                Limited.clear()

windows.create_sprite(check)
windows.run()