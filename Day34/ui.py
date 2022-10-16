from tkinter import *
from quiz_brain import QuizBrain
from PIL import Image, ImageTk

THEME_COLOR = "#375362"


class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.config()
        self.window.title("Quiz Me")
        self.window.config(bg=THEME_COLOR, padx=20, pady=20)

        self.score = Label(text="Score: 0", fg="white", bg=THEME_COLOR, font=("Arial", 30, "bold"))
        self.score.config()
        self.score.grid(row=0, column=1)

        self.canvas = Canvas(width=300, height=250)
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)

        self.q_text = self.canvas.create_text(150, 125, text="Some Question filler", width=280)
        check_img = ImageTk.PhotoImage(Image.open("images/true.png"))
        cross_img = ImageTk.PhotoImage(Image.open("images/false.png"))

        self.check = Button(text="Cross", image=check_img,highlightthickness=0)
        self.check.grid(row=2, column=0)

        self.cross = Button(text="Cross", image=cross_img, highlightthickness=0)
        self.cross.grid(row=2, column=1)
        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        q_text = self.quiz.next_question()
        self.canvas.itemconfig(self.q_text, text=q_text)
