from __future__ import division
import numpy as np
from texttable import Texttable
import matplotlib.pyplot as plt


def f(t):
    return np.exp(-t) - t


def plot(xu,xr,xl):
    x = np.arange(-3, 5, 0.1)
    plt.plot(x, f(x), color='r')
    plt.axvline(xl, color='g')
    plt.axvline(xr, color='b')
    plt.axvline(xu, color='y')
    plt.axhline(0, linestyle='--', color='k', linewidth=0.1)
    plt.axvline(0, linestyle='--', color='k', linewidth=0.1)
    plt.show()


def draw_table(i, xl, xu, test, ea, es,total):
    t = Texttable()
    t.header(["i", "xl", "xu", "test", "ea", "es"])
    t.add_row([i, xl, xu, test, ea, es])
    t.set_cols_width([7, 7, 7, 7, 7, 7])
    t.set_cols_align(["c", "c", "c", "c", "c", "c"])
    total.header(["i", "xl", "xu", "test", "ea", "es"])
    total.add_row([i, xl, xu, test, ea, es])
    total.set_cols_width([7, 7, 7, 7, 7, 7])
    total.set_cols_align(["c", "c", "c", "c", "c", "c"])
    print(t.draw())


def bisection(xl, xu, es):

    if f(xl)*f(xu) > 0:
        print ("No roots")
        return
    ea = 100
    i=0
    total=Texttable()
    while ea > es:
        i+=1
        xr=(xu+xl)/2
        test= f(xl) * f(xr)
        draw_table(i, xl, xu, test, ea, es,total)
        plot(xu,xr,xl)
        ea = abs((xu-xl)/xl)
        if test < 0:
            xu = xr
        else:
            xl = xr
    print(total.draw())
    return


bisection(-2,4,0.01)