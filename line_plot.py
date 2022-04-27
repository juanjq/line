from   matplotlib.collections import LineCollection
import matplotlib.pyplot      as plt
import numpy                  as np
import math

def line(slope,              #slope by default in degrees
         intercept,          #y intercept of the line
         ax,                 #matplotlib axe where we are plotting
         xdisplacement=0,    #if we want to displace the line in the x coordinate
         mode='degree',      #mode to imput the slope('degree','radian','slope')
         color='darkblue',   #color of the line
         linestyle='-'):
    
    #getting slope    
    if mode   == 'degree':
        m = np.tan(slope*np.pi/180)

    elif mode == 'radian':
        m = np.tan(slope)

    elif mode == 'slope':
        m = slope
    
    #get limits
    sup   = ax.get_ylim()[1]       #superior limit
    inf   = ax.get_ylim()[0]       #inferior limit
    right = ax.get_xlim()[1]       #right limit
    left  = ax.get_xlim()[0]       #left limit

    #cut points
    limsx, limsy = [], []

    if m != 0:
        limsy.append(sup)
        limsx.append((sup-intercept)/m+xdisplacement)
        limsy.append(inf)
        limsx.append((inf-intercept)/m+xdisplacement)

    #we also check if the slope is ~ infinite, so we have a vertical line
    if m != math.inf or abs(m) > 10e7 or m != -math.inf:
        limsy.append(right*m + intercept)
        limsx.append(right   + xdisplacement)
        limsy.append(left*m + intercept)
        limsx.append(left   + xdisplacement)
    
    #creating a new colection
    col = LineCollection([np.column_stack((limsx[:2],limsy[:2]))], colors = color,linestyle = linestyle,antialiased = True)
    ax.add_collection(col, autolim = False)

