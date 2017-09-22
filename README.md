# plotterturtle

## Introduction

This is a small python module combining python's Turtle Graphics and the Chiplotle plotter library
It generates a .plt file that can be written to the plotter later.
Or it can drive the plotter right away (see "interactive mode")

The scaling is optimized for HP 7475A plotters in A3 format

Written by Thomas Rutgers for the Willem de Kooning Academy, Rotterdam


## Installation

### Connecting a plotter
Connect the HP7475A plotter with a USB-to-Serial adapter. Install the drivers. Probably [these](http://www.prolific.com.tw/US/ShowProduct.aspx?pcid=41) will work. DIP-Switch settings for the 7475A plotter:
`S2 S1 Y  US A3 B4 B3 B2 B1`
`         x  x  x     x    `
`x  x  x           x     x `
` Par. D MET A4 \.. baud../`

### Installing the chiplotle library
* First install pip. Open a terminal window, and type: `sudo easy_install pip`
* Then install chiplotle. type: `sudo pip install chiplotle`
* Run chiplotle once. type: `chiplotle` and press ENTER two times. It will generate some files in the home-folder. *When using this in a workshop, make sure this is done for the user that is logged in at that moment, else python will give an error
### Write a program
* Open the mydrawing.py example in a text editor, (for instance Sublime text) and run it (in Sublime-Text: command-B)
### Plot it!
* When there are no errors, the console will show a .plt file is being created with the current time as its file name. To plot this file: open a terminal window and run `__chiplotle__` . After the plotter has been found, type for instance `plotter.write_file('140318.plt')` Of course, make sure the directory is correct.

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

To make the plotter execute the commands on the fly, change the `OFFLINE = True` to `False` in the plotterturtle.py file.
