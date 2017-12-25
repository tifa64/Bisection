#To avoid exception of dividing by zero
from __future__ import division
 # To call any mathematical method such as exponential
import numpy as np
#To help printing the values as table
from texttable import Texttable
#To plot the graph
import matplotlib.pyplot as plt

# For more generic code
def f(t):
    return t**4 - 2*(t**3) - 4*(t**2) + 4

# We plot each line in a different colour to distinguish them
def plot(xu,xr,xl):
    # Setting the range of f(t)
    x = np.arange(-3, 5, 0.1)
    # Plotting f(t)
    plt.plot(x, f(x), color='r')
    # Plotting xl (x lower)
    plt.axvline(xl, color='g')
    # Plotting xr (x middle)
    plt.axvline(xr, color='b')
    # Plotting xu (x upper)
    plt.axvline(xu, color='y')
    # X-axis
    plt.axhline(0, linestyle='--', color='k', linewidth=0.1)
    # Y-axis
    plt.axvline(0, linestyle='--', color='k', linewidth=0.1)
    # Show the plot itself
    plt.show()

# Function to print the variables as a table
def draw_table(i, xl, xu, test, ea, es,total):
    # Helper function
    t = Texttable()
    # Setting the columns' values
    t.header(["i", "xl", "xu", "test", "ea", "es"])
    # Adding them to the row
    t.add_row([i, xl, xu, test, ea, es])
    # Setting the table's width dimentions
    t.set_cols_width([7, 7, 7, 7, 7, 7])
    # For justification
    t.set_cols_align(["c", "c", "c", "c", "c", "c"])
    total.header(["i", "xl", "xu", "test", "ea", "es"])
    total.add_row([i, xl, xu, test, ea, es])
    total.set_cols_width([7, 7, 7, 7, 7, 7])
    total.set_cols_align(["c", "c", "c", "c", "c", "c"])
    print(t.draw())


def bisection(xl, xu, es):
    # Either f(a) < 0 and f(b) > 0 or f(a) > 0 and f(b) < 0
    if f(xl)*f(xu) > 0:
        print ("No roots")
        return
    # Setting it to very high values so that we can decrease it to minimum
    ea = 100
    # Iterator
    i=0
    # To withhold the table
    total=Texttable()
    # Loop to get the roots
    while ea > es:
        # Increment the iterator
        i+=1
        # Get middle point
        xr=(xu+xl)/2
        # To see if it achieves the condition
        test= f(xl) * f(xr)
        # Draw table with each iteration
        draw_table(i, xl, xu, test, ea, es,total)
        # Plot graph with each iteration
        plot(xu,xr,xl)
        # Get absolute error
        ea = abs((xu-xl)/xl)
        # To see where do we move and set our new range
        if test < 0:
            # Left
            xu = xr
        else:
            # Right
            xl = xr
    # Draw the table
    print(total.draw())
    return


bisection(-2,1,0.001)