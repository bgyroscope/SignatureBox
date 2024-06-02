#!/usr/bin/python
"""GUI class that controls main feature of the applet"""
import time
import tkinter as tk
import numpy as np
from signaturebox.logic.recorder import MouseRecorder
from matplotlib.figure import Figure 
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg,  
NavigationToolbar2Tk) 

SIGNBOX_WIDTH = 80
SIGNBOX_HEIGH = 10

class SignBox:
    """signagure box object"""
    def __init__(self):
        # storing certain values
        self.pts = None

        # for rendering the gui
        self.root = tk.Tk()
        # pack the label and box in the tkinter app
        lab_header = tk.Label(self.root, text="Signature Box")
        lab_instr = tk.Label(self.root, text="Click and drag in white area to produce signature.")
        lab_box = tk.Label(self.root, background='white', width=SIGNBOX_WIDTH, height=SIGNBOX_HEIGH)

        button_quit = tk.Button(self.root, text="Quit", command=lambda: self.root.quit()  )
        button_clear = tk.Button(self.root, text="Clear", command=self.clear)
        button_rec = tk.Button(self.root, text="Record", command=self.record)

        button_quit.pack(side='bottom')
        button_clear.pack(side='bottom')
        button_rec.pack(side='bottom')
        lab_box.pack(side='bottom')
        lab_instr.pack(side='bottom')
        lab_header.pack(side='bottom')

    def activate(self):
        self.root.mainloop()

    def record(self):
        m = MouseRecorder()
        m.record()
        self.update_pts(m.pts)
        self.render()
 
    def render(self):
        print( f"{len(self.pts)} pts in self.pts")

    def clear(self):
        self.pts = None

    def update_pts(self, pts: np.ndarray):
        if self.pts is None:
            self.pts = pts
        else:
            self.pts = np.append(self.pts, pts, axis=0)