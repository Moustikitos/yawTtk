# yawTtk
yawTtk is a Python wrapper for Tile. It provides classes which allow the display,
positioning and control of native look 'n feel widgets.

## Why this wrapper ?
* yawTtk works with python 2.5 to python 3.4
* Translation between Tkinter and yawTtk requires no code modification. yawTtk silently
  ignores bad options and tries to configure widgets as old tk widgets.
* yawTtk provides new options : **target**, **utext** and **ulabel** (the bitmap option is no 
  longer available).
  * target is an easier way to link scrollbars with scrolable widgets.
  * utext and ulabel are text and label with underscore character to define the underline
    index within Tkinter.
* yawTtk alows easier way to include images in widgets. You can specify a pathfile, a
  base-64 encoded string, a PIL Image instance or a tuple matching Tile specification
  for a multistate image option.
* Menu creation for Menubutton is easier. A couple of functions are defined to add,
  modify or delete menu item without taking care of `Tkinter.Menu` background.
* yawTtk implements element and layout creation to enhance user interfaces.
