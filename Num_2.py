from tkinter import *
from random import randrange

window = Tk()
window.title('0')
window.geometry("600x500")
window.config(bg="#FFF")


canV = Canvas(height=500 , width=600 , bg="#2F4F4F")
canV.place(x=0 , y=0)

n = -1

robot_obj = {
    "x1" :0,
    "y1" :0,
    "x2" :50,
    "y2" :50,
}

canV.create_rectangle(robot_obj["x1"] , robot_obj["y1"], robot_obj["x2"] , robot_obj["y2"] , fill="#2e5bff" , width=0)

rand_x = randrange(0 , 11)
rand_y = randrange(0 , 9)
coin_obj = {
    "x1" : 50 * rand_x,
    "y1" :50 * rand_y,
    "x2" : (50 * rand_x) + 50,
    "y2" :(50 * rand_y) + 50,
}
    
def reset():
    global n 
    rand_x = randrange(0 , 11)
    coin_obj['x1'] = rand_x * 50
    coin_obj['y1'] = rand_y * 50
    coin_obj['x2'] = (rand_x * 50) + 50
    coin_obj['y2'] = (rand_y * 50) + 50
    canV.create_rectangle(0,0, 600 , 500, fill="#fff" , width=0)
    canV.create_oval(coin_obj["x1"] , coin_obj["y1"], coin_obj["x2"] , coin_obj["y2"] , fill="#FFD700" , width=0)
    canV.create_rectangle(robot_obj["x1"] , robot_obj["y1"], robot_obj["x2"] , robot_obj["y2"] , fill="#2e5bff" , width=0)
    n += 1
    window.title(n)

def fun(event):
    # print(event.keycode)
    global coin_obj
    if(event.keycode == 83 and robot_obj["y2"] < 500):
        robot_obj["y1"] += 50
        robot_obj["y2"] += 50
    if(event.keycode == 68 and robot_obj["x2"] < 600):
        robot_obj["x1"] += 50
        robot_obj["x2"] += 50
    if(event.keycode == 87 and robot_obj["y1"] > 0):
        robot_obj["y1"] -= 50
        robot_obj["y2"] -= 50
    if(event.keycode == 65 and robot_obj["x1"] > 0):
        robot_obj["x1"] -= 50
        robot_obj["x2"] -= 50
    
    
    # print(coin_obj["x1"], robot_obj["x1"])
    # print(coin_obj["y1"], robot_obj["y1"])
    # print(coin_obj["x2"], robot_obj["x2"])
    # print(coin_obj["y2"], robot_obj["y2"])
    canV.create_rectangle(0,0, 600 , 500, fill="#fff" , width=0)
    canV.create_oval(coin_obj["x1"] , coin_obj["y1"], coin_obj["x2"] , coin_obj["y2"] , fill="#FFD700" , width=0)
    canV.create_rectangle(robot_obj["x1"] , robot_obj["y1"], robot_obj["x2"] , robot_obj["y2"] , fill="#2e5bff" , width=0)

    
    if (coin_obj["x1"] == robot_obj["x1"]) and (coin_obj["y1"] == robot_obj["y1"]) and (coin_obj["x2"] == robot_obj["x2"]) and (coin_obj["y2"] == robot_obj["y2"]):
        # print('sdjadjasbkd')
        reset()

reset()
window.bind("<KeyPress>" , fun)

window.mainloop()