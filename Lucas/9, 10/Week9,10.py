from pycat.core import Sprite, KeyCode, Window, Label, Scheduler, RotationMode
import random
win = Window()

class Plus(Sprite):
    def on_create(self):
        self.x = 0
        self.y = 0
        self.image = 'fr.png'
        self.scale = 0.15
        self.is_visible = False

    def on_update(self, dt):
        self.is_visible = True
    


class shooter(Sprite):
    def on_create(self):
        self.x = 650
        self.y = 50
        self.image = 'nazi.png'
        self.scale = 0.2
        Scheduler.update(self.shoot, random.randint(0,1))
    def shoot(self):
        win.create_sprite(Bullet)

class Bullet(Sprite):
    def on_create(self):
        self.x = 650
        self.y = 50
        self.rotation = random.randint(0, 180)
        self.image = 'hitler.png'
        self.scale = 0.2

    def on_update(self,dt):
        self.move_forward(5)
        if self.is_touching_window_edge():
            self.delete()
        if self.is_touching_any_sprite_with_tag('player'):
            global player
            player.delete()

class Player(Sprite):
    def on_create(self):
        self.add_tag('player')
        self.x = 650
        self.y = 600
        self.image = 'poland.png'
        self.scale = 0.1
    
    def on_update(self, dt):
        if self.window.is_key_pressed(KeyCode.A):
            self.x -= 8
        if self.window.is_key_pressed(KeyCode.D):
            self.x += 8
        if self.window.is_key_pressed(KeyCode.S):
            self.y -= 8
        if self.window.is_key_pressed(KeyCode.W):
            self.y += 8

player = win.create_sprite(Player)    
win.create_sprite(shooter)

win.run()