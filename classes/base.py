import random

class Base:
    def __init__(self, canvas, color):
        self.canvas = canvas
        self.id = canvas.create_rectangle(0, 0, 150, 20, fill=color)
        start_1 = [40, 60, 90, 120, 150, 180, 200, 240, 260, 290, 320, 350, 380, 400, 440, 460, 490, 520, 550, 580]
        random.shuffle(start_1)      
        self.starting_point_x = start_1[0]
        self.canvas.move(self.id, self.starting_point_x, 500)
        self.x = 0
        self.canvas_width = self.canvas.winfo_width()
        self.canvas.bind_all('<KeyPress-Right>', self.turn_right)
        self.canvas.bind_all('<KeyPress-Left>', self.turn_left)
        self.started = False
        self.canvas.bind_all('<KeyPress-Return>', self.start_game)
    
    def turn_right(self, event):
        self.x = 5
    
    def turn_left(self, event):
        self.x = -5
    
    def start_game(self, event):
        self.started = True
    
    def draw(self):
        self.canvas.move(self.id, self.x, 0)
        pos = self.canvas.coords(self.id)
        if pos[0] <= 0:
            self.x = 0
        elif pos[2] >= self.canvas_width:
            self.x = 0