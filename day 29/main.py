from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip
import json


# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers
    shuffle(password_list)

    password = "".join(password_list)
    pass_ent.insert(0, password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    web = web_ent.get()
    email = email_ent.get()
    password = pass_ent.get()
    new_data = {
        web: {
            "email": email,
            "password": password,
        }}

    if len(web) == 0 or len(password) == 0:
        messagebox.showinfo(title="Empty Fields", message="Please fill the required info")
    else:
        try:
            with open("data.json", "r") as data_file:
                ##Read
                data = json.load(data_file)
        except FileNotFoundError:
            with open("data.json", "w") as data_file:
                ##Save
                json.dump(new_data, data_file, indent=4)
        else:
            data.update(new_data)

            with open("data.json", "w") as data_file:
                ##Save
                json.dump(data, data_file, indent=4)

        finally:
            web_ent.delete(0, END)
            pass_ent.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=20, pady=40)

canvas = Canvas(height=200, width=200)
canvas = Canvas(width=200, height=224, highlightthickness=0)
logo_img = PhotoImage(file="lock.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(row=0, column=1)

# LABELS
web_lab = Label(text="Website:")
web_lab.grid(row=1, column=0)
email_lab = Label(text="Username:")
email_lab.grid(row=2, column=0)
pass_lab = Label(text="Password:")
pass_lab.grid(row=3, column=0)

# Entries
web_ent = Entry(width=35)
web_ent.grid(row=1, column=1, columnspan=2)
web_ent.focus()
email_ent = Entry(width=35)
email_ent.grid(row=2, column=1, columnspan=2)
email_ent.insert(0, "abc@ac.com")
pass_ent = Entry(width=35)
pass_ent.grid(row=3, column=1, columnspan=2)

# Buttons
gen_pass = Button(text="Generate Password", command=generate_password)
gen_pass.grid(row=3, column=2)
add_button = Button(text="Add", width=15, command=save)
add_button.grid(row=4, column=1)

window.mainloop()
