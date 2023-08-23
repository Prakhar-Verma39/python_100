from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip

# ------------------------------- PASSWORD GENERATOR --------------------------#


def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
    password = ""

    password += "".join([choice(letters) for _ in range(randint(8, 10))]) + "".join(
        [choice(symbols) for _ in range(randint(2, 4))]) + "".join([choice(numbers) for _ in range(randint(2, 4))])

    # Need a list to perform shuffling via random module shuffle method
    password = list(password)

    # Perform shuffling via random module shuffle method
    shuffle(password)

    # Convert list to string
    password = ''.join(password)

    # Print password as a String
    password_entry.insert(0, password)
    pyperclip.copy(password)


# ------------------------------- SAVE PASSWORD --------------------------#
def add_data():
    # inputs
    web_data = website_entry.get()
    email_data = email_entry.get()
    password_data = password_entry.get()

    if len(web_data) == 0 or len(password_data) == 0:
        messagebox.showinfo(title="Oh! No", message="Please dont leave any fields empty!")
    else:
        is_ok = messagebox.askokcancel(title=web_data,
                                       message=f'These are the details entered: \nEmail: {email_data} \nPassword:'
                                               f' {password_data} \nIs it ok to save?')

        if is_ok:
            with open("data.txt", mode='a') as f:
                f.write(f"{web_data} | {email_data} | {password_data}\n")
                website_entry.delete(0, END)
                password_entry.delete(0, END)


# ------------------------------- UI SETUP -------------------------#

window = Tk()
window.title("Passo")
window.config(padx=50, pady=50)

canvas = Canvas(height=240, width=300)
pt = PhotoImage(file='open-and-closed-lock.png')
canvas.create_image(130, 130, image=pt)
canvas.grid(column=2, row=1, columnspan=2)

# labels
website_label = Label(text="Website:")
website_label.grid(column=1, row=2)

email_label = Label(text="Email/Username:")
email_label.grid(column=1, row=3)

password_label = Label(text="Password:")
password_label.grid(column=1, row=4)

# entries
website_entry = Entry(width=45)
website_entry.grid(column=2, row=2, columnspan=2)
website_entry.focus()

email_entry = Entry(width=45)
email_entry.grid(column=2, row=3, columnspan=2)
email_entry.insert(0, "dummy@gmail.com")

password_entry = Entry(width=22)
password_entry.grid(column=2, row=4)

# buttons
password_button = Button(text="Generate Password", width=15, command=generate_password)
password_button.grid(column=3, row=4)

add_button = Button(text="Add", width=38, command=add_data)
add_button.grid(column=2, row=5, columnspan=2)

window.mainloop()
