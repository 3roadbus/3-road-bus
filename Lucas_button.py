from pycat.core import Window, Sprite, Point, Label
import random

window = Window()

questions = []
answers = []
current_index = 0
score = 0
quiz_active = False
answer_buttons = []

class QuestionLabel(Label):
    def on_create(self):
        self.font_size = 50
        self.position = Point(500, 550)
        self.text = ""

    def on_update(self, dt):
        if quiz_active and current_index < len(questions):
            self.text = questions[current_index]
        elif not quiz_active and questions:
            self.text = f"Quiz Over! Score: {score}/{len(questions)}"

class AnswerButton(Sprite):
    def on_create(self):
        self.label = window.create_label(Label)
        self.label.font_size = 50
        self.scale = 50
        answer_buttons.append(self)

    def set_answer(self, text, correct):
        self.label.text = text
        self.answer_text = text
        self.is_correct = correct

    def on_left_click(self):
        global score, current_index, quiz_active
        if not quiz_active:
            return
        if self.is_correct:
            score += 1
        current_index += 1
        if current_index >= len(questions):
            quiz_active = False
        clear_buttons()
        create_question()

    def on_update(self, dt):
        if not quiz_active and self in answer_buttons:
            self.label.delete()
            self.delete()
            answer_buttons.remove(self)

def clear_buttons():
    for btn in answer_buttons[:]:
        btn.label.delete()
        btn.delete()
        answer_buttons.remove(btn)

def create_question():
    if current_index >= len(questions):
        return
    correct = answers[current_index]
    choices = [correct]
    while len(choices) < 3:
        wrong = str(int(correct) + random.randint(-10, 10))
        if wrong != correct and wrong not in choices:
            choices.append(wrong)
    random.shuffle(choices)
    x_positions = [320, 640, 960]

    i = 0
    for choice in choices:
        b = window.create_sprite(AnswerButton)
        b.position = Point(x_positions[i], 300)
        b.set_answer(choice, choice == correct)
        b.label.position = b.position + Point(0, -80)
        i += 1

def start_quiz():
    global questions, answers, current_index, score, quiz_active
    questions = []
    answers = []
    current_index = 0
    score = 0
    quiz_active = True
    for _ in range(5):
        a = random.randint(1, 100)
        b = random.randint(1, 100)
        questions.append(f"{a} + {b} = ?")
        answers.append(str(a + b))
    window.create_label(QuestionLabel)
    create_question()

start_quiz()
window.run()
