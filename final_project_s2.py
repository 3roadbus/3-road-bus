from pycat.core import Window, Sprite, Point, Scheduler, Label
import random
windows = Window()
Screen_change = 1
hitblock_move = [Point(1080,440),
                 Point(200,440),
                 Point(200,200),
                 Point(1080,200)
                                ]
#1080, 440
if Screen_change == 1:#menu part

    class title(Label):
        def on_create(self):
            self.text = "Mathing to Winning!"
            self.font_size = 5
            self.position = Point(640,480)

        def on_update(self, dt):
            self.rotation
    class fly_dec (Sprite):
        def on_create(self):
            self.image='tra.png'
            self.goto_random_position()
            self.scale = 0.5
            self.speed = 15
            self.rotation= 0

        def on_update(self, dt):
            self.move_forward(self.speed)
            if self.is_touching_window_edge():
                changing = random.randint(105,255)
                self.rotation += changing
            if not Screen_change == 1:
                self.delete()

    class Hitblock(Sprite):
        def on_create(self):
            self.scale = 5
            self.position=Point(1080,440)
            self.index = 0

        def on_update(self, dt):
            target = hitblock_move[self.index]
            self.point_toward(target)
            self.move_forward(10)
            if self.distance_to(target) < 10:
                if self.index >= 3:
                    self.index = 0
                else:
                    self.index += 1
            if not Screen_change == 1:
                self.delete()

    hitblock = windows.create_sprite(Hitblock)

    class ftcc(Sprite):
        def on_create(self):
            self.image ='FTCC.png'
            self.scale = 0.5
            self.position=Point(1080,440)
            self.rotation =0

        def on_update(self, dt):
            self.position = hitblock.position
            self.rotation += 5
            if not Screen_change == 1:
                self.delete()

    class play(Sprite):
        def on_create(self):
            self.scale = 3
            self.image = 'costume1.png'
            self.position=Point(640,320)

        def on_click(self, mouse_event):
            global Screen_change
            Screen_change = 2
            if not Screen_change == 1:
                self.delete()

    windows.create_sprite(play)

elif Screen_change==2:# difficulty choosing part
    class Easy(Sprite):
        def on_create(self):
            self.image = 'easy.png'
            self.scale = 4
            self.position = Point(320, 480)
        
        def on_left_click(self):
            global Screen_change
            Screen_change = 3

        def on_update(self, dt):
            if not Screen_change == 2:
                self.delete()

    class Mid(Sprite):
        def on_create(self):
            self.image = 'med.png'
            self.scale = 4
            self.position = Point(640, 480)
        
        def on_update(self, dt):
            if not Screen_change == 2:
                self.delete()

        def on_left_click(self):
            global Screen_change
            Screen_change = 3

    class Hard(Sprite):
        def on_create(self):
            self.image = 'hard.png'
            self.scale = 4
            self.position = Point(960, 480)
        
        def on_left_click(self):
            global Screen_change
            Screen_change = 3

        def on_update(self, dt):
            if not Screen_change == 2:
                self.delete()

    class EX(Sprite):
        def on_create(self):
            self.image = 'ex.png'
            self.scale = 4
            self.position = Point(320, 160)
        
        def on_left_click(self):
            global Screen_change
            Screen_change = 3

        def on_update(self, dt):
            if not Screen_change == 2:
                self.delete()

    class devil(Sprite):
        def on_create(self):
            self.image = 'devil.png'
            self.scale = 4
            self.position = Point(960, 160)
        
        def on_left_click(self):
            global Screen_change
            Screen_change = 3

        def on_update(self, dt):
            if not Screen_change == 2:
                self.delete()

    class random(Sprite):
        def on_create(self):
            self.image = 'random.png'
            self.scale = 4
            self.position = Point(640, 160)
        
        def on_left_click(self):
            global Screen_change
            Screen_change = 3

        def on_update(self, dt):
            if not Screen_change == 2:
                self.delete()

windows.create_sprite(ftcc)
for _ in range(20):
    windows.create_sprite(fly_dec)
windows.run()