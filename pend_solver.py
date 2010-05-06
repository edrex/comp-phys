#!/usr/bin/python

from pylab import *
from numpy import *

"""
"""

def euler_cromer(x, v, accel, dt, t_f, t=0):
    while t < t_f:
        yield t, x, v
        t = t + dt
        v = v + accel(x, v, t) * dt
        x = x + v * dt
        
def rk4(x, v, accel, dt, t_f, t=0):
    while t < t_f:
        yield t, x, v
        t  = t + dt
        x1 = v * dt
        v1 = accel(x,      v,      t)      * dt
        x2 = (v + v1/2) * dt
        v2 = accel(x+x1/2, v+v1/2, t+dt/2) * dt
        x3 = (v + v2/2) * dt
        v3 = accel(x+x2/2, v+v2/2, t+dt/2) * dt
        x4 = (v+v3) * dt
        v4 = accel(x+x3,   v+v3,   t+dt/2) * dt
        v  = v + (v1 + 2*v2 + 2*v3 + v4)/6
        x  = x + (x1 + 2*x2 + 2*x3 + x4)/6

def solve(x_0, v_0, accel, dt, t_f, t_0=0, algorithm=euler_cromer):
    # convert the solution generator into a list of data points
    data = list(algorithm(x_0, v_0, accel, dt, t_f)) 
    # this turns a list of triples into three separate lists
    T,X,V = zip(*data)
    return T,X,V
    
def plot_it(T,X,V):
    close()
    ion()
    grid(True)
    hold(True)

    subplot(221)
    plot(T,X,'c-')
    title('x vs time  ')

    subplot(222)
    plot(X,V,'b-')
    title('v vs x')

systems = {
    'simple_pend': lambda x, v, t: -x,
    'real_pend': lambda x, v, t: -sin(x),
    'strange_osc': lambda x, v, t: -x**9,
    'damped': lambda x, v, t: -sin(x)-v/q,
    'damped_driven': lambda x, v, t: -sin(x)-v/q + g*cos(w*t),
}

algorithms = {
    'rk4': rk4,
    'euler_cromer': euler_cromer,
}

#####################    
## Start example code
#####################

alg = 'rk4'
sys = 'simple_pend'
vars = {
    'g': 9.8,
    'q': 1,
    'w': 2*pi,
    'x0': 1,
    'v0': 0,
    'dt': 0.01,
    'tf': 10,
}    

#T,X,V=solve(x_0=1, v_0=0, accel=systems['real pendulum'], dt=0.01, t_f=10, solver=rk4) 
#plot_it(T,X,V)
if __name__ == '__main__':
        DO SOMETHING
