from pycat.core import Window, Sprite
from pycat.extensions.turtle import Turtle

window = Window()

turtle = window.create_sprite(Turtle, image = 'USSR.png', scale = 0.125)
turtle.position = (200,200)

def shape():
    long = 100
    for _ in range(12):
        for _ in range(12):
            turtle.move_forward(long)
            turtle.turn_left(30)
        long *= 0.8
    turtle.move_forward(100)

window.run()