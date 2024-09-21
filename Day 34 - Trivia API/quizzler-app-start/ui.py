from tkinter import *
from quiz_brain import QuizBrain
THEME_COLOR = "#375362"


def aa():
    pass


class QuizInterface:
    def __init__(self, quiz_brain: QuizBrain):

        self.quiz = quiz_brain

        self.window = Tk()
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)
        self.window.title("Quizzler")

        # Creating the Score label
        self.score_label = Label(text="Score: 0", fg="white", bg=THEME_COLOR)
        self.score_label.grid(column=1, row=0)

        # -- Creating the Canvas ---------------------------#
        self.canvas = Canvas(width=300, height=250, bg="white")
        self.question = self.canvas.create_text(
            150,
            125,
            width=280,
            text="hello",
            fill=THEME_COLOR,
            font=("Arial", 15, "italic")
        )
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)

        # Creating the Buttons
        true_image = PhotoImage(file="./images/true.png")
        false_image = PhotoImage(file="./images/false.png")

        self.right = Button(image=true_image, highlightthickness=0, command=self.true_pressed)
        self.right.grid(column=0, row=2)

        self.wrong = Button(image=false_image, highlightthickness=0, command=self.false_pressed)
        self.wrong.grid(column=1, row=2)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            self.score_label.config(text=f"Score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question, text=q_text)
        else:
            self.canvas.itemconfig(self.question, text="You've reached the end of the quiz")
            self.right.config(state="disabled")
            self.wrong.config(state="disabled")

    def true_pressed(self):
        self.give_feedback(self.quiz.check_answer("True"))

    def false_pressed(self):
        is_right = self.quiz.check_answer("False")
        self.give_feedback(is_right)

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")

        self.window.after(1000, self.get_next_question)
