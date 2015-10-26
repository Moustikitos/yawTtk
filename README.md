# `yawTtk`
`yawTtk` is a Python wrapper for Tile. It provides classes which allow the display,
positioning and control of native look 'n feel widgets.

## Why this wrapper ?
* `yawTtk` works with python 2.5 to python 3.4
* Translation between `Tkinter` and `yawTtk` requires no code modification. `yawTtk` silently ignores bad options and tries to configure widgets as `Tkinter` widgets.
* `yawTtk` provides new options : **target**, **utext** and **ulabel** (the bitmap option is no longer available).
  * target is an easier way to link scrollbars with scrolable widgets.
  * utext and ulabel are text and label with underscore character to define the underline index within `Tkinter`.
* `yawTtk` alows easier way to include images in widgets. You can specify a pathfile, a base-64 encoded string, a PIL Image instance or a tuple matching Tile specification for a multistate image option.
* Menu creation for Menubutton is easier. A couple of functions are defined to add, modify or delete menu item without taking care of `Tkinter.Menu` background.
* `yawTtk` implements element and layout creation to enhance user interfaces.

## Simple way to configure widgets 
In Tile, widget options and style are separated. `yawTtk` merges them to simplify and match as possible `Tkinter` way of coding. Remember that it is only available if extend option is True. configure funcion is called by `__init__` and `__setattr__` class method so there are 3 different ways to configure widgets.

```python
# configure widget with __init__ function
button = Button(
  style = "custom.Toolbutton",
  anchor = "center",
  font = ("Tahoma", "8", "bold"),
)
# or with __setattr__ function
button["foreground"] = "steelblue3"
button["background"] = "lightgreen"
# or even with configure function
button.configure(
  command = exit,
  text = "Toolbutton",
  padding = (5, 1, 5, 1)
)
# pack and see...
button.pack(fill="x", padx=5, pady=5)
```
<img src="http://bruno.thoorens.free.fr/yawttk/wiki/images/steelblue_button.png" />
