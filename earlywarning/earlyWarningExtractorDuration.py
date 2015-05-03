import json
from pprint import pprint
import matplotlib.pyplot as plt
import numpy as np
from pylab import *
with open('duration3.json') as data_file:    
    data = json.load(data_file)

keylist=map(int,data.keys())
keylist.sort()
        
plt.xlabel('Issue')
plt.ylabel('Time(s)')
plt.title('The Duration of Issue')
xa=list()
ya=list()
for i in keylist:
    xa.append(i)
    ya.append(data[str(i).encode('utf-8')])

len1=len(xa)
len2=len(ya)
xap=[xa[:len1/2], xa[len1/2:]]
yap=[ya[:len2/2], ya[len2/2:]]
for i in range(2):
    tempx=xap[i]
    tempy=yap[i]
    m,b = polyfit(tempx, tempy, 1)
    fit=polyfit(tempx,tempy,2)
    fit_fn=poly1d(fit)
    plt.plot(tempx, fit_fn(tempx), '--k') 

sumtime=0
timethreshold=60*60*24*12
print('method 1')
for i in range(0,len(xa)-1,1):
    if ya[i]>2000000:
        sumtime=sumtime+ya[i]
    else:
        sumtime=0
    if sumtime>timethreshold:
        print('The team may be struggling at this moment, issue: '+str(i))
        sumtime=0
print('-------------------------------')
print('method 2')
km=list()
for i in range(8,len(xa)-1,1):
    tempx=xa[(i-8):i]
    tempy=ya[(i-8):i]
    m,b = polyfit(tempx, tempy, 1)
    fit=polyfit(tempx,tempy,1)
    fit_fn=poly1d(fit)
    if m>150000:
        print('The team may be waiting at this moment, issue: '+str(i))
    km.append(m)
print(km)
plt.plot(xa,ya,'r*-')
plt.show()
