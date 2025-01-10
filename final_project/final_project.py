from pycat.core import Window , Sprite, KeyCode, Scheduler, Point, Label, Color

windows = Window(background_image='grass.jpg')

team1 = 0
team2 = 0

class point1(Sprite):
    def on_create(self):
        self.position = Point(100,550)
        self.image = 'pt.png'
        
class point2(Sprite):
    def on_create(self):
        self.position = Point(100,90)
        self.image = 'pt.png'
        
class point3(Sprite):
    def on_create(self):
        self.position = Point(480, 90)
        self.image = 'pt.png'
        
class point4(Sprite):
    def on_create(self):
        self.position = Point(480, 550)
        self.image = 'pt.png'

class point5(Sprite):
    def on_create(self):
        self.position = Point(800, 550)
        self.image = 'pt.png'

class point6(Sprite):
    def on_create(self):
        self.position = Point(800, 90)
        self.image = 'pt.png'

class point7(Sprite):
    def on_create(self):
        self.position = Point(1180, 90)
        self.image = 'pt.png'
        
class point8(Sprite):
    def on_create(self):
        self.position = Point(1180, 550)
        self.image = 'pt.png'
        
class point9(Sprite):
    def on_create(self):
        self.position = Point(480, 320)
        self.image = 'pt.png'
        
class point10(Sprite):
    def on_create(self):
        self.position = Point(800, 320)
        self.image = 'pt.png'

class point11(Sprite):
    def on_create(self):
        self.position = Point(640, 450)
        self.image = 'pt.png'
        
class point12(Sprite):
    def on_create(self):
        self.position = Point(640, 190)
        self.image = 'pt.png'

windows.create_sprite(point1)
windows.create_sprite(point2)
windows.create_sprite(point3)
windows.create_sprite(point4)
windows.create_sprite(point5)
windows.create_sprite(point6)
windows.create_sprite(point7)
windows.create_sprite(point8)
windows.create_sprite(point9)
windows.create_sprite(point10)
windows.create_sprite(point11)
windows.create_sprite(point12)

#top left = 1
#battlepoint top left = 4
#battlepoint mid left = 9
#bottom right = 7
#top right = 8
#battlepoint bottom left = 3
#battlepoint top right = 5
#battlepoint bottom right = 6
#battlepoint mid right = 10
#bottom left = 2
#mid top = 11
#mid bottom = 12

class team1_label (Label):
    def on_create(self):
        self.position = Point(300,400 )
        self.color = Color.WHITE
        self.text = "Score:0"

    def on_update(self, dt):
        global team1
        self.text = "Score:" + str(team1)

class team2_label (Label):
    def on_create(self):
        self.position = Point(300,880)
        self.color = Color.WHITE
        self.text = "Score:0"

    def on_update(self, dt):
        global team2
        self.text = "Score:" + str(team2)
windows.create_label(team2_label)

class token1 (Sprite):
    def on_create(self):
        self.image = 'Token.png'
        self.position = Point(640,450)
        self.scale = 0.05

    def on_update(self, dt):
        global team1
        global team2
        if self.is_touching_any_sprite_with_tag('team1'):
            team1 += 1
            self.delete()
        if self.is_touching_any_sprite_with_tag('team2'):
            team2 += 1
            self.delete()

windows.create_label(team1_label)


class token2 (Sprite):
    def on_create(self):
        self.image = 'Token.png'
        self.position = Point(640,190)
        self.scale = 0.05

    def on_update(self, dt):
        global team1
        global team2
        if self.is_touching_any_sprite_with_tag('team1'):
            team1 += 1
            self.delete()
        if self.is_touching_any_sprite_with_tag('team2'):
            team2 += 1
            self.delete()

windows.create_sprite(token1)
windows.create_sprite(token2)

class ally1p1 (Sprite):
    def on_create(self):
        self.image = 'ally1.png'
        self.position = Point(100, 200)
        self.scale = 0.3
        point2_collect = ""
        self.add_tag('team1')

    def on_update(self, dt):
        if not self.y == 90:
            self.y -= 5
        # if self.y == 90:
        #     point2_collect = "p1"
        # if point2_collect == "p1" and not self.x == 5:
        #     self.x += 5

class ally2p1 (Sprite):
    def on_create(self):
        self.image = 'enemy1.png'
        self.position = Point(1180, 200)
        self.scale = 0.3
        self.add_tag('team2')

class ally1p2 (Sprite):
    def on_create(self):
        self.image = 'ally2.png'
        self.position = Point(100, 440)
        self.scale = 0.3
        self.add_tag('team1')

class ally2p2 (Sprite):
    def on_create(self):
        self.image = 'enemy2.png'
        self.position = Point(1180, 440)
        self.scale = 0.3
        self.add_tag('team2')


class player1 (Sprite):
    def on_create(self):
        self.image = 'p1.png'
        self.position = Point(100, 320)
        self.scale = 0.3
        self.add_tag('team1')

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
        self.image = 'p2-1.png'
        self.position = Point(1180, 320)
        self.scale = 0.3
        self.add_tag('team2')

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