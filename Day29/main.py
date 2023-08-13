# Password Manager GUI in TXT File
from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image
import random
import pyperclip


# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v',
               'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q',
               'R',
               'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_list = [random.choice(letters) for _ in range(nr_letters)]
    password_list += [random.choice(symbols) for _ in range(nr_symbols)]
    password_list += [random.choice(numbers) for _ in range(nr_numbers)]

    random.shuffle(password_list)

    password = "".join(password_list)
    password_entry.delete(0, END)
    password_entry.insert(0, password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_password():
    email = email_entry.get()
    website = website_entry.get()
    password_data = password_entry.get()

    if len(website) < 1 or len(password_data) < 1:
        messagebox.showinfo(title="", message="You can't have empty website/password")
        return

    message = messagebox.askokcancel(title=website, message=f"Want to save\n Email: {email}\n Password:{password_data}")

    if message:
        with open("password.txt", mode="a") as pass_file:
            pass_file.write(f"{website} | {email} | {password_data}\n")
        website_entry.delete(0, END)
        password_entry.delete(0, END)
        website_entry.focus()
        messagebox.showinfo(message="Your password details has been saved successfully")


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
website_label = Label(text="Website:")
website_label.grid(row=1, column=0)
website_entry = Entry(width=35)
website_entry.grid(row=1, column=1, columnspan=2, sticky="EW")
website_entry.focus()

# Email Component
email_label = Label(text="Email/user Name:")
email_label.grid(row=2, column=0)

email_entry = Entry(width=35)
email_entry.grid(row=2, column=1, columnspan=2, sticky="EW", )
email_entry.insert(0, string="m@m.com")

# Password Component
password_label = Label(text="Password:")
password_label.grid(row=3, column=0)
password_entry = Entry(width=21)
password_entry.grid(row=3, column=1, sticky="EW")

# Password Button
password_button = Button(text="Generate Password", command=generate_password)
password_button.grid(row=3, column=2, sticky="EW")

# Add Button
add_button = Button(text="Add", width=36, command=save_password)
add_button.grid(row=4, column=1, columnspan=2, sticky="EW")

window.mainloop()
