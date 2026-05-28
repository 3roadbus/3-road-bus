from pycat.core import Window, Sprite, Label, Color,Scheduler,KeyCode
import random

windows = Window(height=1280,width=2560)

speed = 0

class tram_for_drive(Sprite):

    def on_create(self):
        self.image='lrt.png'
        #self.x=-1500
        self.y=550
        self.layer =1
    
    def on_update(self, dt):
         #change later
        global speed
        if windows.is_key_pressed(KeyCode.NUM_0):
            if speed<=70:
                speed += 0.25
            
        elif windows.is_key_pressed(KeyCode.NUM_1):
            if speed>5:
                speed = speed * 0.9955
            else:
                speed = speed *0.97
        else:
            speed= speed * 0.99898
        
        if speed <0.249:
             speed = 0

class floor(Sprite):
    def on_create(self):
        self.image='floor.png'
        self.scale=2
        self.x= 1280
        self.color=Color(random.randint(1,255),random.randint(1,255),random.randint(1,255))

    def the_building_respawn(self):
        for i in range(random.randint(1,5)):
            windows.create_sprite(floor,y=350+i*173,x=2560)
        self.delete()

    def on_update(self, dt):
        global speed
        if self.x<25:
            self.the_building_respawn()
        else:
            self.x-=speed

def opening_of_buildings():
    for i in range(8):
        X=i*363
        for i in range(random.randint(1,5)):
            windows.create_sprite(floor,y=350+i*173,x=X)
 
opening_of_buildings()

windows.create_sprite(tram_for_drive)
windows.run()