from tkinter import *
from PIL import Image, ImageTk

THEME_COLOR = "#375362"


class QuizInterface:

    def __init__(self):
        self.window = Tk()
        self.window.config()
        self.window.title("Quiz Me")
        self.window.config(bg=THEME_COLOR, padx=20, pady=20)

        self.score = Label(text="Score: 0", fg="white", bg=THEME_COLOR, font=("Arial", 24, "bold"))
        self.score.config()
        self.score.grid(row=0, column=1)

        self.canvas = Canvas(width=300, height=250)
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)

        self.q_text = self.canvas.create_text(150, 125, text="Some Question filler", fill=THEME_COLOR)

        check_img = ImageTk.PhotoImage(Image.open("images/true.png"))
        cross_img = ImageTk.PhotoImage(Image.open("images/false.png"))

        self.check = Button(text="Cross", image=check_img,highlightthickness=0)
        self.check.grid(row=2, column=0)

        self.cross = Button(text="Cross", image=cross_img, highlightthickness=0)
        self.cross.grid(row=2, column=1)

        self.window.mainloop()
