import time
import sys
from psychopy import visual,event,core
 
win = visual.Window([400,400],color="black", units="pix")
square = visual.Rect(win,lineColor="black",fillColor="blue",size=[100,100], pos=[0,0])

while not event.getKeys('q'):
	if event.getKeys('left'):
		square.size += (10, 0) 
	if event.getKeys('right'):
		square.size -= (10, 0)

	square.draw()
	win.flip() 

sys.exit()
