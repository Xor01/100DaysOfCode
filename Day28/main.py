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

# ---------------------------- TIMER RESET ------------------------------- # 

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start():
    pass


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

# ---------------------------- UI SETUP ------------------------------- #
# Window part
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

# Label Timer

timer_label = Label(text="Timer", fg=GREEN, bg=YELLOW)
timer_label.grid(row=0, column=1)
timer_label.config(font=(FONT_NAME, 40, "bold"))


# Canvas part
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_photo = ImageTk.PhotoImage(Image.open("tomato.png"))
canvas.create_image(100, 112, image=tomato_photo)
canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 24, "bold"))
canvas.grid(row=1, column=1)

# Start Button
start_button = Button(text="Start", fg="black", command=start, bg=YELLOW)
start_button.grid(row=2, column=0)

# Reset Button
reset_button = Button(text="Reset", fg="black", bg=YELLOW)
reset_button.grid(row=2, column=2)


# Check marks

check_marks = Label(text="✔", bg=YELLOW, fg=GREEN)
check_marks.grid(row=3, column=1)
check_marks.config(padx=10)

window.mainloop()
