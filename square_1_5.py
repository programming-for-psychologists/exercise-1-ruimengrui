import time
import sys
from psychopy import visual,event,core
 
win = visual.Window([400,400],color="black", units="pix")
square_red = visual.Rect(win,lineColor="black",fillColor="red",size=[100,100], pos=[0,0])
square_blue = visual.Rect(win,lineColor="black",fillColor="blue",size=[100,100], pos=[0,0])

for i in range(1,4):
	square_blue.draw() 
	win.flip() 
	core.wait(1.0) #pause for 1000 ms
	win.flip() # blank screen
	core.wait(0.5) #pause for 500 ms 

	square_red.draw() 
	win.flip() # red screen
	core.wait(1.0) #pause for 1000 ms
 	win.flip() # blank screen
	core.wait(0.5) #pause for 500 ms 

sys.exit()