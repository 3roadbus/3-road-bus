from pycat.core import Window, Sprite, Point, Scheduler
import random
windows = Window()
Screen_change = 1
hitblock_move = [Point(1080,440),
                 Point(200,440),
                 Point(200,200),
                 Point(1080,200)
                                ]
#1080, 440
if Screen_change == 1:

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
                if self.index >= 4:
                    self.index = 0
                else:
                    self.index += 1

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




windows.create_sprite(ftcc)
for _ in range(20):
    windows.create_sprite(fly_dec)
windows.run()