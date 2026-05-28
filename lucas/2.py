from pycat.core import Color,Sprite,Label,Window,Scheduler
import random
window = Window(width=500,height=750)
guess_y=725

square_sprites=[]

next_color={
    Color.WHITE:Color.RED,
    Color.RED:Color.BLUE,
    Color.BLUE:Color.YELLOW,
    Color.YELLOW:Color.GREEN,
    Color.GREEN:Color.RED
}

solution = [Color.BLUE,Color.GREEN,Color.RED,Color.YELLOW]
random.shuffle(solution)

class squares(Sprite):
    def on_create(self):
        self.color = Color.WHITE
        self.scale=65
        self.og=True

    def on_left_click(self):
        if self.og==True:
            self.color=next_color[self.color]

    def clone(self):
        new = window.create_sprite(squares)
        new.position = self.position
        new.color = self.color
        new.og=False
        return new

class check(Sprite):
    def on_create(self):
        self.scale_y=65
        self.scale_x=100

    def on_left_click(self):
        global guess_y
        print('check!')
        correction=0
        for ih in range(4):
            if square_sprites[ih].color == solution[ih]:
                correction+=1

        for i in range(4):
            new = square_sprites[i].clone()
            new.y = guess_y
        window.create_label(text=str(correction), x=425,y=guess_y)
        guess_y-= 75

        if correction==4:
            print('You win!')
            Scheduler.wait(2,window.close)

for hi in range(4):
    i=hi*80+70
    square_sprites.append(window.create_sprite(squares,x=i,y=70))

window.create_sprite(check,x=430,y=70)

window.run()