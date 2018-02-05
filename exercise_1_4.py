import time
import sys
from psychopy import visual,event,core
 
win = visual.Window([400,400],color="black", units="pix")
square = visual.Rect(win,lineColor="black",fillColor="blue",size=[100,100], pos=[0,0])

square.draw()
win.flip() 
core.wait(1.5) 

win.flip() 
core.wait(1.0) 

for i in range(1,4):
	square.draw() 
	win.flip() 
	core.wait(0.03) 
	win.flip() 
	core.wait(0.5)

sys.exit()