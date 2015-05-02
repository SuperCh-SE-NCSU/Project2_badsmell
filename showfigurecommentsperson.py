import matplotlib.pyplot as plt
import numpy as np



ccommentsperperson1=[54,56,7]
commentsperperson2=[78,4,1,20]
commentsperperson3=[29,101,187,6]

n_groups=len(ccommentsperperson1)
meansone=range(1,n_groups,1)
weekcount=ccommentsperperson1

fig,ax=plt.subplots()
index = np.arange(n_groups)  
bar_width = 0.35  
 
opacity = 0.4  
rects1 = plt.bar(index+0.5, weekcount, bar_width,alpha=opacity, color='b',label='Number of Comments')  
    #rects2 = fbadsmell1.bar(index + bar_width, means_women, bar_width,alpha=opacity,col    or='r',label='Women')  
 
plt.xlabel('Person')  
plt.ylabel('Number of Comments')  
plt.title('Number of Comments for Every Participant')  
plt.xticks(index + 0.7, ('Person 1','Person 2','Person 3'))  
#fbadsmell1.ylim(0,40)  
plt.legend()  
       
plt.show()


n_groups=len(commentsperperson2)
meansone=range(1,n_groups,1)
weekcount=commentsperperson2

fig,ax=plt.subplots()
index = np.arange(n_groups)  
bar_width = 0.35  
 
opacity = 0.4  
rects1 = plt.bar(index+0.5, weekcount, bar_width,alpha=opacity, color='b',label='Number of Comments')  
    #rects2 = fbadsmell1.bar(index + bar_width, means_women, bar_width,alpha=opacity,col    or='r',label='Women')  
 
plt.xlabel('Person')  
plt.ylabel('Number of Comments')  
plt.title('Number of Comments for Every Participant')  
plt.xticks(index + 0.7, ('Person 1', 'Person 2','Person 3'))  
#fbadsmell1.ylim(0,40)  
plt.legend()  
       
plt.show()


n_groups=len(commentsperperson3)
meansone=range(1,n_groups,1)
weekcount=commentsperperson3

fig,ax=plt.subplots()
index = np.arange(n_groups)  
bar_width = 0.35  
 
opacity = 0.4  
rects1 = plt.bar(index+0.5, weekcount, bar_width,alpha=opacity, color='b',label='Number of Comments')  
    #rects2 = fbadsmell1.bar(index + bar_width, means_women, bar_width,alpha=opacity,col    or='r',label='Women')  
 
plt.xlabel('Week')  
plt.ylabel('Number of Comments')  
plt.title('Number of Comments for Every Participant')  
plt.xticks(index + 0.7, ('Person 1', 'Person 2', 'Person 3'))  
#fbadsmell1.ylim(0,40)  
plt.legend()  
       
plt.show()
