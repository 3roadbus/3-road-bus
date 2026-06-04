from pycat.core import Window, Sprite, Color, KeyCode,Label
import random

SCREEN_W = 2560
SCREEN_H = 1280

window = Window(width=SCREEN_W, height=SCREEN_H)

speed = 0

COLUMN_SPACING = 220
BASE_Y = 150
MAX_SPEED = 70


class TramForDrive(Sprite):

    def on_create(self):
        self.image = 'lrt.png'
        self.x = 15
        self.y = 550
        self.layer = 1

    def on_update(self, dt):
        global speed

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
        if self.can_spawn_next and not self.has_spawned_next and self.x < 25:
            spawn_building_column(SCREEN_W + COLUMN_SPACING)
            self.has_spawned_next = True

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
    number_of_columns = int(SCREEN_W / COLUMN_SPACING) + 3

    for i in range(number_of_columns):
        x = i * 363
        spawn_building_column(x)

class test_text(Label):
    def on_create(self):
        self.position= (1000,1000)
        self.color= Color.BLUE
        self.text = str(0)
        self.layer=2
    def on_update(self, dt):
        global speed
        self.text= str(round(speed))

window.create_label(test_text)


opening_of_buildings()

window.create_sprite(TramForDrive)

window.run()