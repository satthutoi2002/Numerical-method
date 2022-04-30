import numpy as np
from sympy import *
x,y = symbols('x y')
x_l = 0
x_u = 2
y_l = 1
y_u = 4
n_0 = 50
n_1 = 50
h_0=(x_u-x_l)/n_0
m_0=int(n_0/2)
h_1=(y_u-y_l)/n_1
m_1=int(n_1/2)
f = x*cos(x**2 + y)
A = f.subs(x,x_l)+f.subs(x,x_u)+4*f.subs(x,x_l+h_0)
for i in range(1,m_0):
    A+= 2*f.subs(x,x_l+2*i*h_0)+4*f.subs(x,x_l+(2*i+1)*h_0)
G = A*h_0/3
J = G.subs(y,y_l)+G.subs(y,y_u)+4*G.subs(y,y_l+h_1)
for i in range(1,m_1):
    J+= 2*G.subs(y,y_l+2*i*h_1)+4*G.subs(y,y_l+(2*i+1)*h_1)
J = np.double(J)*h_1/3
print("J = ",J)