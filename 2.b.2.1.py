import numpy as np
from sympy import *
x,y = symbols('x y')
x_l= 0
x_u= 2
y_l=1
y_u=4
n_0 =50
n_1 = 50
h_0=(x_u-x_l)/n_0
h_1=(y_u-y_l)/n_1
f = x*cos(x**2 + y)
A = f.subs(x,x_l)/2+f.subs(x,x_u)/2
for i in range(1,n_0):
    A+= f.subs(x,x_l+h_0*i)
G = A*h_0
J = G.subs(y,y_l)/2+G.subs(y,y_u)/2
for i in range(1,n_1):
    J+= G.subs(y,y_l+h_1*i)
J = np.double(J)*h_1
print("J =",J)