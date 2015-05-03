import json
from pprint import pprint
import matplotlib.pyplot as plt
import numpy as np

with open('duration3.json') as data_file:    
    data = json.load(data_file)

keylist=map(int,data.keys())
keylist.sort()
        
            
print data

plt.xlabel('Issue')
plt.ylabel('Time(s)')
plt.title('The Duration of Issue')
xa=list()
ya=list()
for i in keylist:
    xa.append(i)
    ya.append(data[str(i).encode('utf-8')])

sumtime=0
timethreshold=60*60*24*12
for i in range(0,len(xa)-1,1):
    if ya[i]>2000000:
        sumtime=sumtime+ya[i]
    else:
        sumtime=0
    if sumtime>timethreshold:
        print('The team may be struggling at this moment, issue: '+str(i))
        sumtime=0
plt.plot(xa,ya,'r*-')
plt.show()
