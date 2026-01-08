from pycat.core import Window, Sprite, KeyCode, RotationMode, Scheduler

CELL = 64
mode = 'lobby'
VIEW_W = 5          
VIEW_H = 5          
window = Window(width=VIEW_W * CELL, height=VIEW_H * CELL)

if mode=='lobby':
    window.background_image='bgim.png'
    class play(Sprite):
        def on_create(self):
            self.image = 'play.png'
            self.x = 150
            self.y = 120
            self.scale = 1.2
        
        def on_click(self, mouse_event):
            global mode
            
            mode = 'game'
            self.delete()
            tutobt.delete()

    class tuto(Sprite):
        def on_create(self):
            self.image = 'tutorial.png'
            self.x = 150
            self.y = 65
            self.scale = 1.2   
        
        def on_click(self, mouse_event):
            global mode
            
            mode = 'tutorial'
            self.delete()
            Playbt.delete()

    Playbt = window.create_sprite(play) 
    tutobt = window.create_sprite(tuto) 

    return      

#if mode=='tutorial':


if mode=='game':
    cool_map = [
    ["w","w","w","w","w","w","w","w","w"],
    ["w","w","w","w","","","","w","w"],
    ["w","","bu","w","bo","bo","","w","w"],
    ["w","","","","p","d","","w","w"],
    ["w","","w","","","w","","w","w"],
    ["w","","w","","","g","","w","g"],
    ["w","g","w","w","","","","w","w"],
    ["w","w","w","w","w","w","w","w","w"]
    ]
    cool_map = list(reversed(cool_map))

    MAP_H = len(cool_map)
    MAP_W = len(cool_map[0])

    CENTER_SX = (VIEW_W // 2) * CELL + CELL / 2
    CENTER_SY = (VIEW_H // 2) * CELL + CELL / 2

    class Floor(Sprite):
        def on_create(self):
            self.image = "floor.png"
            self.layer = 1

    class Wall(Sprite):
        def on_create(self):
            self.image = "wall.png"
            self.add_tag("wall")
            self.layer = 2

    class Goal(Sprite):
        def on_create(self):
            self.image = "goal.png"
            self.add_tag("goal")
            self.layer = 2

    class Door(Sprite):
        def on_create(self):
            self.image = "door.png"
            self.add_tag("door")
            self.layer = 2

    class Button(Sprite):
        def on_create(self):
            self.image = "button.png"
            self.add_tag("button")
            self.layer = 2

    class Box(Sprite):
        def on_create(self):
            self.image = "box.png"
            self.add_tag("box")
            self.layer = 3
            self.scale = 0.9
            self.rotation_mode = RotationMode.NO_ROTATION

    class Player(Sprite):
        def on_create(self):
            self.image = "man.png"
            self.add_tag("man")
            self.layer = 10
            self.scale = 0.9
            self.rotation_mode = RotationMode.NO_ROTATION

            self.cooldown = 0.12
            self._t = 0.0

        def on_update(self, dt):
            self._t -= dt
            if self._t > 0:
                return

            dx, dy = 0, 0
            if window.is_key_down(KeyCode.UP):
                self.rotation = 90
                dy = 1
            elif window.is_key_down(KeyCode.DOWN):
                self.rotation = 270
                dy = -1
            elif window.is_key_down(KeyCode.LEFT):
                self.rotation = 180
                dx = -1
            elif window.is_key_down(KeyCode.RIGHT):
                self.rotation = 0
                dx = 1
            else:
                return

            self._t = self.cooldown
            try_move(dx, dy)

    player_gx = None
    player_gy = None

    boxes = set()
    goals = set()
    buttons = set()
    doors = set()
    walls = set()

    for y in range(MAP_H):
        for x in range(MAP_W):
            t = cool_map[y][x]
            if "w" in t:
                walls.add((x, y))
            if "g" in t:
                goals.add((x, y))
            if "bu" in t:
                buttons.add((x, y))
            if "d" in t:
                doors.add((x, y))
            if "bo" in t:
                boxes.add((x, y))
            if "p" in t:
                player_gx, player_gy = x, y

    if player_gx is None:
        player_gx, player_gy = 1, 1

    player_sprite = window.create_sprite(Player, x=CENTER_SX, y=CENTER_SY)

    rendered_sprites = []

    def in_bounds(x, y):
        return 0 <= x < MAP_W and 0 <= y < MAP_H

    def is_blocking(x, y):
        return (x, y) in walls or (x, y) in doors

    def render():
        global rendered_sprites

        for s in rendered_sprites:
            s.delete()
        rendered_sprites = []

        start_x = player_gx - (VIEW_W // 2)
        start_y = player_gy - (VIEW_H // 2)

        for vy in range(VIEW_H):
            for vx in range(VIEW_W):
                gx = start_x + vx
                gy = start_y + vy

                sx = vx * CELL + CELL / 2
                sy = vy * CELL + CELL / 2

                f = window.create_sprite(Floor, x=sx, y=sy)
                rendered_sprites.append(f)

                if not in_bounds(gx, gy):
                    continue

                if (gx, gy) in goals:
                    g = window.create_sprite(Goal, x=sx, y=sy)
                    rendered_sprites.append(g)

                if (gx, gy) in walls:
                    w = window.create_sprite(Wall, x=sx, y=sy)
                    rendered_sprites.append(w)

                if (gx, gy) in doors:
                    d = window.create_sprite(Door, x=sx, y=sy)
                    rendered_sprites.append(d)

                if (gx, gy) in buttons:
                    b = window.create_sprite(Button, x=sx, y=sy)
                    rendered_sprites.append(b)

                if (gx, gy) in boxes:
                    bo = window.create_sprite(Box, x=sx, y=sy)
                    rendered_sprites.append(bo)

        player_sprite.x = CENTER_SX
        player_sprite.y = CENTER_SY


    def check_button_press():
        global doors, buttons
        if (player_gx, player_gy) in buttons:
            buttons.remove((player_gx, player_gy))
            doors = set()  

    def check_win():
        if len(boxes) == 0:
            return
        if all(b in goals for b in boxes):
            print("You win!")
            Scheduler.wait(2, window.close)

    def try_move(dx, dy):
        global player_gx, player_gy, boxes

        nx = player_gx + dx
        ny = player_gy + dy

        if not in_bounds(nx, ny):
            return

        if is_blocking(nx, ny):
            return

        if (nx, ny) in boxes:
            bx = nx + dx
            by = ny + dy

            if not in_bounds(bx, by):
                return
            if is_blocking(bx, by):
                return
            if (bx, by) in boxes:
                return

            boxes.remove((nx, ny))
            boxes.add((bx, by))

        player_gx, player_gy = nx, ny

        check_button_press()
        render()
        check_win()
    render()

window.run()
