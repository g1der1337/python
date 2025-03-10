import tkinter as tk


def start_move(event):
    global start_x, start_y
    start_x, start_y = event.x, event.y

def move_window(event):
    global start_x, start_y
    dx = event.x - start_x
    dy = event.y - start_y
    canvas.move(window_id, dx, dy)

root = tk.Tk()
root.title("Кликер")

canvas = tk.Canvas(root, width=300, height=300, bg='#ffffff')
canvas.pack()

clicker_button = tk.Button(root, text="Клик")
window_id = canvas.create_window(150, 150, window=clicker_button)

clicker_button.bind("<ButtonPress-1>", start_move)
clicker_button.bind("<B1-Motion>", move_window)

root.mainloop()
