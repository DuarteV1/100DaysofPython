from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"
FONT_NAME = "Ariel"
to_learn = {}

# -------------------------- READ FILE --------------------------------- #
try:
    words = pandas.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    words = pandas.read_csv("data/french_words.csv")
    to_learn = {row.French: row.English for (index, row) in words.iterrows()}
else:
    to_learn = {row.French: row.English for (index, row) in words.iterrows()}
# words_df = pandas.DataFrame(words)
# to_learn = {row.French: row.English for (index, row) in words.iterrows()}
# print(to_learn)
# alternativamente posso usar to_learn = data.to_dict(orient="records")
current_card = {}


def random_word():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    key, value = random.choice(list(to_learn.items()))
    canvas.itemconfig(word, text=key, fill="black")
    canvas.itemconfig(title, text="French", fill="black")
    current_card = {"French": key, "English": value}
    print(current_card)
    canvas.itemconfig(card_front_img, image=front_img)
    window.after(3000, func=flip_card)


def flip_card():
    canvas.itemconfig(title, text="English", fill="white")
    canvas.itemconfig(word, text=current_card["English"], fill="white")
    canvas.itemconfig(card_front_img, image=back_img)


def is_known():
    to_learn.pop(current_card["French"])
    print(len(to_learn))
    print(to_learn)
    df = pandas.DataFrame(list(to_learn.items()), columns=["French", "English"])
    df.to_csv("data/words_to_learn.csv")
    print(df)
    random_word()


# Graphic User Interface

window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

flip_timer = window.after(3000, func=flip_card)

# To import images, Canvas method must be used in order to lay images on the window
# The dimensions could be checked by opening the card_front.png and see 800x526 PNG
canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)

# Card Back and Front Image
front_img = PhotoImage(file="./images/card_front.png")
back_img = PhotoImage(file="./images/card_back.png")
card_front_img = canvas.create_image(400, 263, image=front_img)

canvas.grid(column=0, row=0, columnspan=2)

# LABELS (Têm de vir a seguir da imagem, senão fica escondida atrás dela)
title = canvas.create_text(400, 150, text="title", fill="black", font=(FONT_NAME, 40, "italic"))
word = canvas.create_text(400, 263, text="French", fill="black", font=(FONT_NAME, 60, "bold"))


# Right and Wrong Button
right_img = PhotoImage(file="./images/right.png")
right_button = Button(image=right_img, highlightthickness=0, command=is_known)
right_button.grid(column=0, row=1)

wrong_img = PhotoImage(file="./images/wrong.png")
wrong_button = Button(image=wrong_img, highlightthickness=0, command=random_word)
wrong_button.grid(column=1, row=1)

random_word()


window.mainloop()
