# Project2_badsmell
Bad smells 

##Collection
##Anonymization
##Tables
##Data
##Data samples
##Feature detection
##Feature detection results
##Bad smells detector
##Bad smells results
##Early warning
Description
We use the trend of created time of issues to find the early warning. We assume that the interval of created time of two adjacent issues is stable if the team is developing the project in a good plan. If the team creates many issues in a short time, it means the team is rushing. If the team doesn't create a issue in a long time, it means the team may not work on the project in schedule.
Assume the number of issues is a function of time: inum=f(t), it will increase linearly as time increases. The differential of f(t) is the interval of created time of two adjacent issues. And the interval should be fluctuating little between a constant. 
We define the script as following:
```python
meaninterval=float(0)       #mean of interval
threshold=float(60*60*12)   #threshold for early warning extractor
thresholdnumbelow=4         #threshold indicating the team may be rushing
thresholdnumup=1            #threshold indicating the team may be following behind the schedule
belowinterval=0             #the number of intervals below mean-threshold
upinterval=0                #the number of intervals above mean+2*threshold

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
```
##Early warning results
For project 1, the interval of created time of two adjacent issue is described in the following graph.
![Project1](https://github.com/SuperCh-SE-NCSU/Project2_badsmell/earlywarning/project1_interval.png)
The early warning detecting result is as following:
```
('the team may be falling behind the schedule before issue', 37)
```
For project 2, the interval of created time of two adjacent issue is described in the following graph.
![Project1](https://github.com/SuperCh-SE-NCSU/Project2_badsmell/earlywarning/project2_interval.png)
The early warning detecting result is as following:
```
('the team may be pushing before issue', 10)
('the team may be falling behind the schedule before issue', 26)
('the team may be falling behind the schedule before issue', 28)
('the team may be pushing before issue', 35)
('the team may be pushing before issue', 40)
('the team may be pushing before issue', 49)
('the team may be pushing before issue', 54)
('the team may be pushing before issue', 59)
('the team may be pushing before issue', 64)
```
For project 3, the interval of created time of two adjacent issue is described in the following graph.
![Project1](https://github.com/SuperCh-SE-NCSU/Project2_badsmell/earlywarning/blob/liang/project3_interval.png)
The early warning detecting result is as following:
```
('the team may be falling behind the schedule before issue', 10)
('the team may be falling behind the schedule before issue', 37)
('the team may be falling behind the schedule before issue', 52)
('the team may be pushing before issue', 58)
('the team may be pushing before issue', 71)
```
