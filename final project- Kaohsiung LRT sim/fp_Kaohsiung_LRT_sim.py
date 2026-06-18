from pycat.core import Window, Sprite, Label, Color,Scheduler
import random

windows = Window(height=1280,width=2560)
class tram_for_drive(Sprite):
    def on_create(self):
        self.image='lrt.png'
        #self.x=-1500
        self.y=640
        self.layer =1
    
class floor(Sprite):
    def on_create(self):
        self.image='floor.png'
        self.scale=2
        self.x= 1280
        self.color=Color(random.randint(1,255),random.randint(1,255),random.randint(1,255))

    def on_update(self, dt):
        if self.x<30:
            self.delete()
        else:
            self.x-=20



class building_spawn_point(Sprite):
    def on_create(self):
        self.x = 2560
        self.y =400
        self.layer=0
        Scheduler.update(lambda : self.genarate_building(random.randint(1,5)),0.3,)  

    def genarate_building(self,floor_count):
                for i in range(floor_count):
                    windows.create_sprite(floor,y=550+i*173, x=2560)
windows.create_sprite(tram_for_drive)
windows.create_sprite(building_spawn_point)
windows.run()