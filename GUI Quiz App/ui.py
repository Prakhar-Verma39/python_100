from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("GUI Quiz App")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)
        self.canvas = Canvas(width=300, height=250, bg="white")
        self.question_text = self.canvas.create_text(
            150,
            125,
            width=280,
            text="question",
            fill=THEME_COLOR,
            font=('Arial', 20, 'italic')
        )
        self.canvas.grid(column=1, row=2, columnspan=2, pady=50)
        self.score_label = Label(text="Score: 0", fg="white", bg=THEME_COLOR, font=("", 16, "normal"))
        self.score_label.grid(column=2, row=1)
        pt = PhotoImage(file="images/true.png")
        pf = PhotoImage(file="images/false.png")
        self.true_button = Button(image=pt, highlightthickness=0, command=self.pressed_true)
        self.false_button = Button(image=pf, highlightthickness=0, command=self.pressed_false)
        self.true_button.grid(column=1, row=3)
        self.false_button.grid(column=2, row=3)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        self.score_label.config(text=f"Score: {self.quiz.score} / {self.quiz.question_number}")
        if self.quiz.still_has_questions():
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
            self.true_button.config(state="normal")
            self.false_button.config(state="normal")
        else:
            self.canvas.itemconfig(self.question_text, text="You've reached the end of the quiz.")
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")

    def pressed_true(self):
        self.true_button.config(state="disabled")
        self.false_button.config(state="disabled")
        self.give_feedback(self.quiz.check_answer("True"))

    def pressed_false(self):
        self.true_button.config(state="disabled")
        self.false_button.config(state="disabled")
        is_right = self.quiz.check_answer("False")
        self.give_feedback(is_right)

    def give_feedback(self, is_right):
        if is_right:
            color = "green"
        else:
            color = "red"
        self.canvas.config(bg=color)
        self.window.after(1000, self.get_next_question)
