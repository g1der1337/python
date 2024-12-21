user = {}
from tkinter import *

window = Tk()
window.title = 'Calculator'
window.geometry("200x200")

lable_login = Label(text= 'Login:')
lable_login.pack()

entry_login = Entry()
entry_login.pack()

lable_password = Label(text= 'Password:')
lable_password.pack()

entry_password = Entry()
entry_password.pack()

def regist():
    n = entry_login.get()
    user[n] = entry_password.get()
    res.config(text='You are logged')
    
def loginn():
    n = entry_login.get()
    if (entry_password.get() in user) and (user[n] == entry_password.get()):
        res.config(text='You are logged')
    else:
        res.config(text='There is no such account')

login = Button(text='Login', command=loginn)
login.pack()

registration = Button(text='Reg', command=regist)
registration.pack()

res = Label()
res.pack()

window.mainloop()