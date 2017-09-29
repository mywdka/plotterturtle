# plotterturtle

## Introduction

This is a small python module linking python's Turtle Graphics to the Chiplotle plotter library

## How-to

### Connecting a plotter
*The plotters i use are HP 7475A plotters. Another plotter will probably work too, although you may have to change the scaling.*

Connect the plotter with a USB-to-Serial adapter. Install the drivers. For the ones we have at the WDKA, [this driver](http://www.prolific.com.tw/US/ShowProduct.aspx?pcid=41) will work. If you need a converter cable, check the [included jpeg](https://github.com/mywdka/plotterturtle/blob/master/hp7475a%20cable.jpg).
So the setup is likethis:

`[plotter]-[converter cable]-[usb to serial cable]-[computer]`

The little DIP-switches next to the connector are set like this:

`S2 S1 Y US A3 B4 B3 B2 B1`

`vv vv v ^^ ^^ ^^ vv ^^ vv`

### Installing the chiplotle library
* First install pip. Open a terminal window, and type: `sudo easy_install pip`
* Then install chiplotle. type: `sudo pip install chiplotle`
* Run chiplotle once. type: `chiplotle` and press ENTER two times. It will generate some files in the home-folder. *When using this in a workshop, make sure this is done for the user that is logged in at that moment, else python will give an error.*
### Write a program
* Download this repository, open the mydrawing.py example in a text editor, (for instance Sublime text), run it (in Sublime-Text: command-B), extend it.
### Plot it!
* When there are no errors, the console will show a .plt file is being created in the *plots/* folder, with the current time as its file name. To plot this file: open a terminal window and run `chiplotle` . After the plotter has been found, type for instance `plotter.write_file('140318.plt')` Of course, make sure the directory is correct.

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

---

Written by Thomas Rutgers for the Willem de Kooning Academy, Rotterdam
Compatible with the laser-cut physical [turtleblocks](http://www.github.com/mywdka/turtleblocks/) for teaching programming
