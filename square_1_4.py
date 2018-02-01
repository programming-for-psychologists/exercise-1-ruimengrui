import time
import sys
from psychopy import visual,event,core
 
win = visual.Window([400,400],color="black", units="pix")
square_red = visual.Rect(win,lineColor="black",fillColor="red",size=[100,100], pos=[0,0])

square_red.draw() # draw in back or buffer
win.flip() 
core.wait(1.5) #pause for 1500 ms 

win.flip() # make it visible
core.wait(1.0) #pause for 500 ms 

for i in range(1,4):
	square_red.draw() # draw in back or buffer
	win.flip() 
	core.wait(0.03) #pause for 30 ms 
	win.flip() 
	core.wait(0.5)

sys.exit()