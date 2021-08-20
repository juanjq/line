import matplotlib.pyplot as plt
import numpy as np
import math
from matplotlib.collections import LineCollection

def line(slope,              #slope by default in degrees
         intercept,          # y intercept of the line
         ax,                 #matplotlib axe where we are plotting
         xdisplacement=0,    # if we want to displace the line in the x coordinate
         mode='degree',      #mode to imput the slope('degree','radian','slope')
         color='darkblue'    #color of the lina
            ):
    
    #getting slope    
    if mode=='degree':
        m=np.tan(slope*np.pi/180)
    elif mode=='radian':
        m=np.tan(slope)
    elif mode=='radian':
        m=slope
    
    #get limits
    sup=ax.get_ylim()[1]
    inf=ax.get_ylim()[0]
    right=ax.get_xlim()[1]
    left=ax.get_xlim()[0]

    #cut points
    limsx,limsy=[],[]

    if m!=0:
        limsy.append(sup)
        limsx.append((sup-intercept)/m+xdisplacement)
        limsy.append(inf)
        limsx.append((inf-intercept)/m+xdisplacement)

    if m!=math.inf or abs(m)>10e7 or m!=-math.inf:
        limsy.append(right*m+intercept)
        limsx.append(right+xdisplacement)
        limsy.append(left*m+intercept)
        limsx.append(left+xdisplacement)
    
    #creating a new colection
    col = LineCollection([np.column_stack((limsx,limsy))], colors=color)
    ax.add_collection(col, autolim=False)