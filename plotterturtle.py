#plotterturtle module by Thomas Rutgers, WDKA Interaction station
import chiplotle, turtle
from random import randint
from datetime import datetime
commands= []
#pixelToMmRatio=7 #for A4
pixelToMmRatio=10 #for A3
OFFLINE = True
def plot():
	plotter = chiplotle.instantiate_plotters()[0]
	plotter.write_file("temp.plt")
def scale(coords):
	xOut = (float(coords[0])*float(pixelToMmRatio))+8080
	yOut = (float(coords[1])*float(pixelToMmRatio))+5520
	return (xOut,yOut)
def turtle_to_plotter():
	cmd(chiplotle.hpgl.PA([scale(turtle.pos())]))
def cmd(c):
	if not OFFLINE: plotter.write(c)
	else: commands.append(c)	
def forward(x):
	turtle.fd(x*5)
	turtle_to_plotter()	
def backward(x):
	turtle.backward(x*5)
	turtle_to_plotter()	
def left(x):
	turtle.left(x)
def right(x):
	turtle.right(x)
def setheading(x):
	turtle.setheading(x)
def goto(x,y):
	turtle.goto(x*5,y*5)
	turtle_to_plotter()
def up():
	turtle.up()
	cmd(chiplotle.hpgl.PU())
def down():
	turtle.down()
	cmd(chiplotle.hpgl.PD())
def save(filename):
	chiplotle.io.save_hpgl(commands, filename)
def mainloop():
	turtle.mainloop()
def speed(s):
	if (s<=0): turtle.tracer(0,0)
	else: turtle.speed(s-1)		
def end():
	turtle.update()
	filename="plots/"+str("%02d" % datetime.now().hour)+str("%02d" % datetime.now().minute)+str("%02d" % datetime.now().second)+".plt"
	save(filename)
	print("Finished! wrote "+filename)
	turtle.exitonclick()
def begin():
	up()
	down()
	
turtle.mode("logo")
turtle.setup( width = 1500, height = 1000, startx = 100, starty = None) 
up()
goto(0,0)
down()
if OFFLINE == False: plotter = chiplotle.instantiate_plotters()[0]
