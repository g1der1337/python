# from tkinter import *
# clicks = 0
# def click():
#     global clicks
#     clicks += 1

# window = Tk()
# window.title("Кликер")
# window.geometry("300x200")

# click_button = Button(window, text="Клик", command='click()')
# click_button.pack()

# label = Label(window, text=clicks)
# label.pack()

# window.mainloop()

from tkinter import *
import random

window = Tk()
window.title("Игра")
window.geometry("500x500") 

def move_button():
    x = random.randint(10, 490)
    y = random.randint(10, 490)

    button.place(x=x, y=y)

button = Button(window, text="опа", command=move_button)
button.grid()

move_button() 
window.mainloop()  