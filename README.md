# line
A simple python module to print a stright line, in the way that it does the matplotlib functions `plt.axhline` or `plt.axvline`, but for any line with different slopes or y intercepts.

Until now there is only a function  `line()` where we have different inputs:

* **`slope=`** (needed) The slope of the line. By default in *degrees* but it culd be im

* **`intercept=`** (needed) The y intercept value of the line.

* **`ax=`** (needed) The ax object of matplotlib where we are plotting the line i.e. `fig, ax = plt.subplots()`

* **`xdisplacement`** If we want to displace the line in the x axe

* **`mode`** Mode of slope input. By default is `'degree'`, could be changed by `'radian'` or `'slope'`

* **`color`** The color of the line
