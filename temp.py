from __future__ import division
import numpy as np
def bisection(xl, xu, es):
   if  (((np.exp(-xl) - xl)*(np.exp(-xu) - xu)) > 0) :
       print ("No roots")
       return
   ea = 100;
   while(ea > es) :
       xr=(xu+xl)/2;
       test= (np.exp(-xl) - xl) * (np.exp(-xr) - xr);
       print "xl: %d  xu: %d test: %f   ea: %f  es: %f"%(xl, xu, test, ea, es)
       ea = abs((xu-xl)/xl);
       if (test < 0):
           xu=xr;
       else:
           xl=xr;
   return