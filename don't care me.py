from pycat.core import Window , Sprite, KeyCode, Scheduler, Point

windows = Window(background_image='grass.jpg')
        
class ally1p1 (Sprite):
    def on_create(self):
        self.image = 'ally1.png'
        self.position = Point(100, 200)
        self.scale = 0.3

class ally1p2 (Sprite):
    def on_create(self):
        self.image = 'enemy1.png'
        self.position = Point(1180, 200)
        self.scale = 0.3

class ally2p1 (Sprite):
    def on_create(self):
        self.image = 'ally2.png'
        self.position = Point(100, 440)
        self.scale = 0.3

class ally2p2 (Sprite):
    def on_create(self):
        self.image = 'enemy2.png'
        self.position = Point(1180, 440)
        self.scale = 0.3


class player1 (Sprite):
    def on_create(self):
        self.image = 'p1.png'
        self.position = Point(100, 320)
        self.scale = 0.3

    def on_update(self, dt):
        self.prev_x = self.x
        self.prev_y = self.y

        if self.window.is_key_pressed(KeyCode.W):
            self.y += 3
        if self.window.is_key_pressed(KeyCode.S):
            self.y -= 3
        if self.window.is_key_pressed(KeyCode.A):
            self.x -= 3
        if self.window.is_key_pressed(KeyCode.D):
            self.x += 3
        if self.is_touching_any_sprite_with_tag('wall'):
            self.x = self.prev_x
            self.y = self.prev_y



class player2 (Sprite):
    def on_create(self):
        self.image = 'p2.png'
        self.position = Point(1180, 320)
        self.scale = 0.3

    def on_update(self, dt):
        self.prev_x = self.x
        self.prev_y = self.y

        if self.window.is_key_pressed(KeyCode.I):
            self.y += 3
        if self.window.is_key_pressed(KeyCode.K):
            self.y -= 3
        if self.window.is_key_pressed(KeyCode.J):
            self.x -= 3
        if self.window.is_key_pressed(KeyCode.L):
            self.x += 3
        if self.is_touching_any_sprite_with_tag('wall'):
            self.x = self.prev_x
            self.y = self.prev_y


class wall1(Sprite):
    def on_create(self):
        self.position = Point(230, 320)
        self.image = '20.png'
        self.scale_x = 4
        self.scale_y = 15
        self.add_tag('wall')

class wall2(Sprite):
    def on_create(self):
        self.position = Point(300, 440)
        self.image = '20.png'
        self.scale_x = 9
        self.scale_y = 3
        self.add_tag('wall')

class wall3(Sprite):
    def on_create(self):
        self.position = Point(300, 200)
        self.image = '20.png'
        self.scale_x = 9
        self.scale_y = 3
        self.add_tag('wall')

class wall4(Sprite):
    def on_create(self):
        self.position = Point(1050, 320)
        self.image = '20.png'
        self.scale_x = 4
        self.scale_y = 15
        self.add_tag('wall')

class wall5(Sprite):
    def on_create(self):
        self.position = Point(975, 440)
        self.image = '20.png'
        self.scale_x = 9
        self.scale_y = 3
        self.add_tag('wall')

class wall6(Sprite):
    def on_create(self):
        self.position = Point(975, 200)
        self.image = '20.png'
        self.scale_x = 9
        self.scale_y = 3
        self.add_tag('wall')

class wall7(Sprite):
    def on_create(self):
        self.position = Point(640,600 )
        self.image = '20.png'
        self.scale_x = 5
        self.scale_y = 6
        self.add_tag('wall')

class wall8(Sprite):
    def on_create(self):
        self.position = Point(640, 320)
        self.image = '20.png'
        self.scale_x = 5
        self.scale_y = 5
        self.add_tag('wall')

class wall9(Sprite):
    def on_create(self):
        self.position = Point(640, 40)
        self.image = '20.png'
        self.scale_x = 5
        self.scale_y = 6
        self.add_tag('wall')

windows.create_sprite(player1)
windows.create_sprite(player2)
windows.create_sprite(wall1)
windows.create_sprite(wall2)
windows.create_sprite(wall3)
windows.create_sprite(wall4)
windows.create_sprite(wall5)
windows.create_sprite(wall6)
windows.create_sprite(wall7)
windows.create_sprite(wall8)
windows.create_sprite(wall9)
windows.create_sprite(ally1p1)
windows.create_sprite(ally2p1)
windows.create_sprite(ally1p2)
windows.create_sprite(ally2p2)
windows.run()
