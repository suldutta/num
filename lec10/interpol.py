#Lagrange interpolation
import numpy as np
n=3 #no. of datapoints
x=np.array([0,1,2])
y=np.array([1,2,4])

x0=1.5
y0=0

#implementing interpolation
for i in range(n):
    s=1
    for j in range(n):
        if i!=j:
            
           s=s*((x0-x[j])/(x[i]-x[j]))
    y0=y0+s*y[i]

print('Interpolated value is ',y0)
def f(x):
    return 2**x
ya=f(x0)
print('Value of y from original function is ',ya)
