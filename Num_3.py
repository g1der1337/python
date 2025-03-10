from tkinter import *

window = Tk()
window.geometry("600x500")
window.config(bg="#78c1c4")

canV = Canvas(height=500 , width=600 , bg="#78c1c4")
canV.place(x=0 , y=0)

entry = Entry()
entry.place(x=250, y=50)

def fun():
    canV.create_text(302 , 202 , text=entry.get() , justify = "center" , font="Georgia 15" , fill="#837d7d")
    canV.create_text(300 , 200 , text=entry.get() , justify = "center" , font="Georgia 15" , fill="#ff0000")
    
button = Button(text='вывести', command=fun)
button.place(x=270, y=100)

window.mainloop()
