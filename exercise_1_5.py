import time
import sys
from psychopy import visual,event,core
 
win = visual.Window([400,400],color="black", units="pix")
square = visual.Rect(win,lineColor="black",size=[100,100], pos=[0,0])

for i in ['blue','red']*3:
	square.setFillColor(i)
	square.draw() 
	win.flip() 
	core.wait(1.0) 
	win.flip() 
	core.wait(0.5)

sys.exit()