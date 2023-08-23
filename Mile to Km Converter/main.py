from tkinter import *

# creating a window object
window = Tk()
window.title("Mile to Km Converter")
window.config(padx=20, pady=20)

# Label no. 1
label_1 = Label(text="is equal to", font=('Arial', 16))
label_1.grid(column=1, row=2)

# entry class
in_miles = Entry(width=10, font=('Arial', 16))
in_miles.grid(column=2, row=1)

# label no. 2
label_2 = Label(text="Miles", font=('Arial', 16))
label_2.grid(column=3, row=1)


def calculate():
    miles = float(in_miles.get())
    label_3.config(text =f"{round((int(miles)*1.60934), 2)}")


# label no. 3
label_3 = Label(text="0", font=('Arial', 16))
label_3.grid(column=2, row=2)

# label no. 4
label_4 = Label(text="Km", font=('Arial', 16))
label_4.grid(column=3, row=2)

# button
bt = Button(text="Calculate",font=('Arial', 16), command=calculate)
bt.grid(column=2, row=3)

# to keep the window open
window.mainloop()