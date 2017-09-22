# plotterturtle

## Introduction

This is a small python module combining python's Turtle Graphics and the Chiplotle plotter library
It generates a .plt file that can be written to the plotter later.
Or it can drive the plotter right away (see "interactive mode")
Written by Thomas Rutgers for the WDKA Interaction Station
The scale is optimized for HP 7475A plotters in A3 format


## Installation

### Installing the chiplotle library
* First install pip. Open a terminal window, and type: **sudo easy_install pip**
* Then install chiplotle. type: **sudo pip install chiplotle**
* Run chiplotle once. type: **chiplotle** and press ENTER two times. It will generate some files in the homefoler. When using this in a workshop, make sure this is done for the user that is logged in at that moment, else python will give an error
* Open the mydrawing.py example in a text editor, (for instance Sublime text) and run it (in Sublime-Text: command-B)
* When there are no errors, the console will show a .plt file is being created with the current time as its file name. To plot this file: open a terminal window and run __chiplotle__ . After the plotter has been found, type for instance **plotter.write_file('140318.plt')** Of course, make sure the directory is correct.

## Supported commands
* begin()
* end()
* forward(x)
* backward(x)
* left(x)
* right(x)
* setheading(x)
* goto(x,y)
* speed(x)
* up()
* down()
* randint(x,y)

## Interactive mode

To make the plotter execute the commands on the fly, change the OFFLINE = True to False in the plotterturtle.py file.
