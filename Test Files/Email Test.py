import tkinter
import re

window = tkinter.Tk()
window.title("Widgets Example")
lbl = tkinter.Label(window, text="Email")
ent = tkinter.Entry(window)
email = ent

def callback():
    print(ent.get())

btn = tkinter.Button(window, text="Verify", command=callback())

lbl.pack()
ent.pack()
btn.pack()


window.mainloop()

