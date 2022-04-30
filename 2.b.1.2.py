import numpy as np
from scipy import integrate
#define function
def func1(x,y):
    f = x*np.cos(x**2+y)
    return f
#Define the number of sub-intervals 
n_0 = 50
n_1 = 50
# Values in x,y to evaluate the integral.
x = np.linspace(0, 2, n_0)
y = np.linspace(1, 4, n_1)
# create 2d array 
X, Y = np.meshgrid(x, y)
#create function with 2d variables and compute the integral by using trapezoid method
func=func1(X, Y)
J = integrate.simpson(integrate.simpson(func,x),y)
print("J =",J)