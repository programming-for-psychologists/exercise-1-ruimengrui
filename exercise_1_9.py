import time
import sys
from psychopy import visual,event,core
 
win = visual.Window([400,400],color="black", units="pix")
square = visual.Rect(win,lineColor="black",fillColor="red",size=[100,100], pos=[0,0])

increment = 6

while True:
	square.ori += increment
	square.draw()
	win.flip()
	if event.getKeys('s'):
		increment = 0
	if event.getKeys('r'):
		increment = 6
	if event.getKeys('q'):
		break

sys.exit()