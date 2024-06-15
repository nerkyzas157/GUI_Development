# Importing requirments
import tkinter
import math

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 20
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None


# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    global reps
    window.after_cancel(timer)
    reps = 0
    canvas.itemconfig(clock, text="00:00")
    label.config(text="Timer", fg=GREEN)
    check.config(text="")


# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global reps
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60
    reps += 1
    if reps % 8 == 0:
        label.config(text="Break", fg=RED)
        count_down(long_break_sec)
    elif reps % 2 == 0:
        label.config(text="Break", fg=PINK)
        count_down(short_break_sec)
    else:
        label.config(text="Work", fg=GREEN)
        count_down(work_sec)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    minutes = math.floor(count / 60)
    seconds = count % 60
    if seconds < 10:
        seconds = f"0{seconds}"
    canvas.itemconfig(clock, text=f"{minutes}:{seconds}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        check_mark = ""
        for i in range(math.floor(reps / 2)):
            check_mark += "✔"
        check.config(text=check_mark)


# ---------------------------- UI SETUP ------------------------------- #
# Window:
window = tkinter.Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)


# Image and clock:
canvas = tkinter.Canvas(width=210, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = tkinter.PhotoImage(file="tomato.png")
canvas.create_image(105, 112, image=tomato_img)
clock = canvas.create_text(
    105, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold")
)
canvas.grid(column=1, row=1)

# Label
label = tkinter.Label(
    text="Timer",
    font=(FONT_NAME, 40, "bold"),
    fg=GREEN,
    bg=YELLOW,
    highlightthickness=0,
)
label.grid(column=1, row=0)

# Check mark:
check = tkinter.Label(
    font=(FONT_NAME, 12, "bold"), fg=GREEN, bg=YELLOW, highlightthickness=0
)
check.grid(column=1, row=3)

# Start button:
start_button = tkinter.Button(text="Start", command=start_timer)
start_button.grid(column=0, row=2)

# Reset button:
reset_button = tkinter.Button(text="Reset", command=reset_timer)
reset_button.grid(column=2, row=2)

# Set window() open:
window.mainloop()
