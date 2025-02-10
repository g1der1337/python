from tkinter import *
n = 0

def on_click():
    global n
    n +=1 
    click_button.config(text=n)
    
window = Tk()
window.geometry("300x300")

click_button = Button(window, text="0", command=on_click)
click_button.pack()

def on_setting(event): 
    if event.keysym == "s":
        global setting_window, btn_width_entry, btn_height_entry, win_width_entry, win_height_entry
        setting_window = Tk()
        setting_window("300x300")
        Label(setting_window, text="Ширина кнопки").pack()
        btn_width_entry = Entry(setting_window)
        btn_width_entry.pack()
 
        Label(setting_window, text="Высота кнопки").pack()
        btn_height_entry = Entry(setting_window)
        btn_height_entry.pack()

        def change_button_size():
            try:
                width = int(btn_width_entry.get())
                height = int(btn_height_entry.get())
                click_button.config(width=width, height=height)
            except ValueError:
                pass

        apply_size_btn = Button(setting_window, text="Применить размер кнопки", command=change_button_size)
        apply_size_btn.pack()
    
        Label(setting_window, text="Ширина окна").pack()
        win_width_entry = Entry(setting_window)
        win_width_entry.pack()

        Label(setting_window, text="Высота окна").pack()
        win_height_entry = Entry(setting_window)
        win_height_entry.pack()

        def change_window_size():
            try:
                width = int(win_width_entry.get())
                height = int(win_height_entry.get())
                window.geometry(f"{width}x{height}")
            except ValueError:
                pass

        apply_window_size_btn = Button(setting_window, text="Применить", command=change_window_size)
        apply_window_size_btn.pack()
        

def of_setting(event):
    if event.keysym == "w":
        setting_window.destroy()

window.bind("<KeyPress>" , on_setting)
window.bind("<KeyRelease>" , of_setting)

window.mainloop()