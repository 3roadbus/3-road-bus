from pycat.core import Window, Sprite, Color, KeyCode,Label,Scheduler,Player
import random,pyglet

from pathlib import Path

station_name =[
    "籬仔內","凱旋瑞田","前鎮之星","凱旋中華","夢時代","經貿園區","軟體園區","高雄展覽館","旅運中心","光榮碼頭","真愛碼頭","駁二大義","駁二蓬萊","哈瑪星","壽山公園","文武聖殿","鼓山區公所","鼓山","馬卡道","臺鐵美術館","內惟藝術中心","美術館","聯合醫院","龍華國小","愛河之心","新上國小","大順民族","灣仔內","高雄高工","樹德家商","科工館","聖功醫院","凱旋公園","衛生局","五權國小","凱旋武昌","凱旋二聖","輕軌機廠"
]

FONT_PATH ='highway.ttf'
pyglet.font.add_file(str(FONT_PATH))

station_length=57
lap_lock = False
current_lap= "N"
SCREEN_W = 2560
SCREEN_H = 1280
distance = 500
follow_station = False
status = 'way'
"STATUS: WAY>>>ARRIVE>>>STOP     REPEAT FOREVER"
button_scale = 1.3
button_layer = 11
button_y = 307
is_door_close = True
go_to_the_next_stop = False
Money = 0
change_stop = False

window = Window(width=SCREEN_W, height=SCREEN_H,enforce_window_limits=False, background_image='bk.png')

speed = 0

MAX_SPEED = 70

BK = Player('bk_sound.mp3')
BK.volume = 0.5

def playing_music():
    BK.play()

playing_music()
Scheduler.update(playing_music,313)

class horn(Sprite):
    def on_create(self):
        self.image = 'horn.png'
        self.layer = button_layer
        self.scale = button_scale
        self.x = 100
        self.y = button_y
        self.playing = False

    def honk(self):
        horn_sound = Player('horn.mp3')
        horn_sound.volume = 1.5
        horn_sound.play()

    def on_left_click(self):
        self.honk()

class horn_t(Label):
    def on_create(self):
        self.layer = button_layer +1 
        self.text = 'Press the button \n         to horn'
        self.x = 180
        self.y = button_y + 25
        self.font_size = 26
        self.font = 'Highway Gothic Wide'
        self.color = Color.BLACK

class door(Sprite):
    def on_create(self):
        global is_door_close
        self.image = 'door.png'
        self.layer = button_layer
        self.scale = button_scale
        self.x = 700
        self.y = button_y
    
    def door_close_auto(self):
        global is_door_close,status,go_to_the_next_stop
        is_door_close = True
        go_to_the_next_stop = True

    def on_left_click(self):
        global is_door_close,status, go_to_the_next_stop
        if is_door_close and status =='stop':
            is_door_close = False
            Scheduler.wait(5,self.door_close_auto)
            
class door_t(Label):
    def on_create(self):
        self.layer = button_layer +1 
        self.text = ' Press the button \n to transfer people'
        self.x = 780
        self.y = button_y + 25
        self.font_size = 26
        self.font = 'Highway Gothic Wide'
        self.color = Color.BLACK
window.create_label(door_t)
window.create_label(horn_t)
window.create_sprite(door)
window.create_sprite(horn)

class bottom_(Sprite):
    def on_create(self):
        self.scale_x = 2560
        self.scale_y = 170
        self.x = 1280
        self.y =300
        self.layer = 10
        self.color = Color.TEAL

class top_(Sprite):
    def on_create(self):
        self.scale_x = 2560
        self.scale_y = 100
        self.x = 1280
        self.y =1230
        self.layer = 10
        self.color = Color.TEAL

window.create_sprite(bottom_)
window.create_sprite(top_)

class station(Sprite):
    def on_create(self):
        self.image='station.png'
        self.x=500
        self.y=700
        self.layer = 2
        self.scale = 1.75
        

    def on_update(self, dt):
        global speed,distance,follow_station,status,change_stop,Money
        self.x-= speed
        if self.x<-1100:
            follow_station=False
            if status =='arrive':
                Money -= 50
                status = 'way'
                distance = random.randint(250,1000)
            change_stop = True
            self.delete()

class station_name_t(Label):
    def on_create(self):
        global station_name
        self.position= (1560,1260)
        self.color= Color.WHITE
        self.label = station_name[0]
        self.layer=12
        self.font_size = 40
        self.i = 0

    def on_update(self, dt):
        global change_stop, station_name
        if change_stop:
            if self.i<= 37:
                self.i+= 1 
            else:
                self.i = 0
            change_stop = False
        self.text = station_name[self.i]
            

window.create_label(station_name_t)

class TramForDrive(Sprite):

    def on_create(self):
        self.image = 'lrt.png'
        self.x = 15
        self.y = 550
        self.layer = 4

    #def distance_of_approaching():
        

    def on_update(self, dt):
        global speed,distance,follow_station,current_lap,lap_lock,status,Station,Station_h,go_to_the_next_stop
        
        distance -= int(speed)/60
        if distance<=0 and status == 'way':
            follow_station=True
            Station = window.create_sprite(station,x=4250)
            Station_h = window.create_sprite(station_hitbox)
            Random_haha = random.randint(10,25)
            for i in range(Random_haha):
                window.create_sprite(passenger)
            status = 'arrive'

        if speed == 0 and status == 'arrive':
            status = 'stop'
            current_lap = "N"
        
        if go_to_the_next_stop:
            distance=500
            status = 'way'

        #round the value
        if speed < 0.0499999:
            speed = 0

        #accelerate
        if window.is_key_pressed(KeyCode._0) and status != 'stop':
            current_lap="A4"

        if window.is_key_pressed(KeyCode._9) and status != 'stop':
            current_lap="A3"

        if window.is_key_pressed(KeyCode._8) and status != 'stop':
            current_lap="A2"

        if window.is_key_pressed(KeyCode._7) and status != 'stop':
            current_lap="A1"

        #no action
        if window.is_key_pressed(KeyCode._6) and status != 'stop':
            current_lap="N"

        #brake
        if window.is_key_pressed(KeyCode._5) and status != 'stop':
            current_lap="B1"

        if window.is_key_pressed(KeyCode._4) and status != 'stop':
            current_lap="B2"    

        if window.is_key_pressed(KeyCode._3) and status != 'stop':
            current_lap="B3"

        if window.is_key_pressed(KeyCode._2) and status != 'stop':
            current_lap="B4"

        if window.is_key_pressed(KeyCode._1) and status != 'stop':
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
        global follow_station,Station, status, is_door_close,Money
        if status =='stop'and is_door_close == False:
            Money += 5
            self.delete()
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
        self.opacity= 10
        self.color = Color.RED

#684.5
class station_hitbox(Sprite):
    def on_create(self):
        self.y=430
        self.opacity= 10
        self.scale =10
        self.layer = 4
        self.color = Color.BLUE

    def on_update(self, dt):
        global follow_station,Station
        if follow_station:
            self.x= int(Station.x)+1185
        else:
            self.delete()

Tram = window.create_sprite(tram_hitbox)

#speed bar
class text_test(Label):
    def on_create(self):
        self.position= (325,1250)
        self.color= Color.BLUE
        self.text = str(0)
        self.layer=12
        self.font = 'Highway Gothic Wide'
        self.font_size = 40

    def on_update(self, dt):
        global speed
        self.text= str(round(speed))+" km/h"

#distance bar
class test_text(Label):
    def on_create(self):
        self.position= (50,1250)
        self.color= Color.WHITE
        self.text = str(0)
        self.layer=12
        self.font = 'Highway Gothic Wide'
        self.font_size = 40
    
    def on_update(self, dt):
        global distance, status,Tram,Station_h,speed, go_to_the_next_stop
        if go_to_the_next_stop:
            self.text= str(round(distance)+station_length) + " m"
            self.color = Color.WHITE
            go_to_the_next_stop = False
        if status == 'way' or go_to_the_next_stop:
            self.text= str(round(distance)+station_length) + " m"
            self.color = Color.WHITE
        elif status == 'arrive':
            T = str(abs(round((int(Tram.x) - int(Station_h.x))/60)))
            self.text = str(abs(round((int(Tram.x) - int(Station_h.x))/60))) + " m"
            if int(Tram.x) < int(Station_h.x) and int(T)>= 10:
                self.color = Color.ORANGE
            elif int(Tram.x) < int(Station_h.x) and int(T)<= 10 and int(T)>=0:
                self.color = Color.GREEN
            elif int(Tram.x) > int(Station_h.x):
                self.color = Color.RED
            
            if speed == 0:
                self.text = str(T) + " m"
                self.color = Color.BLACK

#gear bar
class lap_text(Label):
    def on_create(self):
        self.position= (600,1250)
        self.color= Color.GREEN
        self.text = ""
        self.layer=12
        self.font = 'Highway Gothic Wide'
        self.font_size = 40
    def on_update(self, dt):
        global current_lap
        self.text= current_lap

class money_text(Label):
    def on_create(self):
        self.position= (875,1250)
        self.color= Color.YELLOW
        self.text = str(0) + " $"
        self.layer=12
        self.font = 'Highway Gothic Wide'
        self.font_size = 40
    def on_update(self, dt):
        global Money
        self.text= str(Money) + " $"

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

class idk(Sprite):
    def on_create(self):
        self.scale_x = 250
        self.scale_y = 80
        self.color = Color(165,42,42)
        self.y = 1230
        self.layer = 11

for i in range(5):
    window.create_sprite(idk, x = 150 + 275*i)

window.create_label(money_text)
window.create_label(test_text)
window.create_label(text_test)
window.create_label(lap_text)

opening_of_buildings()

class _test(Label):
    def on_create(self):
        self.position= (1125,1250)
        self.color= Color.AMBER
        self.text = str(0)
        self.layer=12
        self.font = 'Highway Gothic Wide'
        self.font_size = 36

    def on_update(self, dt):
        global status
        self.text="Mode: " + status

window.create_label(_test)

window.create_sprite(tram_hitbox)
window.create_sprite(TramForDrive)
window.create_sprite(tram_from_the_other_side)

window.run()