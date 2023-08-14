# Flash Cards
from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"
TITLE_FONT = ("Arial", 24, "italic")
WORD_FONT = ("Arial", 24, "bold")

data_dict = {}

try:
    data = pandas.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    original_data = pandas.read_csv("data/french_words.csv")
    data_dic = original_data.to_dict(orient="records")
except pandas.errors.EmptyDataError:
    messagebox.showinfo(title="Alert", message="Your CSV data file is empty")
    quit()
else:
    data_dic = data.to_dict(orient="records")

current_card = {}


def get_word():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    try:
        current_card = random.choice(data_dic)
        if len(current_card) == 2:
            raise ValueError

    except IndexError:
        messagebox.showinfo(title="Congrats", message="You have successfully completed all words")

    except ValueError:
        messagebox.showinfo(title="Alert", message="This is the last word")
        french_word = current_card["French"]
        canvas.itemconfig(lang_Title, text="French", fill="black")
        canvas.itemconfig(word, text=french_word, fill="black")
    else:
        french_word = current_card["French"]
        canvas.itemconfig(lang_Title, text="French", fill="black")
        canvas.itemconfig(word, text=french_word, fill="black")
        canvas.itemconfig(card_background_img, image=card_front_img)
        flip_timer = window.after(3000, flip_card)
    print(len(current_card))


def flip_card():
    canvas.itemconfig(lang_Title, text="English", fill="white")
    canvas.itemconfig(word, text=current_card["English"], fill="white")
    canvas.itemconfig(card_background_img, image=card_back_img)


def is_known():
    try:
        data_dic.remove(current_card)
    except ValueError:
        messagebox.showinfo("No more words left")
    else:
        get_word()
        data_to_save = pandas.DataFrame(data_dic)
        data_to_save.to_csv("data/words_to_learn.csv", index=False)
        print(len(data_dic))


# Window
window = Tk()
window.config(padx=25, pady=25, bg=BACKGROUND_COLOR)
window.title("Flash Card")
flip_timer = window.after(3000, flip_card)

# Canvas
canvas = Canvas(width=800, height=526)
# Image
card_front_img = canvas_image = ImageTk.PhotoImage(Image.open("images/card_front.png"))
card_background_img = canvas.create_image(400, 263, image=canvas_image)

card_back_img = canvas_image = ImageTk.PhotoImage(Image.open("images/card_back.png"))

ImageTk.PhotoImage(Image.open("images/card_back.png"))

canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(row=0, column=0, columnspan=2)

# Canvas Text
lang_Title = canvas.create_text(400, 150, font=TITLE_FONT)
word = canvas.create_text(400, 263, font=WORD_FONT)

# Unknown Button
cross_image = ImageTk.PhotoImage(Image.open("images/wrong.png"))
wrong_button = Button(image=cross_image, highlightthickness=0, command=get_word)
wrong_button.grid(row=1, column=0)

# Correct Button
check_image = ImageTk.PhotoImage(Image.open("images/right.png"))
known_button = Button(image=check_image, highlightthickness=0, command=is_known)
known_button.grid(row=1, column=1)

get_word()

window.mainloop()
