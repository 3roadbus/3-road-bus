from pycat.core import Window, KeyCode, Sprite, Point, Scheduler
import random

windows = Window(background_image='vol.png')

class Player(Sprite):
    def on_create(self):
        self.image = 'USSR.png'
        self.position = Point(650,300)
        self.scale = 0.2

    def on_update(self, dt):
        if self.window.is_key_pressed(KeyCode.UP ):
            self.y += 5
        if self.window.is_key_pressed(KeyCode.DOWN ):
            self.y -= 5
        if self.window.is_key_pressed(KeyCode.LEFT ):
            self.x -= 5
        if self.window.is_key_pressed(KeyCode.RIGHT ):
            self.x += 5

class Enemy(Sprite):
    def on_create(self):
        self.image = 'nazi.png'
        self.goto_random_position()
        self.rotation = random.randint(0, 359)
        self.scale = 0.2
        Scheduler.update(self.shoot, 1 )
    def shoot(self):
        windows.create_sprite(enemybullet)
    def on_update(self, dt):
        self.move_forward(3)
        if self.x > 1200 or self.x < 10 or self.y < 10 or self.y > 1250:
            self.delete()

class enemybullet(Sprite):
    def on_create(self):
        self.image = 'naziflag.png'
        self.position = enemy.position
        self.scale = 0.08

    def on_update(self, dt):
        self.point_toward_sprite(player)
        
player = windows.create_sprite(Player)
enemy = windows.create_sprite(Enemy)
windows.run()