# Importing requirements
import pandas  # type: ignore
import tkinter
import random
import tkinter.messagebox
import os

# Creating New Flash Cards
try:
    data = pandas.read_csv("data\\words_to_learn.csv")
except FileNotFoundError:
    data = pandas.read_csv("data\\french_words.csv")
finally:
    cards_to_learn = data.to_dict(orient="records")
timer = None


def new_word():
    global current_card, timer
    try:
        current_card = random.choice(cards_to_learn)
    except IndexError:
        pass
    canvas.itemconfig(card, image=card_front)
    canvas.itemconfig(title, text="French", fill="#000000")
    canvas.itemconfig(text, text=current_card["French"], fill="#000000")
    timer = window.after(3000, flip_card)


# Fliping the Cards
def flip_card():
    window.after_cancel(timer)
    global current_card
    canvas.itemconfig(card, image=card_back)
    canvas.itemconfig(title, text="English", fill="#fff")
    canvas.itemconfig(text, text=current_card["English"], fill="#fff")


# Removing learned words
def learned_word():
    window.after_cancel(timer)
    global current_card
    if len(cards_to_learn) == 0:
        tkinter.messagebox.showwarning(
            title="Warning",
            message="Congratulations! You've learned all imported the words.",
        )
        # path = "Day_31_Flash_Card_App\\data\\words_to_learn.csv"
        os.remove("data\\words_to_learn.csv")
        return window.destroy()
    cards_to_learn.remove(current_card)
    df = pandas.DataFrame(cards_to_learn)
    # newdf = df.drop("age", axis='columns')
    df.to_csv("data\\words_to_learn.csv", index=False)
    new_word()


# Creating User Interface
BACKGROUND_COLOR = "#B1DDC6"

# Window
window = tkinter.Tk()
window.title("Flash Card App")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

# The card
canvas = tkinter.Canvas(
    width=800, height=530, highlightthickness=0, bg=BACKGROUND_COLOR
)
card_front = tkinter.PhotoImage(file="images\\card_front.png")
card_back = tkinter.PhotoImage(file="images\\card_back.png")
card = canvas.create_image(400, 265, image=card_front)
canvas.grid(column=0, row=0, columnspan=2)
title = canvas.create_text(400, 155, text="", font=("Ariel", 40, "italic"))
text = canvas.create_text(400, 265, text="", font=("Ariel", 60, "bold"))

# Right button
right_image = tkinter.PhotoImage(file="images\\right.png")
right_button = tkinter.Button(
    image=right_image, highlightthickness=0, bg=BACKGROUND_COLOR, command=learned_word
)
right_button.grid(column=1, row=1)

# Wrong button
wrong_image = tkinter.PhotoImage(file="images\\wrong.png")
wrong_button = tkinter.Button(
    image=wrong_image, highlightthickness=0, bg=BACKGROUND_COLOR, command=new_word
)
wrong_button.grid(column=0, row=1)

# Start learning
new_word()

# Window loop
window.mainloop()
