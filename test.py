
from tkinter import *

window = Tk()
window.title('cashier')
window.geometry("600x500")
window.config(bg="#ffec19")



# создание элемента Canvas
canV = Canvas(height=500 , width=600 , bg="#fff")
canV.place(x=0 , y=0)
# рисуем в Canvas с помощью методов

canV.create_text(200 , 300 , text="wertyui\nowguwuegefe\nefefeff\,efee\nefefefef" , justify = "center" , font="Georgia 15" , fill="#21B297")



window.mainloop()
