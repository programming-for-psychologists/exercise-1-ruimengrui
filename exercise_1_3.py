import time
import sys
from psychopy import visual,event,core
 
win = visual.Window([400,400],color="black", units="pix")
square = visual.Rect(win,lineColor="black",size=[100,100], pos=[0,0])

square.setFillColor('red')
square.draw() 
win.flip() 
core.wait(1.0) 
win.flip()

square.setFillColor('blue')
square.draw() 
win.flip() 
core.wait(1.0) 

sys.exit()