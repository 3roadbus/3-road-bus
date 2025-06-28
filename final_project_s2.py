from pycat.core import Window, Sprite, Point, Scheduler, Label
import random
windows = Window()
Screen_change = 1
hitblock_move = [Point(1080,440),
                 Point(200,440),
                 Point(200,200),
                 Point(1080,200)
                                ]

showing= True
score = 0
question = []
Answer = []
class Question_label(Label):
    def on_create(self):
        self.font_size = 50
        self.position = Point(640, 500)
        self.text = ""

class FeedbackLabel(Label):
    def on_create(self):
        self.font_size = 45
        self.position = Point(640, 400)
        self.text = ""

class title (Label):
    def on_create(self):
        self.text = "Mathing to Winning!"
        self.font_size = 110
        self.position = Point(20,500)
        self.rotation = 90

    def on_update(self, dt):
        if not Screen_change == 1:
            self.delete()
        self.rotation += 20
class fly_dec (Sprite):
    def on_create(self):
        self.image='tra.png'
        self.goto_random_position()
        self.scale = 0.5
        self.speed = 15
        self.rotation= 0

    def on_update(self, dt):
        self.move_forward(self.speed)
        if self.is_touching_window_edge():
            changing = random.randint(105,255)
            self.rotation += changing
        if not Screen_change == 1:
            self.delete()

class Hitblock(Sprite):
    def on_create(self):
        self.scale = 5
        self.position=Point(1080,440)
        self.index = 0

    def on_update(self, dt):
        target = hitblock_move[self.index]
        self.point_toward(target)
        self.move_forward(10)
        if self.distance_to(target) < 10:
            if self.index >= 3:
                self.index = 0
            else:
                self.index += 1
        if not Screen_change == 1:
            self.delete()

hitblock = windows.create_sprite(Hitblock)

class ftcc(Sprite):
        def on_create(self):
            self.image ='FTCC.png'
            self.scale = 0.5
            self.position=Point(1080,440)
            self.rotation =0

        def on_update(self, dt):
            self.position = hitblock.position
            self.rotation += 5
            if not Screen_change == 1:
                self.delete()
class Easy(Sprite):
    def on_create(self):
        self.time = 0
        self.image = 'easy.png'
        self.scale = 4
        self.position = Point(320, 480)
    
    def on_left_click(self):
        global showing
        showing = False
        self.time= 0
        start_quiz("easy")

    def on_update(self, dt):
        if showing == False:
            self.opacity = 0.1
            
class Mid(Sprite):
    def on_create(self):
        self.image = 'med.png'
        self.scale = 4
        self.position = Point(640, 480)
        self.time = 0
    
    def on_left_click(self):
        global showing
        showing = False
        self.time= 0
        start_quiz("medium")

    def on_update(self, dt):
        if showing == False:
            self.opacity = 0.1
            

class Hard(Sprite):
    def on_create(self):
        self.image = 'hard.png'
        self.scale = 4
        self.position = Point(960, 480)
        self.time = 0
    
    def on_left_click(self):
        global showing
        showing = False
        self.time= 0
        start_quiz("hard")

    def on_update(self, dt):
        if showing == False:
            self.opacity = 0.1
            

class EX(Sprite):
    def on_create(self):
        self.image = 'ex.png'
        self.scale = 4
        self.position = Point(320, 160)
        self.time = 0
    
    def on_left_click(self):
        global showing
        showing = False
        self.time= 0
        start_quiz("EX")

    def on_update(self, dt):
        if showing == False:
            self.opacity = 0.1
            
class play(Sprite):
    def on_create(self):
        self.scale = 3
        self.image = 'costume1.png'
        self.position=Point(640,320)

    def on_click(self, mouse_event):
        global Screen_change
        Screen_change = 2
        windows.create_sprite(Easy)
        windows.create_sprite(Mid)
        windows.create_sprite(Hard)
        windows.create_sprite(EX)
        if not Screen_change == 1:
            self.delete()
        
windows.create_sprite(ftcc)
for _ in range(20):
    windows.create_sprite(fly_dec)

    # if Screen_change == 1:

def start_quiz(difficulty):
    global question, Answer,score, question_label, feedback_label
    question.clear()
    Answer.clear()
    score = 0

    for _ in range(5):
        if difficulty == "easy":
            a = random.randint(1, 25)
            b = random.randint(1, 25)
            question.append(f"{a} + {b}")
            Answer.append(str(a + b))
        elif difficulty == "medium":
            a = random.randint(20, 25)
            b = random.randint(1, 25)
            question.append(f"{a} - {b}")
            Answer.append(str(a - b))
        elif difficulty == "hard":
            a = random.randint(1, 25)
            b = random.randint(1, 25)
            question.append(f"{a} x {b}")
            Answer.append(str(a * b))
        elif difficulty == "EX":
            a = random.randint(1, 25)
            b = random.randint(1, 25)* a
            question.append(f"{b} ÷ {a}")
            Answer.append(str(b / a))

    feedback_label = windows.create_label(FeedbackLabel)
    question_label = windows.create_label(Question_label)
    run_quiz()

def run_quiz():
    global score
    for i in range(5):
        q = question[i]
        question_label.text = f"Q{i+1}: {q} = ?"
        feedback_label.text = ""

        user_input = input(f"{q} = ")
        if user_input.strip() == Answer[i]:
            feedback_label.text = "✅ Correct!"
            score += 1
        else:
            feedback_label.text = f"❌ Wrong! Correct: {Answer[i]}"

    question_label.text = "Quiz Finished!"
    feedback_label.text = f"Your Score: {score}/5"

windows.create_label(title)
windows.create_sprite(play)

windows.run()
