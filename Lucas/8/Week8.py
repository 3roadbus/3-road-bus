from pycat.core import Window, Label, Sprite, Point, KeyCode
windows = Window()

class time(Label):
    def on_create(self):
        self.text = '0'
        self.position = Point (650,500)
        self.is_running = False
        self.timer = 0
    
    def on_update(self, dt):
        if self.is_running:
            self.timer += dt
        self.text = str(round(self.timer,3))

time = windows.create_label(time)        

class start(Sprite):
    def on_create(self):
        self.image = 'start.png'
        self.position = Point(625,350)
    
    def on_left_click(self):
        if time.is_running:
            time.is_running = False
        else:
            time.is_running = True

        
class pause(Sprite):
    def on_create(self):
        self.image = 'pause.png'
        self.position = Point(750,350)
    
    def on_left_click(self):
        time.is_running = False
        time.timer = 0
        


windows.create_sprite(start)
windows.create_sprite(pause)
windows.run()