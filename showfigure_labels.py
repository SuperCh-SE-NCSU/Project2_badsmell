import matplotlib.pyplot as plt
import numpy as np



labels1=[15,5,1,36,3,21,15,5,14,5]
labels2=[23,33,3,29,1,6,12]
labels3=[27,42,58,12,1,1,22,4,3,1,51,33,1,40,8,2,3,1,11,5,1]

n_groups=len(labels1)
meansone=range(1,n_groups,1)
weekcount=labels1

fig,ax=plt.subplots()
index = np.arange(n_groups)  
bar_width = 0.35  
 
opacity = 0.4  
rects1 = plt.bar(index+0.5, weekcount, bar_width,alpha=opacity, color='b',label='Used Times')  
    #rects2 = fbadsmell1.bar(index + bar_width, means_women, bar_width,alpha=opacity,col    or='r',label='Women')  
 
plt.xlabel('Label')  
plt.ylabel('Used Times')  
plt.title('Number of Times Each Label was Used')  
plt.xticks(index + 0.7, ('Develop','Question','Invalid','Solved','Duplicate','Design','Help Wanted','Test','Bug','Enhancement'))  
#fbadsmell1.ylim(0,40)  
plt.legend()  
       
plt.show()


n_groups=len(labels2)
meansone=range(1,n_groups,1)
weekcount=labels2

fig,ax=plt.subplots()
index = np.arange(n_groups)  
bar_width = 0.35  
 
opacity = 0.4  
rects1 = plt.bar(index+0.5, weekcount, bar_width,alpha=opacity, color='b',label='Used Times')  
    #rects2 = fbadsmell1.bar(index + bar_width, means_women, bar_width,alpha=opacity,col    or='r',label='Women')  
 
plt.xlabel('Label')  
plt.ylabel('Used Times')  
plt.title('Number of Times Each Label was Used')  
plt.xticks(index + 0.7, ('Test Problem', 'info!','Configure Problem','help wanted','wontfix','bug','Design Problem'))  
#fbadsmell1.ylim(0,40)  
plt.legend()  
       
plt.show()


n_groups=len(labels3)
meansone=range(1,n_groups,1)
weekcount=labels3

fig,ax=plt.subplots()
index = np.arange(n_groups)  
bar_width = 0.35  
 
opacity = 0.4  
rects1 = plt.bar(index+0.5, weekcount, bar_width,alpha=opacity, color='b',label='Used Times')  
    #rects2 = fbadsmell1.bar(index + bar_width, means_women, bar_width,alpha=opacity,col    or='r',label='Women')  
 
plt.xlabel('Label')  
plt.ylabel('Used Times')  
plt.title('Number of Times Each Label was Used')  
#plt.xticks(index + 0.7, ('Person 1', 'Person 2', 'Person 3'))  
#fbadsmell1.ylim(0,40)  
plt.legend()  
       
plt.show()
