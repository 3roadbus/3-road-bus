from pycat.core import Window,Sprite,KeyCode,RotationMode,Scheduler

windows = Window()

wall_inside_x=[2,2,2,3,3,5,3,2,1]
wall_inside_y=[1,2,3,1,5,3,6,6,6]

cell = 64
offx = 32
offy = 32
class box (Sprite):
    def on_create(self):
        self.image = 'box.png'
        self.add_tag('box')
        self.layer = 3
        self.rotation_mode = RotationMode.NO_ROTATION

    def push(self):
        self.rotation = Player.rotation
        self.move_forward(cell)
        self.scale = 0.9
        if self.get_touching_sprites_with_tag('box') or self.get_touching_sprites_with_tag('wall') or self.get_touching_sprites_with_tag('door'):
            self.move_forward(-cell)
            player.move_forward(-cell)

class button (Sprite):
    def on_create(self):
        self.image = 'button.png'
        self.add_tag('button')
        self.layer = 2

    def on_update(self, dt):
        if self.is_touching_any_sprite_with_tag('man'):
            #Door.delete()
            self.delete()

class door (Sprite):
    def on_create(self):
        self.image = 'door.png'
        self.add_tag('door')
        self.layer = 2

class goal (Sprite):
    def on_create(self):
        self.image = 'goal.png'
        self.add_tag('goal')
        self.layer = 2        
        
class wall (Sprite):
    def on_create(self):
        self.image = 'wall.png'
        self.add_tag('wall')
        self.layer = 2

class floor (Sprite):
    def on_create(self):
        self.image = 'floor.png'
        self.add_tag('floor')
        self.layer = 1

class player (Sprite):
    def on_create(self):
        self.add_tag('man')
        self.image = 'man.png'
        self.rotation_mode = RotationMode.NO_ROTATION
        self.layer = 3

    def on_update(self, dt):
        if windows.is_key_down(KeyCode.UP):
            self.rotation = 90
            self.y += cell
        if windows.is_key_down(KeyCode.DOWN):
            self.rotation = 270
            self.y -= cell
        if windows.is_key_down(KeyCode.LEFT):
            self.rotation = 180
            self.x -= cell
        if windows.is_key_down(KeyCode.RIGHT):
            self.rotation = 0
            self.x += cell
        if self.is_touching_any_sprite_with_tag('wall') or self.is_touching_any_sprite_with_tag('door'):
            self.move_forward(-cell)
        tb = self.get_touching_sprites_with_tag('box')
        if len(tb)>0:
            tb[0].push()
            winning()

def  winning():
    box_at_here = 0
    for box in windows.get_sprites_with_tag('box'):
        if box.is_touching_any_sprite_with_tag('goal'):
            box_at_here+=1
        if box_at_here == len(windows.get_sprites_with_tag('box')):
            print('vheiofjg')
            Scheduler.wait(2,windows.close)
            
cool_map =[
["w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w"],
["w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w"],
["w","w","w","w","","","","","","","","","","","","","","","","w"],
["w","","bu","w","bo","bo","","","","w","","","","","","","","","","w"],
["w","","","","p","d","","w","","w","","","","","","","","","","w"],
["w","","w","","","w","","w","","w","","","","","","","","","","w"],
["w","","w","","","g","","w","","w","","","","","","","","","","w"],
["w","g","w","w","","","","w","","w","","","","","","","","","","w"],
["w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w"],
["w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w"]]
cool_map =list(reversed(cool_map))

for Y in range(10):
    for X in range(20):
        
        px = offx + X*cell
        py = offy + Y*cell
        type = cool_map[Y][X]
        if type == "p":
            pl_x = round((px - offx)/cell)
            pl_y = round((py - offy)/cell)
            print(pl_x,pl_y)
            Player = windows.create_sprite(player,x=608,y=288)
def checking():

    player_vision_x = -3
    player_vision_y = -3

    if player_vision_y >3:
        if player_vision_x >3:
            player_vision_x = -3
        else:
            x_ch = pl_x + player_vision_x
            y_ch = pl_y + player_vision_y
            psx = offx + x_ch*cell
            psy = offy + y_ch*cell
            type_s = cool_map[y_ch][x_ch]
            if type_s == "w":
               Wall = windows.create_sprite(wall, x=psx,y=psy)
            if type_s == "g":
               Goal = windows.create_sprite(goal,x=psx,y=psy)
            if type_s == "d":
               Door = windows.create_sprite(door, x=psx,y=psy)
            if type_s == "bo":
               Box = windows.create_sprite(box, x=psx,y=psy)
            if type_s == "bu":
               Button = windows.create_sprite(button,x=psx,y=psy)

windows.run()