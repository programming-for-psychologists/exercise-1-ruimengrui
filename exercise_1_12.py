import time
import sys
from psychopy import visual,event,core
 
win = visual.Window([400,400],color="black", units="pix")
square_left = visual.Rect(win,lineColor="black",fillColor="red",size=[100,100], pos=[-100,0])
square_right = visual.Rect(win,lineColor="black",fillColor="red",size=[100,100], pos=[100,0])

while True:
	square_left.ori += 1
	square_right.ori -= 1
	square_left.draw()
	square_right.draw()
	win.flip()

	if event.getKeys('q'):
		break

sys.exit()