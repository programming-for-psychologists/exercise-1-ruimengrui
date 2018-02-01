import time
import sys
from psychopy import visual,event,core
 
win = visual.Window([400,400],color="black", units="pix")
square_red = visual.Rect(win,lineColor="black",fillColor="red",size=[100,100], pos=[0,0])
square_blue = visual.Rect(win,lineColor="black",fillColor="blue",size=[100,100], pos=[0,0])

square_red.draw() # draw in back or buffer
win.flip() 
core.wait(1.0) #pause for 1000 ms 

square_blue.draw() 
win.flip() # make it visible
core.wait(1.0) #pause for 1000 ms

sys.exit()