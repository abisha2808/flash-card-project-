from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"

data = pandas.read_csv("data/french_words.csv")
data_dict = data.to_dict(orient="records")
current_card = random.choice(data_dict)


def next_card():
    global flip_timer
    windows.after_cancel(flip_timer)
    canvas.itemconfigure(title_canvas, text="French")
    canvas.itemconfigure(word_canvas, text=current_card["French"])
    canvas.itemconfigure(image_canvas, image=front_photo)
    flip_timer = windows.after(3000, func=flip_card)

def remove_card():
    data_dict.remove(current_card)

    file = pandas.DataFrame()
    next_card()



def flip_card():
    canvas.itemconfigure(title_canvas, text="English")
    canvas.itemconfigure(word_canvas, text=current_card["English"])
    canvas.itemconfigure(image_canvas, image=back_photo)


windows = Tk()
windows.title("Flashy")
windows.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
flip_timer = windows.after(3000, func=flip_card)

canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
front_photo = PhotoImage(file="images/card_front.png")
back_photo = PhotoImage("images/card_back.png")
image_canvas = canvas.create_image(400, 213, image=front_photo)
canvas.grid(row=0, column=0, columnspan=2)

title_canvas = canvas.create_text(400, 150, text="title", font=("Ariel", 40, "italic"))

word_canvas = canvas.create_text(400, 263, text="word", font=("Ariel", 60, "bold"))

right_photo = PhotoImage(file="images/right.png")
right_button = Button(image=right_photo, highlightthickness=0, command=remove_card)
right_button.grid(row=1, column=1)

wrong_photo = PhotoImage(file="images/wrong.png")
wrong_button = Button(image=wrong_photo, highlightthickness=0, command=next_card)
wrong_button.grid(row=1, column=0)

next_card()

windows.mainloop()
