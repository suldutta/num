import numpy as np
x=np.linspace(-2,2,100)
def f(x):
    return (10-x*x)
a=-2

b=2

y1=f(a)

y2=f(b)

h=(b-a)/100.0

s1=((y1+y2)/2.0)*h

s2=0

for i in range(100):
    s2=s2+f(a+i*h)

s=s1+s2*h

s

