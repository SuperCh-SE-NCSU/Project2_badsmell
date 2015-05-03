import matplotlib.pyplot as plt
import numpy as np



milestoneissues1=[11,6,15,19,8,8]
milestoneissues2=[12,17,4,23,13]
milestoneissues3=[46,16,7,12,4,5,6]

n_groups=len(milestoneissues1)
meansone=range(1,n_groups,1)
weekcount=milestoneissues1

fig,ax=plt.subplots()
index = np.arange(n_groups)  
bar_width = 0.35  
 
opacity = 0.4  
rects1 = plt.bar(index+0.5, weekcount, bar_width,alpha=opacity, color='b',label='Number of Issues')  
    #rects2 = fbadsmell1.bar(index + bar_width, means_women, bar_width,alpha=opacity,col    or='r',label='Women')  
 
plt.xlabel('Milestone')  
plt.ylabel('Number of Issues')  
plt.title('Number of Issues for Each Milestone')  
plt.xticks(index + 0.7, ('None','Final release','Beta Launch','V1','V2','System test and Report'))  
#fbadsmell1.ylim(0,40)  
plt.legend()  
       
plt.show()


n_groups=len(milestoneissues2)
meansone=range(1,n_groups,1)
weekcount=milestoneissues2

fig,ax=plt.subplots()
index = np.arange(n_groups)  
bar_width = 0.35  
 
opacity = 0.4  
rects1 = plt.bar(index+0.5, weekcount, bar_width,alpha=opacity, color='b',label='Number of Issues')  
    #rects2 = fbadsmell1.bar(index + bar_width, means_women, bar_width,alpha=opacity,col    or='r',label='Women')  
 
plt.xlabel('Milestone')  
plt.ylabel('Number of Issues')  
plt.title('Number of Issues for Each Milestone')  
plt.xticks(index + 0.7, ('None', 'Final','Small Scale Test and Comparison','Basic Service and Test','Large Scale Test'))  
#fbadsmell1.ylim(0,40)  
plt.legend()  
       
plt.show()


n_groups=len(milestoneissues3)
meansone=range(1,n_groups,1)
weekcount=milestoneissues3

fig,ax=plt.subplots()
index = np.arange(n_groups)  
bar_width = 0.35  
 
opacity = 0.4  
rects1 = plt.bar(index+0.5, weekcount, bar_width,alpha=opacity, color='b',label='Number of Issues')  
    #rects2 = fbadsmell1.bar(index + bar_width, means_women, bar_width,alpha=opacity,col    or='r',label='Women')  
 
plt.xlabel('Milestone')  
plt.ylabel('Number of Issues')  
plt.title('Number of Issues for Each Milestone')  
plt.xticks(index + 0.7, ('None', 'v0.6 Cleanup','v0.4','v0.5','v0.1','v0.2','v0.3'))  
#fbadsmell1.ylim(0,40)  
plt.legend()  
       
plt.show()
