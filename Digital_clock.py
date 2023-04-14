from tkinter import *
import time

app_window=Tk()
app_window.title("Clock")
app_window.geometry("590x150")
app_window.resizable(0,0)


text_font = ("Boulder",68,"bold")
background="#E5B8F4"
foreground="#810CA8"
border_width=25

label = Label(app_window,font=text_font,bg=background,fg=foreground,bd=border_width)

label.grid(row=0,column=1)

def digital_clock():
    time_live = time.strftime("%H:%M:%S:%p")
    label.config(text=time_live)
    label.after(200,digital_clock)
digital_clock()
app_window.mainloop()