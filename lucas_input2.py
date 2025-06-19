from pycat.core import Window, Sprite, Label, Point
import random
import time

window = Window()
Screen_state = "menu"

questions = []
answers = []
score = 0

# === UI Labels ===

class QuestionLabel(Label):
    def on_create(self):
        self.font_size = 50
        self.position = Point(640, 500)
        self.text = ""

class FeedbackLabel(Label):
    def on_create(self):
        self.font_size = 45
        self.position = Point(640, 400)
        self.text = ""

question_label = None
feedback_label = None

# === Intro Animation ===

class Title(Label):
    def on_create(self):
        self.text = "Mathing to Winning!"
        self.font_size = 110
        self.position = Point(20, 500)
        self.rotation = 90

    def on_update(self, dt):
        self.rotation += 20
        if Screen_state != "menu":
            self.delete()

class FlyDec(Sprite):
    def on_create(self):
        self.image = 'tra.png'
        self.goto_random_position()
        self.scale = 0.5
        self.speed = 15

    def on_update(self, dt):
        self.move_forward(self.speed)
        if self.is_touching_window_edge():
            self.rotation += random.randint(105, 255)
        if Screen_state != "menu":
            self.delete()

# === Buttons ===

class PlayButton(Sprite):
    def on_create(self):
        self.image = 'costume1.png'
        self.scale = 3
        self.position = Point(640, 320)

    def on_left_click(self):
        global Screen_state
        Screen_state = "choose_difficulty"
        self.delete()
        window.create_sprite(EasyButton)

    def on_update(self, dt):
        if Screen_state != "menu":
            self.delete()

class EasyButton(Sprite):
    def on_create(self):
        self.image = 'easy.png'
        self.scale = 4
        self.position = Point(640, 480)

    def on_left_click(self):
        global Screen_state
        Screen_state = "quiz"
        self.delete()
        start_quiz()

    def on_update(self, dt):
        if Screen_state != "choose_difficulty":
            self.delete()

# === Quiz Functions ===

def start_quiz():
    global questions, answers, score, question_label, feedback_label
    questions.clear()
    answers.clear()
    score = 0

    for _ in range(5):
        a = random.randint(1, 20)
        b = random.randint(1, 20)
        questions.append(f"{a} + {b}")
        answers.append(str(a + b))

    question_label = window.create_label(QuestionLabel)
    feedback_label = window.create_label(FeedbackLabel)

    run_quiz()

def run_quiz():
    global score
    for i in range(5):
        q = questions[i]
        question_label.text = f"Q{i+1}: {q} = ?"
        feedback_label.text = ""
        time.sleep(0.5)

        user_input = input(f"{q} = ")
        if user_input.strip() == answers[i]:
            feedback_label.text = "✅ Correct!"
            score += 1
        else:
            feedback_label.text = f"❌ Wrong! Correct: {answers[i]}"
        time.sleep(1.5)

    question_label.text = "Quiz Finished!"
    feedback_label.text = f"Your Score: {score}/5"

# === Startup ===

for _ in range(20):
    window.create_sprite(FlyDec)
window.create_label(Title)
window.create_sprite(PlayButton)

window.run()
