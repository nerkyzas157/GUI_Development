import tkinter

# Created window:
window = tkinter.Tk()

window.title("Mile to Km Converter")
window.minsize(width=300, height=100)
window.config(padx=60, pady=30)

# Entry:
miles_input = tkinter.Entry(width=10)
miles_input.grid(column=1, row=0)

# Labels:
label1 = tkinter.Label(text="Miles", font=("Arial", 12))
label1.grid(column=2, row=0)

label1 = tkinter.Label(text="is equal to", font=("Arial", 12))
label1.grid(column=0, row=1)

label2 = tkinter.Label(text="0", font=("Arial", 12))
label2.grid(column=1, row=1)

label3 = tkinter.Label(text="Km", font=("Arial", 12))
label3.grid(column=2, row=1)


# Button to convert Miles to Kilometers
def button_clicked():
    miles = float(miles_input.get())
    if miles > 0:
        label2.config(text=round(miles * 1.609, 2))


button = tkinter.Button(text="Calculate", command=button_clicked)
button.grid(column=1, row=2)

# Must keep as the last fn, it keeps the window open:
window.mainloop()
