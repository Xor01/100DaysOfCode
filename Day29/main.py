from tkinter import *
from PIL import ImageTk, Image


# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_password():
    with open("password.txt", mode="a") as pass_file:
        pass_file.write(f"{website_entry.get()} | {email_entry.get()} | {password_entry.get()}\n")
    website_entry.delete(0, END)
    password_entry.delete(0, END)
    website_entry.focus()

# ---------------------------- UI SETUP ------------------------------- #

# Window Component
window = Tk()
window.title("Password Manager")
window.config(pady=50, padx=50)

# Canvas Component
canvas = Canvas(width=200, height=200)
logo_image = ImageTk.PhotoImage(Image.open("logo.png"))
canvas.create_image(100, 100, image=logo_image)
canvas.grid(row=0, column=1)

# Website Component
website_label = Label(text="Website")
website_label.grid(row=1, column=0)
website_entry = Entry(width=35)
website_entry.grid(row=1, column=1, columnspan=2, sticky="EW")
website_entry.focus()

# Email Component
email_label = Label(text="Email/user Name")
email_label.grid(row=2, column=0)

email_entry = Entry(width=35)
email_entry.grid(row=2, column=1, columnspan=2, sticky="EW", )
email_entry.insert(0, string="m@m.com")

# Password Component
password_label = Label(text="Password")
password_label.grid(row=3, column=0)
password_entry = Entry(width=21)
password_entry.grid(row=3, column=1, sticky="EW")

# Password Button
password_button = Button(text="Generate Password")
password_button.grid(row=3, column=2, sticky="EW")

# Add Button
add_button = Button(text="Add", width=36, command=save_password)
add_button.grid(row=4, column=1, columnspan=2, sticky="EW")

window.mainloop()
