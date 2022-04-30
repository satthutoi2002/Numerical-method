import numpy as np
import matplotlib.pyplot as plt
import math
#initial data of x and y
x = np.array([0.2, 0.3, 0.6, 0.9, 1.1, 1.3, 1.4, 1.6])
y = np.array([0.050446, 0.098426, 0.33277, 0.72660, 1.0972, 1.5697, 1.8487, 2.5015])
#construct matrix A
A = np.zeros((len(x),2))
for i in range(2):
    for j in range(len(x)):
        A[j,i] = x[j]**i
#conver y to ln_y
log_y = np.log(y)
#calculate the coefficients of the polynomial
a = np.matmul(np.linalg.inv(np.matmul(np.transpose(A),A)),np.matmul(np.transpose(A),np.transpose(log_y)))
#swap the coefficients to easily determine which is first and which is second
a = np.flipud(a)
#convert from log(b) to b
b = math.e**a[1]
#Construct function
def P(x):
    f = b*math.e**(a[0]*x)
    return f
#calculate the error
error = np.sum((y-P(x))**2)
print("a = ",a[0])
print("b = ",b)
print("The error = ",error)
#plot the polynomial graph and show the different between actual and theory data
plt.scatter(x,y,c = 'r')
plt.plot(x,P(x),c = 'blue')
plt.show()