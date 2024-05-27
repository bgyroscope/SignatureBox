#!/usr/bin/python
"""GUI class that controls main feature of the applet"""
import time
import tkinter as tk

SIGNBOX_WIDTH = 40
SIGNBOX_HEIGH = 20

class SignBox:
    """signagure box object"""
    def __init__(self):
        self.root = tk.Tk() 
        # pack the label and box in the tkinter app
        lab_header = tk.Label(self.root, text="Signature Box")
        lab_instr = tk.Label(self.root, text="Click and drag in white area to produce signature.")
        lab_box = tk.Label(self.root, background='white', width=SIGNBOX_WIDTH, height=SIGNBOX_HEIGH)

        button_quit = tk.Button(self.root, text="Quit", command=lambda: self.root.quit()  )

        button_quit.pack(side='bottom')
        lab_box.pack(side='bottom')
        lab_instr.pack(side='bottom')
        lab_header.pack(side='bottom')

    def activate(self):
        self.root.mainloop()

    def record(self):
        pass   

