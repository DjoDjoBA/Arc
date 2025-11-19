from tkinter import *

import time
import random 
import threading

from classes.ball import Ball
from classes.base import Base
from classes.score import Score
from classes.block import Block

main = Tk()
main.title("Platform")
main.geometry("800x600")
main.resizable(0, 0)

screen = Canvas(main, width=800, height=600, highlightthickness=0)
screen.pack()
main.update()

score = Score(screen, 'blue')
base = Base(screen, 'white')

block_1 = Block(screen, 'blue', True, 0, 10)
block_2 = Block(screen, 'blue', True, 200, 10)
block_3 = Block(screen, 'blue', True, 400, 10)
block_4 = Block(screen, 'blue', True, 600, 10)

ball = Ball(screen, base, block_1, block_2, block_3, block_4, score, 'red')
        
while not ball.hit_bottom:
    if base.started == True:
        ball.draw()
        base.draw()

    main.update_idletasks()
    main.update()
    time.sleep(0.01)
    
    block_1.status()
    block_2.status()
    block_3.status()
    block_4.status()

time.sleep(3)