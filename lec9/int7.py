import numpy as np
a=-1
b=3
n=4.0
h=(b-a)/(n-1)
x=np.linspace(a,b,n)
def func(x):
    return 10-3*x*x

s=0.0
x=a+h
for i in range(1,n/2+1):
    s+=4*func(x)
    x=x+2*h
x=a+2*h
for j in range(1,n/2):
    s=s+2*func(x)
    x=x+2*h

integration=(h/3)*(func(a)+func(b)+s)
print(integration)

