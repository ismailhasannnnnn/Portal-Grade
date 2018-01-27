import tkinter as tk
from tkinter import *

class GUI:

    def __init__(self, master):

        frame = Frame(master)
        frame.pack()

        self.button = Button(frame, text="Quit", fg="red", command=frame.quit)
        self.button.pack(side=LEFT)

        self.say_hi = Button(frame, text="Hi", fg="blue", command=self.say_hi)
        self.say_hi.pack(side=RIGHT)


    def say_hi(self):
        global frame

        self.hiLabel = Label(frame, text="Hey dood")
        self.hiLabel.pack(t)

root = Tk()

gui = GUI(root)

root.mainloop()
root.destroy()
