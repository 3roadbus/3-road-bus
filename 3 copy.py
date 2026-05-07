from pycat.base import NumpyImage
from pycat.core import Window, Sprite
from pycat.base.event.mouse_event import MouseEvent, MouseButton

window = Window(height=360, width=750)

def extract_texture(image: NumpyImage, i: int, j:int, size: int):
    start_col = i*size
    end_col = (i+1)*size
    start_row = j*size
    end_row = (j+1)*size
    array =image[start_row:end_row,start_col:end_col,:]
    texture = NumpyImage.get_texture_from_array(array)
    return texture

og_image = NumpyImage.get_array_from_file("k9da.png")
mouse_segment:Sprite= None

class segment(Sprite):
    def on_create(self):
        self.add_tag('segment')
        self.goto_random_position()
        self.label = window.create_label()

    def on_update(self, dt):
        self.label.text = str(self.i)+','+str(self.j)
        self.label.position = self.position

    def on_left_click(self):
        global mouse_segment
        mouse_segment = self

for i in range(4):
    for j in range(4):
        Segment = window.create_sprite(segment)
        Segment.texture = extract_texture(og_image,i,j,90)
        Segment.i = i
        Segment.j = j
        

class target(Sprite):
    def on_create(self):
        self.add_tag('target')
        self.scale = 30
        self.opacity= 155
        self.label = window.create_label()

    def on_update(self, dt):
        self.label.text = str(self.i)+','+str(self.j)
        self.label.position = self.position

for i in range(4):
    for j in range(4):
        Target = window.create_sprite(target, x=i*90+45, y=j*90+45)
        Target.i = i
        Target.j = j

def puzzle_fin():
    for target in window.get_sprites_with_tag('target'):
        touch_segment = target.get_touching_sprites_with_tag('segment')
        if len(touch_segment)!=1:
            return False
        else:
            Segment = touch_segment[0]
            if Target.i != Segment.i or Target.j != Segment.j:
                return False
    return True

def on_mouse_drag_handler(mouse_event : MouseEvent):
    global mouse_segment
    if mouse_segment:
        mouse_segment.position=window.mouse_position

def on_mouse_release_handler(mouse_event : MouseEvent):
    print('nnnn!')
    global mouse_segment
    if mouse_segment and mouse_event.button == MouseButton.LEFT:
        for target in mouse_segment.get_touching_sprites_with_tag('target'):
            mouse_segment.position=target.position
            break
    mouse_segment = None
    if puzzle_fin():
        print('you win!')

window.subscribe(on_mouse_drag = on_mouse_drag_handler, on_mouse_release = on_mouse_release_handler)

window.run()
