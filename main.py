from tkinter import *
import requests
import random


def get_quote():
    response=requests.get(url=f"https://bhagavadgitaapi.in/slok/{random.randint(1,18)}/{random.randint(1,20)}")
    if 200 == response.status_code:
        data=response.json()["slok"]
        canvas.itemconfigure(quote_text, text= data)
    else:
        return response.raise_for_status()



window = Tk()
window.title("Bhagavad Gita...")
window.config(padx=50, pady=50)

canvas = Canvas(width=300, height=414)
background_img = PhotoImage(file="bg.png")
canvas.create_image(150, 207, image=background_img)
quote_text = canvas.create_text(150, 207, text="Every day, let the wise teachings of the Gita help you along your path.\n\n  - SANSKRIT.", width=250, font=("courier new 12 old", 13, ), fill="black")
canvas.grid(row=0, column=0)

kanye_img = PhotoImage(file="book.png")
kanye_button = Button(image=kanye_img, highlightthickness=0, command=get_quote)
kanye_button.grid(row=1, column=0)



window.mainloop()
