import math
import numpy as np
from scipy import integrate
#define function
f = lambda y,x:x*math.cos(x**2+y)
#compute the integral and error
I = integrate.dblquad(f,0,2,1,4)
print("The result of I = ",I[0])
print("The error = ", I[1])