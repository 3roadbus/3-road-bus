from pycat.core import Window , Sprite , KeyCode

window = Window(background_image= 'busstop.jpg')
#BRUH
class bus(Sprite):
    def on_create(player):
        player.image= 'tnbuso13.jpg'
        player.x=0
        player.y=200
        player.scale=0.1

    def on_update(player, dt):
        player.move_forward(5)
        if player.window.is_key_pressed(KeyCode.W):
            player.rotation=90
        if player.window.is_key_pressed(KeyCode.A):
            player.rotation=180
        if player.window.is_key_pressed(KeyCode.S):
            player.rotation=270
        if player.window.is_key_pressed(KeyCode.D):
            player.rotation=0
        if player.x > 1200:
            print("You've reach the finish line!")
            window.close()
window.create_sprite(bus)
window.run()