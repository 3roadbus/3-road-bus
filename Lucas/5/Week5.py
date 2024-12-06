from pycat.core import Window, Sprite, KeyCode

win = Window(background_image='KM.jpg')

class ball(Sprite):
    def on_create(player):
        player.image='USSR.png'
        player.x=0
        player.y=45
        player.scale=0.25
    
    def on_update(player, dt):
        if player.window.is_key_pressed(KeyCode.A):
            player.x-=3
            player.scale_x=-1
        if player.window.is_key_pressed(KeyCode.D):
            player.scale_x=1
            player.x+=3

class drop(Sprite):
    def on_create(player):
        player.image='vodka.jpg'
        player.x=0
        player.y=500
        player.scale=0.4

    def on_update(self, dt):
        

win.create_sprite(ball)
win.run()