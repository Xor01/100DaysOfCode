import math
from tkinter import *
from PIL import ImageTk, Image

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = ""


# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    title_label.config(text="Timer")
    check_marks.config(text="")
    global reps
    reps = 0

# ---------------------------- TIMER MECHANISM ------------------------------- #


def start_timer():
    global reps
    reps += 1
    if reps % 8 == 0:
        count_down(LONG_BREAK_MIN * 60)
        title_label.config(text="Break", fg=RED)
    elif reps % 2 == 0:
        count_down(SHORT_BREAK_MIN * 60)
        title_label.config(text="Break", fg=PINK)
    else:
        count_down(WORK_MIN * 60)
        title_label.config(text="Work", fg=GREEN)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = "0" + str(count_sec)

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        global reps
        work_session = math.floor(reps / 2)
        marks = ""
        for _ in range(work_session):
            marks += "✔"
            check_marks.config(text=marks)


# ---------------------------- UI SETUP ------------------------------- #
# Window part
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

# Label Timer

title_label = Label(fg=GREEN, bg=YELLOW)
title_label.grid(row=0, column=1)
title_label.config(font=(FONT_NAME, 40, "bold"))

# Canvas part
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_photo = ImageTk.PhotoImage(Image.open("tomato.png"))
canvas.create_image(100, 112, image=tomato_photo)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 24, "bold"))
canvas.grid(row=1, column=1)

# Start Button
start_button = Button(text="Start", fg="black", command=start_timer, highlightthickness=0, bg=YELLOW)
start_button.grid(row=2, column=0)

# Reset Button
reset_button = Button(text="Reset", fg="black",highlightthickness=0, bg=YELLOW, command=reset_timer)
reset_button.grid(row=2, column=2)

# Check marks

check_marks = Label(bg=YELLOW, fg=GREEN)
check_marks.grid(row=3, column=1)

window.mainloop()
