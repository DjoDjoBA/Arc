import random

class Ball:
    
    def __init__(self, canvas, base, block1, block2, block3, block4, score, color):
        self.canvas = canvas
        self.base = base
        self.block1 = block1
        self.block2 = block2
        self.block3 = block3
        self.block4 = block4
        self.score = score
        self.id = canvas.create_oval(10,10, 35, 35, fill=color)
        start_2 = [40, 60, 90, 120, 150, 180, 200, 240, 260, 290, 320, 350, 380, 400, 440, 460, 490, 520, 550, 580]
        random.shuffle(start_2)
        self.canvas.move(self.id, start_2[0], 300)
        starts = [-2, 2]
        random.shuffle(starts)
        self.x = starts[0]
        self.y = -2
        self.canvas_height = self.canvas.winfo_height()
        self.canvas_width = self.canvas.winfo_width()
        self.hit_bottom = False
   
    def hit_base(self, pos):
        base_pos = self.canvas.coords(self.base.id)
        if pos[2] >= base_pos[0] and pos[0] <= base_pos[2]:
            if pos[3] >= base_pos[1] and pos[3] <= base_pos[3]:
                self.score.hit()
                return True
        return False
    
    def draw(self):
        self.canvas.move(self.id, self.x, self.y)
        pos = self.canvas.coords(self.id)
        
        if pos[1] <= 0:
            self.y = 2
        
        if pos[3] >= self.canvas_height:
            self.hit_bottom = True
            self.canvas.create_text(400, 300, text='Вы проиграли', font=('Courier', 30), fill='red')
        
        if self.hit_base(pos) == True:
            self.y = -2

        if self.hit_block1(pos) == True:
            self.y = 2

        if self.hit_block2(pos) == True:
            self.y = 2
        
        if self.hit_block3(pos) == True:
            self.y = 2
        
        if self.hit_block4(pos) == True:
            self.y = 2

        if pos[0] <= 0:
            self.x = 2
        if pos[2] >= self.canvas_width:
            self.x = -2

    def hit_block1(self, pos):
        block1_pos = self.canvas.coords(self.block1.id)
        if pos[2] >= block1_pos[0] and pos[0] <= block1_pos[2] and self.block1.state == True:
            if pos[3] >= block1_pos[1] and pos[3] <= block1_pos[3] and self.block1.state == True:
                self.score.hit()
                self.block1.state = False
                return True
        return False    

    def hit_block2(self, pos):
        block2_pos = self.canvas.coords(self.block2.id)
        if pos[2] >= block2_pos[0] and pos[0] <= block2_pos[2] and self.block2.state == True:
            if pos[3] >= block2_pos[1] and pos[3] <= block2_pos[3] and self.block2.state == True:
                self.score.hit()
                self.block2.state = False
                return True
        return False   

    def hit_block3(self, pos):
        block3_pos = self.canvas.coords(self.block3.id)
        if pos[2] >= block3_pos[0] and pos[0] <= block3_pos[2] and self.block3.state == True:
            if pos[3] >= block3_pos[1] and pos[3] <= block3_pos[3] and self.block3.state == True:
                self.score.hit()
                self.block3.state = False
                return True
        return False   

    def hit_block4(self, pos):
        block4_pos = self.canvas.coords(self.block4.id)
        if pos[2] >= block4_pos[0] and pos[0] <= block4_pos[2] and self.block4.state == True:
            if pos[3] >= block4_pos[1] and pos[3] <= block4_pos[3] and self.block4.state == True:
                self.score.hit()
                self.block4.state = False
                return True
        return False       