from pycat.core import Window, Sprite, Color, KeyCode,Label,Scheduler
import random

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
        self.layer = 1
        self.scale = 1.75
        

    def on_update(self, dt):
        global speed,distance,follow_station
        self.x-= speed
        if self.x<-950:
            follow_station=False
            self.delete()

class TramForDrive(Sprite):

    def on_create(self):
        self.image = 'lrt.png'
        self.x = 15
        self.y = 550
        self.layer = 2

    #def distance_of_approaching():
        

    def on_update(self, dt):
        global speed,distance,follow_station

        distance -= int(speed)/60
        if distance<=0:
            distance=500
            follow_station=True
            window.create_sprite(station,x=4250)
            window.create_sprite(station_hitbox)

        if window.is_key_pressed(KeyCode.NUM_0):
            if speed < MAX_SPEED:
                speed += 0.25

        elif window.is_key_pressed(KeyCode.NUM_1):
            speed *= 0.985

        else:
            speed *= 0.999956

        if speed < 0.2499:
            speed = 0


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
        self.opacity= 250

#684.5
class station_hitbox(Sprite):
    def on_create(self):
        self.y=430
        self.opacity= 250
        self.scale =10

    def on_update(self, dt):
        global follow_station
        if follow_station:
            self.x= int(Station.x)+684.5
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
        self.text= str(round(distance))

# remove later
#class bt(Sprite):
#    def on_create(self):
#        self.scale = 3
##    def on_update(self, dt):
#        self.position = window.mouse_position
 ##   def on_left_click_anywhere(self):
 #       print(str(self.x))
#        print(str(self.y))
#window.create_sprite(bt)
window.create_label(test_text)
window.create_label(text_test)

opening_of_buildings()

window.create_sprite(tram_hitbox)
window.create_sprite(TramForDrive)
Station = window.create_sprite(station,x=4250)
window.run()