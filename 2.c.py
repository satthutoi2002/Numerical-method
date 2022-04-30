import numpy as np
#define function
def func(x,y):
    f = x*np.cos(x**2+y)
    return f

# Values in x,y to evaluate the integral with 40 and 60 sub-intervals.
x_1 = np.linspace(0, 2, 40)
y_1 = np.linspace(1, 4, 60)
# Values in x,y to evaluate the integral with 80 and 120 sub-intervals.
x_2 = np.linspace(0, 2, 80)
y_2 = np.linspace(1, 4, 120)
# create 2d array 
X_1, Y_1 = np.meshgrid(x_1, y_1)
X_2, Y_2 = np.meshgrid(x_2,y_2)
#create function with 2d variables and compute the integral by using trapezoid method
func1=func(X_1,Y_1)
func2=func(X_2,Y_2)
#evaluate integral with 40 and 60 sub_intervals
J_1 = np.trapz(np.trapz(func1,y_1, axis=0), x_1, axis=0)
J_2 = np.trapz(np.trapz(func2,y_2,axis = 0), x_2,axis = 0)
I = 1/2*(-np.cos(8)+np.cos(4)+np.cos(5)-np.cos(1))
print("J_1 = ",J_1)
print("The error of J_1 is: ",np.abs(J_1-I))
print("J_2 = ",J_2)
print("The error of J_2 is: ",np.abs(J_2-I))

