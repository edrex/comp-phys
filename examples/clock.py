# EB  ... testing some more: all pretty random!

#3 ways to import the correct function: here clock()
from time import * # Or: from time import clock  (since only clock is needed)
# or import time  but then you have use: time.clock() to get the time

from  numpy  import *   # numerical array package
from  math   import *   # most functions are standard in Python, but have to be called
 
s=.0
print help(clock)
print 'Time in some kind of units...  ', clock()
tmp=clock()
for a in range(1,10000):
    z=tan(atan(exp(log(sqrt(a*a)))))/a  #note atan here
    s =s+z
print  s/a  #this should be 1.
print 'using math  ',clock()-tmp

s=0.0

from scipy import *     #note new math functions imported

tmp=clock()
for b in range(1,10000):
    z=tan(arctan(exp(log(sqrt(b*b)))))/b    #note arctan here
    s =s+z
print  s/b
print 'using scipy  ',clock()-tmp                           #note that scipy is slower

za = array([[1.5,2,3],[4,5,6]])
print "floating point array follows",'\n',za
za[1,0]=1984.       #Note which element is being changed: what is row and what is column?
print 'Look at column 1, row 2 '
print za,'\n '

print "complex"
j=1
print j
print (5+6*j)**2,'\t',' note: just a real number'
print (5+6j)**2,'\t',' note: a COMPLEX number','\n '

za = array([[1,2,3],[4,5,6+6j]])  # Made a complex array because one element is complex!
print za,'\n '
print "imag part, followed by real part of the complex array above"
print za.imag         # print imag part only 
print za.real,'\n '   # print real part only

print "Fourier transform.  Yes, we can do Fourier transforms.... and?"
a=array([8,2,3,4])
print a
print fft(a)       # BUT I DONOT KNOW fft's..., later, we will cover it.

raw_input("Holding for the next set of arrays, 1-dim, 2-dim: all zeros, all 1's, identity")
x = cos(arange(5)/30.0*2*pi)  # apply function to arrays (arange-->array )
print x,'\n '                 # notice you get 5 numbers from arange(5)
print zeros((3,3)),'\n '
print ones((3,3)),'\n '
print identity(4)

raw_input("What is the smallest difference from 1?")
q=1.
for n in range(17):
    q=q/10.
    z=1.+q
    print n,"\t",q,"\t",z-1.    # note '\t' means a tab (space)

import urllib2                  # access the internet
for line in urllib2.urlopen('http://tycho.usno.navy.mil/cgi-bin/timer.pl'):
    if 'PDT' in line:      # look for Pacific Daylight Time
        print '\n ' ,'PDT',line
for line in urllib2.urlopen('http://tycho.usno.navy.mil/cgi-bin/timer.pl'):
    if 'PST' in line:      # look for Pacific Standard Time
        print '\n ' ,"PST",line   # NO! we are not on PST right now!

# dumping data to a file - you DO want to preserve something for posterity, right?
y=zeros(1001)
x=ones(1001)
fout=open("junk.txt","w")
"""The first argument is a string containing the filename.  The second argument is another
string containing a few characters describing the way in which the file will be used.
Mode can be 'r' when the file will only be read, 'w' for only writing (an existing file with
the same name will be erased), and 'a' opens the file for appending; any data written to the
file is automatically added to the end. 'r+' opens the file for both reading and writing.
The mode argument is optional; 'r' will be assumed if it's omitted."""

for i in range (5):
    x[i]=0.1*cos(pi*i/10)
    y[i]=sin(pi*i/10)
    line=str(i)+"\t"+str(x[i])+"\t"+str(y[i])  # convert numbers to strings so we can write 3 #'s on 1 line
    fout.write(line+"\n")
fout.close()  # close file...

fout=open("junk.txt","r")
while True:
    line=fout.readline()
    if len(line)==0:
        break
    print line,
fout.close()  # close file...

fout=open("junk2.txt","w")
z=cos(arange(30)*pi/30)     # much quicker! but is it right?
print '\n',z,'\n'
fout.write(str(z))
fout.close()
fout=open("junk2.txt","r")
a=fout.read(len(str(z)))    # kind of klutzy, so probably do it the harder way
print a
fout.close()
