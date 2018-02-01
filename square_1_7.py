import time
import sys
from psychopy import visual,event,core
 
win = visual.Window([400,400],color="black", units="pix")
square = visual.Rect(win,lineColor="black",fillColor="red",size=[100,100], pos=[0,0])

while not event.getKeys('q'):
	square.setOri(6, '+')
	square.draw()
	win.flip() # take 60ms

sys.exit()