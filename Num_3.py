products = [300, 500, 400, 30, 100]
res = 0
n = ''
from tkinter import *

window = Tk()
window.title('cashier')
window.geometry("400x400")

lst = ['Laptop:300$', 'P.C.:500$', 'IPhone 13:400$', 'Powerbank:30$', 'Headphones:100$']
list_box = Listbox(listvariable = Variable(value=lst))
list_box.place(x=30 , y=30 , height=80)

def set():
        global res
        global n
        if list_box.curselection() == (0,):
               n = 0
        elif list_box.curselection() == (1,):
               n = 1
        elif list_box.curselection() == (2,):
               n = 2
        elif list_box.curselection() == (3,):
               n = 3
        elif list_box.curselection() == (4,):
               n = 4

        res += int(products[n]) * int(entry_number.get())
        lable_res_1.config(text=res)
    
def reset():
      global res
      res = 0
      lable_res_1.config(text=res)


entry_number = Entry(width=10)
entry_number.place(x=180, y=60)

lable_sht = Label(text='th.')
lable_sht.place(x=240, y=60)

button_set = Button(text='SET', command=set)
button_set.place(x=280, y=56)

button_reset = Button(text='Reset', command=reset)
button_reset.place(x=30, y=120)

lable_res = Label(text='Res:')
lable_res.place(x=30, y=150)

lable_res_1 = Label(text=0)
lable_res_1.place(x=60, y=150)


window.mainloop()