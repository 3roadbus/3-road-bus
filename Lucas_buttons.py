from pycat.core import Window, Sprite, Point, Label
import random

window = Window()
Screen_change = 1

# Quiz state
Easy_math = []
Easy_ans = []
current_question_index = 0
score = 0
quiz_active = False

# === Question Label ===
class QuestionLabel(Label):
    def on_create(self):
        self.font_size = 40
        self.position = Point(300, 600)
        self.text = ""

    def on_update(self, dt):
        if quiz_active and current_question_index < len(Easy_math):
            self.text = Easy_math[current_question_index]
        elif not quiz_active and Easy_math:
            self.text = f"Quiz Over! Your score: {score}/{len(Easy_math)}"

# === Answer Button ===
answer_buttons = []  # to manually track sprites and their labels

class AnswerOption(Sprite):
    def on_create(self):
        self.label = window.create_label(Label)
        self.label.font_size = 70
        self.scale = 50  # Bigger button
        answer_buttons.append(self)

    def set_answer(self, answer_text, is_correct):
        self.answer_text = answer_text
        self.label.text = answer_text
        self.is_correct = is_correct

    def on_left_click(self):
        global score, current_question_index, quiz_active
        if not quiz_active:
            return
        if self.is_correct:
            score += 1
        current_question_index += 1
        if current_question_index >= len(Easy_math):
            quiz_active = False
        clear_answers()
        create_question()

    def on_update(self, dt):
        if not quiz_active and self in answer_buttons:
            self.delete()
            self.label.delete()
            answer_buttons.remove(self)

# === Helper to remove old answers ===
def clear_answers():
    for btn in answer_buttons[:]:
        btn.delete()
        btn.label.delete()
        answer_buttons.remove(btn)

# === Title ===
class Title(Label):
    def on_create(self):
        self.text = "Mathing to Winning!"
        self.font_size = 110
        self.position = Point(20, 500)
        self.rotation = 90

    def on_update(self, dt):
        self.rotation += 20
        if Screen_change != 1:
            self.delete()

# === Flying Decorations ===
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
        if Screen_change != 1:
            self.delete()

# === Easy Button ===
class Easy(Sprite):
    def on_create(self):
        self.image = 'easy.png'
        self.scale = 4
        self.position = Point(640, 480)

    def on_left_click(self):
        global Screen_change, Easy_math, Easy_ans, current_question_index, score, quiz_active
        Screen_change = 3
        Easy_math.clear()
        Easy_ans.clear()
        current_question_index = 0
        score = 0
        quiz_active = True

        for _ in range(5):
            a = random.randint(1, 100)
            b = random.randint(1, 100)
            Easy_math.append(f"{a} + {b} = ?")
            Easy_ans.append(str(a + b))

        window.create_label(QuestionLabel)
        create_question()

    def on_update(self, dt):
        if Screen_change != 2:
            self.delete()

# === Play Button ===
class PlayButton(Sprite):
    def on_create(self):
        self.image = 'costume1.png'
        self.scale = 3
        self.position = Point(640, 320)

    def on_click(self, mouse_event):
        global Screen_change
        Screen_change = 2
        window.create_sprite(Easy)
        self.delete()

# === Create Answers ===
def create_question():
    if current_question_index >= len(Easy_math):
        return

    correct = Easy_ans[current_question_index]
    choices = [correct]
    while len(choices) < 3:
        wrong = str(int(correct) + random.randint(-10, 10))
        if wrong != correct and wrong not in choices:
            choices.append(wrong)
    random.shuffle(choices)

    x_positions = [320, 640, 960]
    for i, ans in enumerate(choices):
        a = window.create_sprite(AnswerOption)
        a.position = Point(x_positions[i], 400)
        a.set_answer(ans, ans == correct)
        a.label.position = a.position + Point(0, -100)

# === Startup Menu ===
for _ in range(20):
    window.create_sprite(FlyDec)
window.create_label(Title)
window.create_sprite(PlayButton)

window.run()
