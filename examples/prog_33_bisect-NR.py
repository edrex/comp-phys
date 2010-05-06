"""  week 3 -  
bisection and Newton-Raphson,  finding roots"""
from pylab import *
from numpy import *

def Fun(x):
    return 3.*x**3-2.*x**2+5.*x-1.#cos(x)-x#(x**8.)/40320.-(x**6)/720.+(x**4)/24.-(x**2)/2.-x+1.#3.*x**3-2.*x**2+5.*x-1.
def DFun(z):
    return 6.*z**2-4.*z+5.#-sin(x)-1.#8./40320*x**7-6*x**5/720.+4*x**3/24-x-1.#6.*z**2-4.*z+5.   #sure, this one is easy!

t=zeros((101))
y=zeros((101))
xbot=-1.
xtop=1.
#
#tol=0.00000001  #Rel. tolerance-->[1E-10]
#
print "function = 3x^3 - 2x^2 +5x -1"
tol=float(raw_input("enter tolerance for Bisection (<0.000001)"))
for i in range(101):
    x=xbot+(xtop-xbot)*i/100.
    t[i]=x
    y[i]=Fun(x)
ion()
hold(True)
grid(True)
plot(t,y,'r-')
print
print "Bisection"
print "iteration", "\t","zero","\t","\t","tolerance test"
bot=Fun(xbot)
top=Fun(xtop)
tol_tst=1.
i=0
while tol_tst>tol:
   i=i+1
   z=(xtop+xbot)/2
   tol_tst=xtop-xbot
   test=Fun(z)
   if (test*bot<0): 
      xtop=z
      top=test
   else:
      xbot=z
      bot=test
   print '%3d \t %10.9e \t %7.4e' % (i,z,tol_tst)
#%3d \t %10.9e \t %7.4e means print the following numbers as: 3 digits, exponential notation, ditto
   if z<>0.: 
      tol_tst=tol_tst/z  #notice relative tolerance... why?

#Newton-Raphson
print
print "Newton-Raphson"
print "iteration", "\t","x","\t"*2,"func(x)","\t"*2,"deriv func(x)"
#
x=1.
i=0
tol_tst=1.
while tol_tst>tol and i<30:
   i=i+1
   test=x-Fun(x)/DFun(x)
   if x<>0.:
      tol_tst=abs((x-test)/x)
   print '%3d \t %10.9e \t %10.9e \t %10.9e'% (i,x,Fun(x),DFun(x))
   x=test
