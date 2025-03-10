from tkinter import *

def update_arc(*args):
    canvas.delete("arc")
    size = size_scale.get()
    angle = angle_scale.get()
    canvas.create_arc(100, 100, 100 + size, 100 + size, start=0, extent=angle, outline='#0882a0', width=3, style=ARC, tags="arc")

root = Tk()
root.title("Дуга с управлением")

canvas = Canvas(root, width=300, height=300, bg='#ffffff')
canvas.pack()

size_scale = Scale(root, from_=50, to=200, orient=HORIZONTAL, label="Размер", command=update_arc)
size_scale.pack()
size_scale.set(100)

angle_scale = Scale(root, from_=0, to=360, orient=HORIZONTAL, label="Градус", command=update_arc)
angle_scale.pack()
angle_scale.set(180)

update_arc()
root.mainloop()
