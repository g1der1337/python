from tkinter import *
window = Tk()
window.title = 'Calculator'
window.geometry = '400600'
# window.config(bg="#e4ffa6")

first_numb = Entry()
first_numb.place(x=30, y=30)

second_numb = Entry()
second_numb.place(x=30, y=70)

def plus1():
    n =int(first_numb.get()) + int(second_numb.get())
    labell.config(text=n)

def minus1():
    n =int(first_numb.get()) - int(second_numb.get())
    labell.config(text=n)

def multiply1():
    n =int(first_numb.get()) * int(second_numb.get())
    labell.config(text=n)

def split1():
    n =int(first_numb.get()) / int(second_numb.get())
    labell.config(text=n)

plus = Button(text='+', command=plus1)
plus.place(x=30, y=110)

minus = Button(text='-', command=minus1)
minus.place(x=65, y=110)

multiply = Button(text='*',command=multiply1)
multiply.place(x=100, y=110)

split = Button(text=':', command=split1)
split.place(x=135, y=110)

labell = Label(text='')
labell.place(x=80, y=150)


window.mainloop()