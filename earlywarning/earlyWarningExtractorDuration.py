import json
from pprint import pprint
import matplotlib.pyplot as plt
import numpy as np

with open('duration3.json') as data_file:    
    data = json.load(data_file)

keylist=map(int,data.keys())
keylist.sort()
        
            
print data

plt.xlabel('Interval')
plt.ylabel('Time(s)')
plt.title('The Duration of Issue')
xa=list()
ya=list()
for i in keylist:
    xa.append(i)
    ya.append(data[str(i).encode('utf-8')])

plt.plot(xa,ya,'r*-')
plt.show()
