import matplotlib.pyplot as plt
import numpy as np

plt.figure()

numberofissueWeek1=[24, 9, 4, 2, 5, 6, 5, 8]
numberofissueWeek2=[10, 12, 4, 1, 1, 1, 1, 37, 1]
numberofissueWeek3=[21, 8, 9, 2, 9, 10, 26, 5]

n_groups=len(numberofissueWeek1)
meansone=range(1,n_groups,1)
weekcount=numberofissueWeek1

fig,ax=plt.subplots()
index = np.arange(n_groups)  
bar_width = 0.35  
 
opacity = 0.4  
rects1 = plt.bar(index+bar_width, weekcount, bar_width,alpha=opacity, color='b',label=    'Number of issues')  
    #rects2 = fbadsmell1.bar(index + bar_width, means_women, bar_width,alpha=opacity,col    or='r',label='Women')  
 
plt.xlabel('Week')  
plt.ylabel('Number of Issues')  
plt.title('Number of Issues Every Week')  
#fbadsmell1.xticks(index + bar_width, ('A', 'B', 'C', 'D', 'E'))  
#fbadsmell1.ylim(0,40)  
plt.legend()  
       
plt.show()


n_groups=len(numberofissueWeek2)
meansone=range(1,n_groups,1)
weekcount=numberofissueWeek2

fig,ax=plt.subplots()
index = np.arange(n_groups)  
bar_width = 0.35  
 
opacity = 0.4  
rects1 = plt.bar(index+bar_width, weekcount, bar_width,alpha=opacity, color='b',label=    'Number of issues')  
    #rects2 = fbadsmell1.bar(index + bar_width, means_women, bar_width,alpha=opacity,col    or='r',label='Women')  
 
plt.xlabel('Week')  
plt.ylabel('Number of Issues')  
plt.title('Number of Issues Every Week')  
#fbadsmell1.xticks(index + bar_width, ('A', 'B', 'C', 'D', 'E'))  
#fbadsmell1.ylim(0,40)  
plt.legend()  
       
plt.show()


n_groups=len(numberofissueWeek3)
meansone=range(1,n_groups,1)
weekcount=numberofissueWeek3

fig,ax=plt.subplots()
index = np.arange(n_groups)  
bar_width = 0.35  
 
opacity = 0.4  
rects1 = plt.bar(index+bar_width, weekcount, bar_width,alpha=opacity, color='b',label=    'Number of issues')  
    #rects2 = fbadsmell1.bar(index + bar_width, means_women, bar_width,alpha=opacity,col    or='r',label='Women')  
 
plt.xlabel('Week')  
plt.ylabel('Number of Issues')  
plt.title('Number of Issues Every Week')  
#fbadsmell1.xticks(index + bar_width, ('A', 'B', 'C', 'D', 'E'))  
#fbadsmell1.ylim(0,40)  
plt.legend()  
       
plt.show()
