from tkinter import *

root = Tk()

root.geometry("840x680")

onPic = PhotoImage(file="on.png")
offPic = PhotoImage(file="off.png")

def func():
    def fun():
        
        but.config(image=onPic, command=func)

    but.config(image=offPic, command=fun)

but = Button(image=onPic, bd=0, relief="flat", command=func)

but.pack(pady=30)

mainloop()
