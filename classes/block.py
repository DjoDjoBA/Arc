import random
import time
import threading 
from tkinter import ttk

class Block:
    def __init__(self, canvas, color, state, base_x, base_y):
        self.canvas = canvas
        self.id = canvas.create_rectangle(10, 10, 180, 50, fill=color)
        self.x = base_x
        self.y = base_y
        self.canvas.move(self.id, base_x, base_y)
        self.state = True
        
    def draw(self):
        pos = self.canvas.coords(self.id)
        self.x
        self.y         

    def status(self):
        if self.state == False:
            self.x = 1000
            self.y = 700 
            self.canvas.move(self.id, self.x, self.y)