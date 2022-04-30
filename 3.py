import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
def solve(L,dx,T0,Tinf,h,TL):
    n =int(L/dx -1)
    A = np.zeros((n,n))
    for i in range(0,n):
        for j in range(0,n):
            if i == j:
                A[i,j] = (-2-dx**2*h)
            elif j == i-1:
                A[i,j] = 1
            elif j == i+1:
                A[i,j] = 1
            else:
                A[i,j] = 0
    b = -h*dx**2*Tinf*np.ones((n,1))
    b[0] = b[0] - T0
    b[-1] = b[-1] - TL
    T = np.matmul(np.linalg.inv(A),b)
    return T,L
L = float(input("Input value of  L = "))
dx = float(input("Input value of  dx = "))
Tinf = float(input("Input value of  Tinf = "))
T0 = float(input("Input value of  T0 = "))
h = float(input("Input value of  h = "))
TL = float(input("Input value of  TL = "))
n =int(L/dx -1)
T,distance = solve(L,dx,T0,Tinf,h,TL)
print("T = ",T)
print("L = ",distance)
x = np.linspace(0+dx,L-dx,n)
x = np.append(x,L)
x = np.insert(x,0,0)
T =np.append(T,TL)
T = np.insert(T,0,T0)
sns.lineplot(x = x,y = T)
plt.xlabel('x(m)')
plt.ylabel('T(K)')
plt.title('Plot of the result between x and T')
plt.show()
