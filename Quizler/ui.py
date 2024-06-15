import tkinter
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class Quiz_Interface:
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = tkinter.Tk()
        self.window.title("Quizler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)
        self.score_label = tkinter.Label(
            text=f"Score: {self.quiz.score}", fg="white", bg=THEME_COLOR
        )
        self.score_label.grid(column=1, row=0)
        self.canvas = tkinter.Canvas(
            width=300, height=250, highlightthickness=0, bg="white"
        )
        self.question_text = self.canvas.create_text(
            150,
            125,
            width=280,
            text="Question text",
            font=("Ariel", 20, "italic"),
            fill=THEME_COLOR,
        )
        self.canvas.grid(column=0, row=1, columnspan=2, pady=50)
        true_img = tkinter.PhotoImage(
            file="images\\true.png"
        )
        self.true_button = tkinter.Button(
            image=true_img,
            highlightthickness=0,
            bg=THEME_COLOR,
            command=self.press_true,
        )
        self.true_button.grid(column=0, row=2)
        false_img = tkinter.PhotoImage(
            file="images\\false.png"
        )
        self.false_button = tkinter.Button(
            image=false_img,
            highlightthickness=0,
            bg=THEME_COLOR,
            command=self.press_false,
        )
        self.false_button.grid(column=1, row=2)

        self.get_question()

        self.window.mainloop()

    def get_question(self):
        self.canvas.config(bg="white")
        if self.quiz.questions_over():
            self.canvas.itemconfig(
                self.question_text,
                text=f"Congratulations! You finished the quiz with a score of {self.quiz.score}/10.",
            )
            self.true_button.grid_remove()
            self.false_button.grid_remove()
            self.timer = self.window.after(6000, self.window.destroy)
        else:
            quiz_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=quiz_text)

    def press_true(self):
        self.feedback(self.quiz.check_answer("True"))

    def press_false(self):
        self.feedback(self.quiz.check_answer("False"))

    def feedback(self, fn: bool):
        if fn:
            self.canvas.config(bg="green")
            self.score_label.config(text=f"Score: {self.quiz.score}")
        else:
            self.canvas.config(bg="red")
        self.timer = self.window.after(1000, self.get_question)

