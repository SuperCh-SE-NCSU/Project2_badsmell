import json
from pprint import pprint
import matplotlib.pyplot as plt
import numpy as np

with open('createtimeproject1.json') as data_file:    
    data = json.load(data_file)

keylist=map(int,data.keys())
keylist.sort()
interval=list()

meaninterval=float(0)       #mean of interval
threshold=float(60*60*12)   #threshold for early warning extractor
thresholdnumbelow=ArithmeticError
thresholdnumup=1

belowinterval=0
upinterval=0
for i in range(1,len(keylist)-1):
    interval.append(data[str(keylist[i]).encode('utf-8')]-data[str(keylist[i-1]).encode('utf-8')])

for i in range(0,len(interval)-1):
    meaninterval=(meaninterval*i+interval[i])/(i+1)
    if interval[i]<meaninterval-threshold:
        belowinterval=belowinterval+1
    else:
        if interval[i]>meaninterval+2*threshold:
            upinterval=upinterval+1
        else:
            upinterval=0
            belowinterval=0
    if belowinterval>thresholdnumbelow:
        print('the team may be pushing before issue',i)
        belowinterval=0
    if upinterval>thresholdnumup:
        print('the team may be falling behind the schedule before issue',i)
        upinterval=0
        
            
print interval
index = np.arange(len(interval))
plt.xlabel('Interval')
plt.ylabel('Time(s)')
plt.title('The Interval of created time of two adjacent issues')
plt.plot(index,interval,'r*-')
plt.show()
