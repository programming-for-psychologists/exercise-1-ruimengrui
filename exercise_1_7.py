import time
import sys
from psychopy import visual,event,core
 
win = visual.Window([400,400],color="black", units="pix")
square = visual.Rect(win,lineColor="black",fillColor="red",size=[100,100], pos=[0,0])

while True:
	square.ori += 6
	square.draw()
	win.flip()
	if event.getKeys('q'):
		break

sys.exit()