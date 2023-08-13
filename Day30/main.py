# Password Manager GUI in JSON File
from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image
import random
import pyperclip
import json


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


# ---------------------------- SEARCH EMAIL ------------------------------- #

def search_password():
    try:
        with open("password.json", "r") as search_file:
            website_name = website_entry.get()
            data = json.load(search_file)

    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="PASSWORD FILE IS NOT FOUND")

    else:
        if website_name in data:
            web_data = data[website_name]
            email = web_data['email']
            password = web_data['password']
            messagebox.showinfo(title=website_name, message=f"Email: {email}\nPassword: {password}")
        else:
            messagebox.showinfo(title="Error", message=f"NO DETAILS ON \"{website_name}\"")


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_password():
    email = email_entry.get()
    website = website_entry.get()
    password_data = password_entry.get()
    new_data = {
        website:
            {
                "email": email,
                "password": password_data,
            }
    }

    if len(website) < 1 or len(password_data) < 1:
        messagebox.showinfo(title="", message="You can't have empty website/password")
        return

    else:
        try:
            with open("password.json", mode="r") as pass_file:
                data = json.load(pass_file)

        except FileNotFoundError:
            with open("password.json", 'w') as pass_file:
                json.dump(new_data, pass_file, indent=4)

        except json.decoder.JSONDecodeError:
            with open("password.json", 'w') as pass_file:
                json.dump(new_data, pass_file, indent=4)

        else:
            data.update(new_data)
            with open("password.json", mode="w") as pass_file:
                json.dump(data, pass_file, indent=4)
                messagebox.showinfo(message="Your password details has been saved successfully")

        finally:
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
website_label = Label(text="Website:")
website_label.grid(row=1, column=0)
website_entry = Entry(width=21)
website_entry.grid(row=1, column=1, sticky="EW")
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

# Search Button
search_button = Button(text="Search", command=search_password)
search_button.grid(row=1, column=2, sticky="EW")

# Add Button
add_button = Button(text="Add", width=36, command=save_password)
add_button.grid(row=4, column=1, columnspan=2, sticky="EW")

window.mainloop()
