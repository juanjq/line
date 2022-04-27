# line_plot
A simple python module to print a stright line, in the way that it does the matplotlib functions `plt.axhline` or `plt.axvline`, but for any line with different slopes or y intercepts.

Until now there is only a function  `line()` where we have different inputs:

* **`slope=`** (needed) The slope of the line. By default in *degrees* but it culd be im

* **`intercept=`** (needed) The y intercept value of the line.

* **`ax=`** (needed) The ax object of matplotlib where we are plotting the line i.e. `fig, ax = plt.subplots()`

* **`xdisplacement`** If we want to displace the line in the x axe

* **`mode`** Mode of slope input. By default is `'degree'`, could be changed by `'radian'` or `'slope'`

* **`color`** The color of the line


For installing it you can do:

```
import httpimport
with httpimport.remote_repo(['line_plot'], 'https://raw.githubusercontent.com/juanjq/line_plot/main'):
     import line_plot as line
```

An example of use,

```
fig, ax = plt.subplots()

#other random plot
x1 = np.linspace(-1,1,100)
ax.plot(x1, np.sin(x1))

#plot the line
line.line(20,0.5,ax,xdisplacement=-0.6,color='darkblue',linestyle='--')

plt.show() 
```

![alt text](https://github.com/juanjq/line_plot/blob/main/data/line.png?raw=true)
