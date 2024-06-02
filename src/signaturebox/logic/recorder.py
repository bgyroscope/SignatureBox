#!/usr/bin python 
"""recorder records location of the mouse as the user drags it."""
import time 
from pynput import mouse

MAX_POINTS = 10000

class MouseRecorder:
    """record movement of the mouse"""

    def on_click(self,x,y,button,pressed):

        if pressed:
            # print( "Clicked!")
            self.recording = True

        if not pressed:
            self.running = False
            return False

    def mark(self,x,y):
        if self.counter < len(self.pts):
            self.pts[self.counter] = (x,y)
            self.counter += 1 

    def on_move(self,x,y):
        if self.recording:
            # print(f'Pointer moved to {(x,y)}' )
            self.mark(x,y)

    def __init__(self):
        self.recorder = mouse.Listener(
            on_move=self.on_move,
            on_click=self.on_click
        ) 
        self.running = False
        self.recording = False

        self.counter = 0 
        self.pts = [(0,0) for i in range(MAX_POINTS)]

    def trim_pts(self):
        self.pts = self.pts[:self.counter]

    def record(self):
        self.running = True
        self.recorder.start() 
        while self.running:
            time.sleep(0.1)

        self.trim_pts()