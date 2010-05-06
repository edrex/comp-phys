# example of HW problem 3.12 provided by Brett Buchea
# MODIFY
from pylab import *
from numpy import *
from scipy import *


#### Checks if t=2*pi*n/omega ####
def timeCheck1(t,sensitivity):
    maxN=int(omega*t/(2*pi)+1)
    minN=maxN-1
    
    for i in range(minN,maxN):
        temp=2*pi*i/omega
        if round(t,sensitivity)==round(temp,sensitivity):
            return True

    return False


#### Checks if t=2*pi*n/omega+pi/4 ####
def timeCheck2(t,sensitivity):
    maxN=int(omega*(t-pi/4)/(2*pi)+1)
    minN=maxN-1
    
    for i in range(minN,maxN):
        temp=2*pi*i/omega+pi/4
        if round(t,sensitivity)==round(temp,sensitivity):
            return True

    return False


#### Plots Theta with Respect to Omega + Poincare Section (Meat of the Program)####

def f1(thetaIni,wIni):
    #Sets initial values of variables
    theta=[float(thetaIni)]
    w=[float(wIni)]
    thetaGraph1=[0.0]
    wGraph1=[0.0]
    thetaGraph2=[0.0]
    wGraph2=[0.0]
    thetaGraph3=[0.0]
    wGraph3=[0.0]

    #Solves for values for each time step
    for i in range(0,int(maxT/delT)):

        temp=w[i]-(g/l)*sin(theta[i])*delT-q*w[i]*delT+Fd*sin(omega*i*delT)*delT

        w.append(temp)
        temp=theta[i]+w[i+1]*delT

        #Checks if theta is outside range -pi<theta<pi
        if temp>3.14:
            temp=temp-2*3.14
        
        elif abs(temp)>3.14:
            temp=temp+2*3.14

        # Poincare for t=t=2*pi*n/omega
        if timeCheck1(delT*i,1)==True:
            thetaGraph1.append(temp)
            wGraph1.append(w[i])

        # Poincare for t=t=2*pi*n/omega + pi/4
        if timeCheck2(delT*i,1)==True:
            thetaGraph2.append(temp)
            wGraph2.append(w[i])

        # Poincare for Fd=Fd*sin(theta)
        if round(sin(omega*i*delT),3)==1:
            thetaGraph3.append(temp)
            wGraph3.append(w[i])

        theta.append(temp)
        
    thetaGraph1.remove(0.0)
    wGraph1.remove(0.0)
    thetaGraph2.remove(0.0)
    wGraph2.remove(0.0)
    thetaGraph3.remove(0.0)
    wGraph3.remove(0.0)
    
    return [thetaGraph1,wGraph1,thetaGraph2,wGraph2,thetaGraph3,wGraph3,theta,w]



### Sets Variables ####
Fd=float(raw_input('What is your driving force? (1.2 Recomended):'))
maxT=1000
g=9.81
l=9.8
delT=0.04
q=0.5
omega=0.66

print '\nDriving Force is',Fd,'.\n'
print 'Max Time is',maxT,'. Length of pendulum arm is',l,'. Time step is',delT,'. Coefficient of friction is',q,'. Omega is',omega,'.'

ion()

values=f1(0.2,0)    #Collect Values for Graphs

# Theta vs. Omega Graph
subplot(221)
plt.xlabel('Theta (radians)')
plt.ylabel('omega (rad/s)')
plt.title('Same as Figure 3.8 In Book')
plot(values[6],values[7],'b-')

# Poincare t=2*pi*n/omega
subplot(222)
plt.xlabel('Theta (radians)')
plt.ylabel('omega (rad/s)')
plt.title('Same as Figure 3.9 In Book')
plot(values[0],values[1],'bo')

# Poincare for t=2*pi*n/omega + pi/4
subplot(223)
plt.xlabel('Theta (radians)')
plt.ylabel('omega (rad/s)')
plt.title('Poincare where t=2*pi*n/omega+pi/4 ')
plot(values[2],values[3],'ro')

# Poincare for Fd=Fd*sin(theta)
subplot(224)
plt.xlabel('Theta (radians)')
plt.ylabel('omega (rad/s)')
plt.title('Poincare where Fd=Fd*sin(theta)')
plot(values[4],values[5],'go')

raw_input('Press Enter to Quit Program')

exit()

