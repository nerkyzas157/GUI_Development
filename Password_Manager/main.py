# Import requirments
import tkinter
import random
import tkinter.messagebox
import pyperclip  # type: ignore
import json


# ---------------------------- PULL PASSWORD ------------------------------- #
def pull_pass():
    website = website_entry.get()
    if len(website) == 0:
        website = "Website/Portal"
    email_username = eu_entry.get()
    try:
        with open("data.json", mode="r") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        tkinter.messagebox.showwarning(
            title="Error",
            message="Database is empty. Please add login credentials.",
        )
    else:
        with open("data.json", mode="r") as data_file:
            data = json.load(data_file)
            if website in data and email_username in data[website]["email/username"]:
                password_entry.delete(0, tkinter.END)
                password = data[website]["password"]
                password_entry.insert(0, password)
                pyperclip.copy(password)
                tkinter.messagebox.showinfo(
                    title=website,
                    message=f"Password was added to the clipboard.",
                )
            elif website not in data:
                tkinter.messagebox.showwarning(
                    title="No Results",
                    message=f"There are no credentials added for {website}.",
                )
            elif email_username not in data[website]["email/username"]:
                tkinter.messagebox.showwarning(
                    title="No Results",
                    message=f"Email/Username does not match the {website} login credentials.",
                )


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
LETTERS = [
    "a",
    "b",
    "c",
    "d",
    "e",
    "f",
    "g",
    "h",
    "i",
    "j",
    "k",
    "l",
    "m",
    "n",
    "o",
    "p",
    "q",
    "r",
    "s",
    "t",
    "u",
    "v",
    "w",
    "x",
    "y",
    "z",
    "A",
    "B",
    "C",
    "D",
    "E",
    "F",
    "G",
    "H",
    "I",
    "J",
    "K",
    "L",
    "M",
    "N",
    "O",
    "P",
    "Q",
    "R",
    "S",
    "T",
    "U",
    "V",
    "W",
    "X",
    "Y",
    "Z",
]
NUMBERS = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
SYMBOLS = ["!", "#", "$", "%", "&", "(", ")", "*", "+"]


def pass_gen():
    letters = random.choices(LETTERS, k=random.randint(8, 10))
    symbols = random.choices(NUMBERS, k=random.randint(2, 4))
    numbers = random.choices(SYMBOLS, k=random.randint(2, 4))
    pw = list(letters + symbols + numbers)
    random.shuffle(pw)
    password = "".join(pw)
    pyperclip.copy(password)
    password_entry.delete(0, tkinter.END)
    password_entry.insert(0, password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_password():
    website = website_entry.get()
    password = password_entry.get()
    email_username = eu_entry.get()
    new_data = {website: {"email/username": email_username, "password": password}}
    # Pop-Up (Standard Dialogs)
    if website == "" or password == "" or email_username == "":
        tkinter.messagebox.showerror(
            title="Oops", message="Please don't leave any fields empty."
        )
    else:
        confirm = tkinter.messagebox.askokcancel(
            title=website,
            message=f"These are the details entered:\nEmail: {email_username}\nPassword: {password}\nIs it okay to save?",
        )
        if confirm:
            try:
                with open(
                    "data.json", mode="r"
                ) as data_file:
                    data = json.load(data_file)
            except FileNotFoundError:
                with open(
                    "data.json", mode="w"
                ) as data_file:
                    json.dump(new_data, data_file, indent=4)
            else:
                with open(
                    "data.json", mode="r"
                ) as data_file:
                    data = json.load(data_file)
                    data.update(new_data)
                with open(
                    "data.json", mode="w"
                ) as data_file:
                    json.dump(new_data, data_file, indent=4)
            finally:
                website_entry.delete(0, tkinter.END)
                password_entry.delete(0, tkinter.END)
                tkinter.messagebox.showinfo(
                    title=website,
                    message=f"Credentials were saved successfully.",
                )


# ---------------------------- UI SETUP ------------------------------- #
# Window
window = tkinter.Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

# Image
canvas = tkinter.Canvas(width=200, height=200, highlightthickness=0)
logo_img = tkinter.PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(column=1, row=0)

# Labels
website_label = tkinter.Label(text="Website:")
website_label.grid(column=0, row=1)
eu_label = tkinter.Label(text="Email/Username:")
eu_label.grid(column=0, row=2)
password_label = tkinter.Label(text="Password:")
password_label.grid(column=0, row=3)

# Entry boxes
website_entry = tkinter.Entry(width=32)
website_entry.grid(column=1, row=1)
website_entry.focus()
eu_entry = tkinter.Entry(width=50)
eu_entry.insert(0, "email@email.com")
eu_entry.grid(column=1, row=2, columnspan=2)
password_entry = tkinter.Entry(width=32)
password_entry.grid(column=1, row=3)

# Buttons
gen_pass_button = tkinter.Button(text="Generate Password", width=14, command=pass_gen)
gen_pass_button.grid(column=2, row=3)
add_button = tkinter.Button(text="Add", width=43, command=save_password)
add_button.grid(column=1, row=4, columnspan=2)
search_button = tkinter.Button(text="Search", width=14, command=pull_pass)
search_button.grid(column=2, row=1)

# Window loop
window.mainloop()
