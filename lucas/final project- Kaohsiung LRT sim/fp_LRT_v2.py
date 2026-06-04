from pycat.core import Window, Sprite, Color, KeyCode
import random

SCREEN_W = 1280
SCREEN_H = 720

window = Window(width=SCREEN_W, height=SCREEN_H)

speed = 0

COLUMN_SPACING = 220
FLOOR_GAP = 95
BASE_Y = 150
MAX_SPEED = 700


class TramForDrive(Sprite):

    def on_create(self):
        self.image = 'lrt.png'
        self.x = SCREEN_W * 0.35
        self.y = SCREEN_H * 0.2
        self.scale = 0.45
        self.layer = 10

    def on_update(self, dt):
        global speed

        if window.is_key_pressed(KeyCode.NUM_0):
            if speed < MAX_SPEED:
                speed += 250 * dt

        elif window.is_key_pressed(KeyCode.NUM_1):
            speed *= 0.985

        else:
            speed *= 0.995

        if speed < 5:
            speed = 0


class Floor(Sprite):

    def on_create(self):
        self.image = 'floor.png'
        self.scale = 1
        self.layer = 1

        self.color = Color(
            random.randint(1, 255),
            random.randint(1, 255),
            random.randint(1, 255)
        )

        self.can_spawn_next = False
        self.has_spawned_next = False

    def on_update(self, dt):
        global speed

        self.x -= speed * dt

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
            y=BASE_Y + i * FLOOR_GAP
        )

        if i == 0:
            floor.can_spawn_next = True


def opening_of_buildings():
    number_of_columns = int(SCREEN_W / COLUMN_SPACING) + 3

    for i in range(number_of_columns):
        x = i * COLUMN_SPACING
        spawn_building_column(x)


opening_of_buildings()

window.create_sprite(TramForDrive)

window.run()