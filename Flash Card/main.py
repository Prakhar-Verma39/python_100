from tkinter import *
import random
import pandas
from pandas.errors import EmptyDataError

BACKGROUND_COLOR = "#b1ddc6"
data = None
random_word = {}
data_dict_list = {}
try:
    data = pandas.read_csv("data/words_to_learn.csv")
except (FileNotFoundError, pandas.errors.EmptyDataError):
    original_data = pandas.read_csv("data/hindi_words.csv")
    data_dict_list = original_data.to_dict(orient="records")
else:
    data_dict_list = data.to_dict(orient="records")


# ------------------------------ REMOVE CORRECT WORD ------------------------------------ #
def correct_word():
    data_dict_list.remove(random_word)
    df = pandas.DataFrame(data_dict_list)
    df.to_csv("data/words_to_learn.csv", index=False)
    generate_random_word()


# ------------------------------ RANDOM WORD GENERATOR -------------------------- #
def generate_random_word():
    global random_word, flip_timer
    window.after_cancel(flip_timer)
    if len(data_dict_list) > 0:
        random_word = random.choice(data_dict_list)
    canvas.itemconfig(canvas_image, image=old_image)
    canvas.itemconfig(card_title, text="Hindi", fill="black")
    canvas.itemconfig(card_word, text=f"{random_word['Hindi']} ({random_word['Transliteration']})", fill="black")
    window.after(3000, func=flip_card)


# ------------------------------ FLIP CARD -------------------------- #
def flip_card():
    canvas.itemconfig(canvas_image, image=new_image)
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_word, text=random_word["English"], fill="white")


# ------------------------------ UI SETUP -------------------------- #
window = Tk()
window.title("FLASH CARD")
window.minsize()
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

flip_timer = window.after(3000, func=flip_card)

canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)

old_image = PhotoImage(file="images/card_front.png")
new_image = PhotoImage(file="images/card_back.png")
canvas_image = canvas.create_image(400, 263, image=old_image)
card_title = canvas.create_text(400, 150, text="item", font=("Ariel", 40, "italic"))
card_word = canvas.create_text(400, 263, text="word", font=("Ariel", 60, "bold"))
canvas.grid(column=1, row=1, columnspan=2)

rt = PhotoImage(file="images/right.png")
right_button = Button(image=rt, highlightthickness=0, command=correct_word)
right_button.grid(column=2, row=2)
wt = PhotoImage(file="images/wrong.png")
wrong_button = Button(image=wt, highlightthickness=0, command=generate_random_word)
wrong_button.grid(column=1, row=2)

generate_random_word()

window.mainloop()
