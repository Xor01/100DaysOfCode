from tkinter import *
from PIL import ImageTk, Image

BACKGROUND_COLOR = "#B1DDC6"

TITLE_FONT = ("Arial", 24, "italic")
WORD_FONT = ("Arial", 24, "bold")

# Window
window = Tk()
window.config(padx=25, pady=25, bg=BACKGROUND_COLOR)
window.title("Flash Card")

# Canvas
canvas = Canvas(width=800, height=526)
my_image = ImageTk.PhotoImage(Image.open("images/card_front.png"))
canvas.create_image(400, 263, image=my_image)
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(row=0, column=0)

# Canvas Text
canvas.create_text(400, 150, text="Title", font=TITLE_FONT)
canvas.create_text(400, 263, text="Word", font=WORD_FONT)



window.mainloop()
