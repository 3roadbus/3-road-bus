from pycat.core import Window, Label, Point
import random
import time

window = Window()

# Setup Labels
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

question_label = window.create_label(QuestionLabel)
feedback_label = window.create_label(FeedbackLabel)

# Generate Questions
questions = []
answers = []
for _ in range(5):
    a = random.randint(1, 20)
    b = random.randint(1, 20)
    questions.append(f"{a} + {b}")
    answers.append(str(a + b))

# Run Quiz
score = 0
for i in range(5):
    q = questions[i]
    question_label.text = f"Q{i+1}: {q} = ?"
    feedback_label.text = ""
    time.sleep(0.5)  # allow time for the question to appear

    user_input = input(f"{q} = ")
    if user_input.strip() == answers[i]:
        feedback_label.text = "✅ Correct!"
        score += 1
    else:
        feedback_label.text = f"❌ Wrong! Correct: {answers[i]}"
    time.sleep(1.5)

# Final Result
question_label.text = "Quiz Finished!"
feedback_label.text = f"Your Score: {score}/5"

window.run()
