from pycat.core import Window, Sprite, KeyCode,Color, Scheduler
import random

Windows = Window(background_image='uhm.png', enforce_window_limits= False)

class WrapSprite(Sprite):
    def wrap_on_window(self):
        if self.x < 0-Windows.width/ 2:
            self.x = Windows.width
        elif self.x > Windows.width+Windows.width/ 2:
            self.x= 0

        if self.y < 0-Windows.height/ 2:
            self.y = Windows.height
        elif self.y > Windows.height+Windows.height/ 2:
            self.y= 0

class obstacle_hitbox(WrapSprite):
    def on_create(self):
        self.image = 'sb.png'
        self.speed = random.randint(2,10)
        self.rotation = random.randint(1,360)
        self.layer =2
        self.add_tag('sb')
        self.scale = 0.8

    def separated(self,XX,YY,smaller):
            for i in range(random.randint(1,4)):
                Windows.create_sprite(obstacle_hitbox,x=XX+random.randint(-30,30),y=YY+random.randint(-30,30),scale=smaller)

    def on_update(self, dt):

        self.wrap_on_window()
        
        if self.scale<=0.4:
            self.delete()

        self.move_forward(self.speed)
        if dt>=20:
            self.delete()
        for bullet in self.get_touching_sprites_with_tag('bullet'):
            self.separated(self.x,self.y,self.scale*0.75)
            bullet.delete()
            self.delete()

class bullet(Sprite):
    def on_create(self):
        self.scale_x = 30
        self.scale_y = 7.5
        self.color = Color.RED
        self.layer = 0
        self.add_tag('bullet')

    def on_update(self, dt):
        self.move_forward(25)
        if self.is_touching_window_edge():
            self.delete()
            
class player(WrapSprite):
    def on_create(self):
        self.x = 640
        self.y = 320
        self.image = 'arrow.png'
        self.scale = 0.35
        self.rotation=0
        self.speed = 0
        self.layer =1
        self.add_tag('player')
    
    def on_update(self, key_event):
        self.wrap_on_window()
        if Windows.is_key_pressed(KeyCode.W):
            self.speed = min(5,self.speed+0.25)
        if Windows.is_key_pressed(KeyCode.S):
            self.speed = max(0,self.speed-0.05)
        if Windows.is_key_pressed(KeyCode.A):
            self.rotation += 3
        if Windows.is_key_pressed(KeyCode.D):
            self.rotation -= 3

        self.move_forward(self.speed)

        if Windows.is_key_down(KeyCode.SPACE):
            Bullet = Windows.create_sprite(bullet)
            Bullet.rotation = self.rotation
            Bullet.position = self.position

def creating_sb():
    Windows.create_sprite(obstacle_hitbox, x= random.randint(50,1200), y= random.randint(50,600))

Scheduler.update(creating_sb, 2.5)

Windows.create_sprite(player)
Windows.run()