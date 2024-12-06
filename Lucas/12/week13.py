from pycat.core import Window, KeyCode, Sprite, Point, Scheduler
import random

windows = Window(background_image='vol.png')

class Player(Sprite):
    def on_create(self):
        self.image = 'USSR.png'
        self.position = Point(650,300)
        self.scale = 0.2
        self.add_tag('player')

    def on_update(self, dt):
        if self.window.is_key_pressed(KeyCode.UP ):
            self.y += 5
        if self.window.is_key_pressed(KeyCode.DOWN ):
            self.y -= 5
        if self.window.is_key_pressed(KeyCode.LEFT ):
            self.x -= 5
        if self.window.is_key_pressed(KeyCode.RIGHT ):
            self.x += 5

player = windows.create_sprite(Player)

        
class Enemy(Sprite):
    def on_create(self):
        self.image = 'nazi.png'
        self.goto_random_position()
        self.rotation = random.randint(0, 359)
        self.scale = 0.2
        self.time = 0
        self.bullettime = 1

    def on_update(self, dt):
        self.time += dt
        if self.time > self.bullettime:
           Enemybullet = windows.create_sprite(enemybullet)
           self.position = Enemybullet.position
           Enemybullet.point_toward_sprite(player)
           self.time = 0
        if  self.is_touching_window_edge():
            self.delete

enemy = windows.create_sprite(Enemy)

class enemybullet(Sprite):
    def on_create(self):
        self.image = 'naziflag.png'
        self.position = enemy.position
        self.scale = 0.08
        

    def on_update(self, dt):
        self.move_forward(5)
        if self.is_touching_sprite(player):
            self.delete()





windows.run()