from pycat.core import Window, Sprite, Color, KeyCode,Label,Scheduler
import random

station_length=57
lap_lock = False
current_lap= "N"
SCREEN_W = 2560
SCREEN_H = 1280
distance = 500
follow_station = False
approaching= False

window = Window(width=SCREEN_W, height=SCREEN_H,enforce_window_limits=False)

speed = 0

MAX_SPEED = 70

class station(Sprite):
    def on_create(self):
        self.image='station.png'
        self.x=500
        self.y=700
        self.layer = 2
        self.scale = 1.75
        

    def on_update(self, dt):
        global speed,distance,follow_station
        self.x-= speed
        if self.x<-1100:
            follow_station=False
            self.delete()

class TramForDrive(Sprite):

    def on_create(self):
        self.image = 'lrt.png'
        self.x = 15
        self.y = 550
        self.layer = 4

    #def distance_of_approaching():
        

    def on_update(self, dt):
        global speed,distance,follow_station,current_lap,lap_lock,now_lap,Station
        
        distance -= int(speed)/60
        if distance<=0:
            distance=500
            follow_station=True
            Station = window.create_sprite(station,x=4250)
            window.create_sprite(station_hitbox)
            Random_haha = random.randint(10,25)
            for i in range(Random_haha):
                window.create_sprite(passenger)

        #round the value
        if speed < 0.0499999:
            speed = 0

        #accelerate
        if window.is_key_pressed(KeyCode._0):
            current_lap="A4"

        if window.is_key_pressed(KeyCode._9):
            current_lap="A3"

        if window.is_key_pressed(KeyCode._8):
            current_lap="A2"

        if window.is_key_pressed(KeyCode._7):
            current_lap="A1"

        #no action
        if window.is_key_pressed(KeyCode._6):
            current_lap="N"

        #brake
        if window.is_key_pressed(KeyCode._5):
            current_lap="B1"

        if window.is_key_pressed(KeyCode._4):
            current_lap="B2"    

        if window.is_key_pressed(KeyCode._3):
            current_lap="B3"

        if window.is_key_pressed(KeyCode._2):
            current_lap="B4"

        if window.is_key_pressed(KeyCode._1):
            current_lap="B5"   

        #speed
        if current_lap=="A4":
            if speed< MAX_SPEED:
                speed+=0.2
        elif current_lap=="A3":
            if speed< MAX_SPEED:
                speed+=0.15
        elif current_lap=="A2":
            if speed< MAX_SPEED:
                speed+=0.1
        elif current_lap=="A1":
            if speed< MAX_SPEED:
                speed+=0.05
        elif current_lap=="B5":
            if speed>0:
                speed-=0.15
        elif current_lap=="B4":
            if speed>0:
                speed-=0.1
        elif current_lap=="B3":
            if speed>0:
                speed-=0.075
        elif current_lap=="B2":
            if speed>0:
                speed-=0.05
        elif current_lap=="B1":
            if speed>0:
                speed-=0.025
        else:
            speed *= 0.999956

class passenger(station):
    def on_create(self):
        self.position_in_station = random.randint(-1000,1000)
        self.image = 'pax.png'
        self.layer = 3
        self.scale =0.8
        self.y = random.randint(500,540)

    def on_update(self, dt):
        global follow_station,Station
        if follow_station:
            self.x= int(Station.x)+ int(self.position_in_station)
        else:
            self.delete()

class Floor(Sprite):

    def on_create(self):
        self.image = 'floor.png'
        self.scale = 2
        self.layer = 0

        self.color = Color(
            random.randint(1, 255),
            random.randint(1, 255),
            random.randint(1, 255)
        )

        self.can_spawn_next = False
        self.has_spawned_next = False

    def on_update(self, dt):
        global speed

        self.x -= speed
        if self.x<0:
            self.x= 2760

        if self.x < 0:
            self.delete()

            

def spawn_building_column(x):
    number_of_floors = random.randint(1, 5)

    for i in range(number_of_floors):
        floor = window.create_sprite(
            Floor,
            x=x,
            y=350+ i * 173
        )

        if i == 0:
            floor.can_spawn_next = True


def opening_of_buildings():
    number_of_columns = 8

    for i in range(number_of_columns):
        x = i * 343
        spawn_building_column(x)

class tram_hitbox(Sprite):
    def on_create(self):
        self.x=1580
        self.y=430
        self.layer = 4
        self.scale =10
        #self.opacity= 250
        self.color = Color.RED

#684.5
class station_hitbox(Sprite):
    def on_create(self):
        self.y=430
        #self.opacity= 250
        self.scale =10
        self.layer = 4
        self.color = Color.BLUE
    def on_update(self, dt):
        global follow_station,Station
        if follow_station:
            self.x= int(Station.x)+1185
        else:
            self.delete()

class text_test(Label):
    def on_create(self):
        self.position= (1000,1000)
        self.color= Color.BLUE
        self.text = str(0)
        self.layer=2
    def on_update(self, dt):
        global speed
        self.text= str(round(speed))

class test_text(Label):
    def on_create(self):
        self.position= (1000,1200)
        self.color= Color.RED
        self.text = str(0)
        self.layer=2
    def on_update(self, dt):
        global distance
        self.text= str(round(distance)+station_length)

class lap_text(Label):
    def on_create(self):
        self.position= (1000,1100)
        self.color= Color.GREEN
        self.text = ""
        self.layer=2
    def on_update(self, dt):
        global current_lap
        self.text= current_lap

class tram_from_the_other_side(Sprite):
    def on_create(self):
        self.biu = True
        self.image = 'lrt.png'
        self.x = 3500
        self.y = 575
        self.layer = 1
        self.scale =0.8

    def hi(self):
        self.x = 3500
        self.biu = True

    def on_update(self, dt):
        global speed
        
        if self.biu:
            self.x -= int(speed) + 55
            if self.x< -3500:
                self.biu=False
                Scheduler.wait(120,self.hi)


                
# remove later
#class bt(Sprite):
#    def on_create(self):
#        self.scale = 3
#    def on_update(self, dt):
#        self.position = window.mouse_position
 #   def on_left_click_anywhere(self):
  #      print(str(self.x))
  #      print(str(self.y))
#window.create_sprite(bt)
window.create_label(test_text)
window.create_label(text_test)
window.create_label(lap_text)

opening_of_buildings()

window.create_sprite(tram_hitbox)
window.create_sprite(TramForDrive)
window.create_sprite(tram_from_the_other_side)

window.run()