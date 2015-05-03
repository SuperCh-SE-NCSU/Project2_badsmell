# Project2_badsmell
Bad smells 

##Collection
##Anonymization
##Tables
##Data

### Features:

The values in the table represent the number of rows of data collected for that particular feature.

|Number|Feature|
|------|-------|
|1|Total number of issues|
|2|Number of issues without comments|
|3|Number of issues each week|
|4|Total number of labels|
|5|Number of times each label was used|
|6|Mean and standard deviation of time spent in each label|
|7|"Unusually long" time a label|
|8|Mean and standard deviation number of labels assigned to each issue|
|9|Number of times each milestone was used|
|10|Percentage of issues using labels|
|11|Percentage of issues using milestones|
|12|Percentage of issues using assignees|
|13|"Unusually small" number of issues handled only by one person|
|14|"Unusually large" number of issues handle by one person|
|15|Issue participating times of each user|

##Data samples

### Features:

**1. Total number of issues**

**2. Number of issues without comments**

**3. Number of issues each week**

**4. Total number of labels**

**5. Number of times each label was used**

**6. Mean and standard deviation of time spent in each label**

**7. "Unusually long" time a label**

**8. Mean and standard deviation number of labels assigned to each issue**

**9. Number of times each milestone was used**

**10. Percentage of issues using labels**

**11. Percentage of issues using milestones**

**12. Percentage of issues using assignees**

**13. "Unusually small" number of issues handled only by one person**

**14. "Unusually large" number of issues handle by one person**

**15. Issue participating times of each user**

## Feature detection & Result

####1. Total number of issues

This feature is quite straightforward. We decide to find the total number of issues of each team. And this feature can reflect briefly how team members communicate during the development period.

<b>Scripts are found here</b>

#####Result
We counted total number of issues of each project. And here is the result.

```  
Number of issues:
  Project1: 67
  Project2: 80
  Project3: 93
```

####2. Number of issues without comments

We also want to know how many issues are actually no comments below. This feature goes deeper comparing to the first feature. And according to this feature, we can find out which issue actually makes the difference.

<b>Scripts are found here</b>

#####Result
We also counted the number of issues without comments.

```  
Number of issues without comments:
  Project1: 5
  Project2: 41
  Project3: 6
```

####3. Number of issues each week

This issue is quite interesting.  We want to find out that which period is most likely to create issues, beginning or near the deadline. And we can analyse the results, which will help to optimize the development schedule.

<b>Scripts are found here</b>

#####Result
We divided the total number of issues monthly, and get an array for each project.

```
  Project1: [24, 9, 4, 2, 5, 6, 5, 8]
```
![Project1](https://github.com/SuperCh-SE-NCSU/Project2_badsmell/blob/zhewei/project1_numberofissues_week.png)
```
  Project2: [10, 12, 4, 1, 1, 1, 1, 37, 1]
```
![Project2](https://github.com/SuperCh-SE-NCSU/Project2_badsmell/blob/zhewei/project2_numberofissues_week.png)
```
  Project3: [21, 8, 9, 2, 9, 10, 26, 5]
```
![Project3](https://github.com/SuperCh-SE-NCSU/Project2_badsmell/blob/zhewei/project3_numberofissues_week.png)

####4. Total number of labels

We want to know the total number of labels each team created. Different number of labels reflect different kinds of situations and different levels of priorities each team will set.

<b>Scripts are found here</b>

#####Result
We counted the total number of labels for each project.

```  
Total number of labels:
  Project1: 10
  Project2: 7
  Project3: 21
```

####5. Number of times each label was used

We can figure out which kind of label was used a lot of times, and which kind of label was seldom used. And the results will reflect whether the quantity and the setting of labels are reasonable or not.

<b>Scripts are found here</b>

#####Result
We also counted the number of times each label was used.

```  
  Project1: 
          develop 15
          question 5
          invalid 1
          Solved 36
          duplicate 3
          design 21
          help wanted 15
          test 5
          bug 14
          enhancement 5
```
![Project1](https://github.com/SuperCh-SE-NCSU/Project2_badsmell/blob/zhewei/project1_labels.png)
```
  Project2:
          Test Problem 23
          info! 33
          Configure Problem 3
          help wanted 29
          wontfix 1
          bug 6
          Design Problem 12
```
![Project2](https://github.com/SuperCh-SE-NCSU/Project2_badsmell/blob/zhewei/project2_labels.png)
```
  Project3:
          feature dev 27
          4. feature complete 42
          2a. feature dev 58
          5. bug 12
          wontfix 1
          2b. help wanted 1
          feature QA 22
          testing 4
          question 3
          backtrack.JS 1
          1. feature request 51
          feature request 33
          trailModel.JS 1
          3. feature QA 40
          help wanted 8
          branch 2
          deployment 3
          branch list 1
          feature complete 11
          bug 5
          resources 1
```
![Project3](https://github.com/SuperCh-SE-NCSU/Project2_badsmell/blob/zhewei/project3_labels.png)

####6. Mean and standard deviation of time spent in each label

This feature will show us mean and standard deviation of times spending in each label. And it will help us to analyse in depth. 

<b>Scripts are found here</b>

#####Result
We calculated mean and standard deviation of time spent in each label.

```  
Mean and standard deviation of time spent in each label:
  Project1:
          mean:       717715.441667
          standard:   735405.992596
  Project2:
          mean:       683042.074766
          standard:   1003264.24323
  Project3:
          mean:       428354.733945
          standard:   458374.563866
```

####7. "Unusually long" time a label

"Unusually long" time means 1.5 or 2 standard deviations time in a label. In normal distribution, 1.5 or 2 standard deviations means the data point is quite far away from the mean value. In this case, unusually long time a label may indicate team do little stuff during this time period.

<b>Scripts are found here</b>

#####Result
We counted number of labels with unusually long time, which means 1.5 or 2 standard deviations time compatring to mean value.

```  
"Unusually long" time a label:
  Project1: 14
  Project2: 10
  Project3: 29
```

####8. Mean and standard deviation number of labels assigned to each issue

This feature will show us mean and standard deviation of number of labels assigned to each issue. And in this feature, we consider label and issue together, we want to find out the reasonable of the setting of labels. Also, we want to find out whether team members used to add corresponding labels to issues or not.

<b>Scripts are found here</b>

#####Result
We calculated mean and standard deviation number of labels assigned to each issue.

```  
Mean and standard deviation number of labels assigned to each issue:
  Project1:
          Mean value          84452.1587302
          Standard deviation  173010.600703
  Project2:
          Mean value          90650.6617647
          Standard deviation  252940.849578
  Project3:
          Mean value          65775.3888889
          Standard deviation  159966.183254
```

####9. Number of times each milestone was used

We are interesting in number of milestones. And each milestone usually represents one stage in development cycle. We can analyse which software development method each team used.

<b>Scripts are found here</b>

#####Result
We counted the number of times each milestone was used.

``` 
 Project1: 
          None 11
          Final release 6
          Beta Launch  15
          V1 19
          V2 8
          System test and Report 8
 ```
![Project1](https://github.com/SuperCh-SE-NCSU/Project2_badsmell/blob/zhewei/project1_milestones.png)
 ```
  Project2:
          None 12
          Final 17
          Small Scale Test and Comparison 4
          Basic Service and Test 23
          Large Scale Test 13
```
![Project2](https://github.com/SuperCh-SE-NCSU/Project2_badsmell/blob/zhewei/project2_milestone.png)
```
  Project3:
          None 46
          v0.6 Cleanup 16
          v0.4 7
          v0.5 12
          v0.1 4
          v0.2 5
          v0.3 6
```
![Project3](https://github.com/SuperCh-SE-NCSU/Project2_badsmell/blob/zhewei/project3_milestone.png)

####10. Percentage of issues using labels

We want to see how many issues used labels.

<b>Scripts are found here</b>

#####Result
We calculated percentage of issues using labels.

```  
Percentage of issues using labels:
  Project1: 91.1% in 67 issues
  Project2: 68.8% in 80 issues
  Project3: 96.8% in 93 issues
```

####11. Percentage of issues using milestones

We want to see how many issues used milestones.

<b>Scripts are found here</b>

#####Result
We calculated percentage of issues using milestones.

```  
Percentage of issues using milestones:
  Project1: 83.6% in 69 issues
  Project2: 82.6% in 93 issues
  Project3: 52.1% in 93 issues
```

####12. Percentage of issues using assignees

We are interested in how many issues used assignees. And if the percentage of issues using assignees is high, which means responsibility distribution is clear.

<b>Scripts are found here</b>

#####Result
We also calculated percentage of issues using assignees.

```  
Percentage of issues using milestones:
  Project1: 19.1% in 69 issues
  Project2: 60.3% in 93 issues
  Project3: 72.2% in 93 issues
```

####13. "Unusually small" number of issues handled only by one person

A issue handled only by one person means this issue is opened and closed by same person and no other guys write comments below this issue. We define number of issues handles only by one person less than 10% indicates this person is a "passenger". And it means responsibility distribution of this team may be uneven.

<b>Scripts are found here</b>

#####Result
We also calculated percentage of issues using milestones.

```  
Unusually small" number of issues handled only by one person:
 Project1: 
          user 1: 40.6
          user 2: 54
          user 3: 7
  Project2:
          user 1: 1
          user 2: 4
          user 3: 20
          user 4: 78
  Project3:
          user 1: 187
          user 2: 101
          user 3: 29
          user 4: 6
```

####14. "Unusually large" number of issues handle by one person

We define number of issues handles only by one person more than 70% indicates this person is a "great dictator". And it also means responsibility distribution of this team may be uneven.

<b>Scripts are found here</b>

Result

####15. Issue participating times of each user

This feature calculates each user's frequency of attendency.

<b>Scripts are found here</b>

#####Result
We calculated issue participating times of each user.

```  
Issue participating times of each user:
  Project1: 
          user 1: 56
          user 2: 54
          user 3: 7
  Project2:
          user 1: 1
          user 2: 4
          user 3: 20
          user 4: 78
  Project3:
          user 1: 187
          user 2: 101
          user 3: 29
          user 4: 6
```

## Bad smells detector & Result 

###Issue Time Interval Detector [need Liang's data]
During the development cycle, team members will post some issues in order to communicate other members. However, the time interval between two issue creation may vary dramatically. This detector can analyse time interval to decide whether it is too long or too short. The result can reflect the process of each team. And we named it [issueTimeIntervalDetector.](https://github.com/SuperCh-SE-NCSU/Project2_badsmell/blob/zhewei/bad_smell_detector/issueTimeIntervalDetector.py) Below are pseudocode of algorithm we use to detect bad smells.
```
issueTimeInterval > mean + 2*std_dev:
    Badsmell: Too long time interval between this issue and the last.

issueTimeInterval < mean - 2*std_dev:
    Badsmell: Too little time interval between this issue and the last.

Otherwise:
    Issue interval time is normal this time
```

####Result
Because the result are too long, we eliminate some normal results and leave some bad smells.

Project 1
```
('mean:', 72013.56451612903)
('std_dev:', 209839.24439541661)
...
38. Issue interval time is normal this time
39. Issue interval time is normal this time
40. Issue interval time is normal this time
41. Badsmell: Too long time interval between this issue and the last.
42. Badsmell: Too little time interval between this issue and the last.
43. Badsmell: Too long time interval between this issue and the last.
44. Issue interval time is normal this time
45. Issue interval time is normal this time
46. Issue interval time is normal this time
47. Issue interval time is normal this time
48. Issue interval time is normal this time
...
```
Project 2
```
('mean:', 90169.373134328358)
('std_dev:', 255257.2690866554)
...
20. Issue interval time is normal this time
21. Issue interval time is normal this time
22. Issue interval time is normal this time
23. Issue interval time is normal this time
24. Issue interval time is normal this time
25. Badsmell: Too long time interval between this issue and the last.
26. Badsmell: Too long time interval between this issue and the last.
27. Issue interval time is normal this time
28. Issue interval time is normal this time
29. Issue interval time is normal this time
30. Issue interval time is normal this time
...
63. Issue interval time is normal this time
64. Issue interval time is normal this time
65. Issue interval time is normal this time
66. Badsmell: Too long time interval between this issue and the last.
...
```
Project 3
```
('mean:', 53007.370786516854)
('std_dev:', 197722.12811823591)
...
15. Issue interval time is normal this time
16. Issue interval time is normal this time
17. Issue interval time is normal this time
18. Issue interval time is normal this time
19. Issue interval time is normal this time
20. Badsmell: Too long time interval between this issue and the last.
21. Badsmell: Too little time interval between this issue and the last.
22. Issue interval time is normal this time
23. Issue interval time is normal this time
24. Issue interval time is normal this time
25. Issue interval time is normal this time
...
35. Issue interval time is normal this time
36. Issue interval time is normal this time
37. Issue interval time is normal this time
38. Issue interval time is normal this time
39. Badsmell: Too long time interval between this issue and the last.
40. Issue interval time is normal this time
41. Issue interval time is normal this time
42. Issue interval time is normal this time
43. Issue interval time is normal this time
44. Issue interval time is normal this time
45. Issue interval time is normal this time
...
```

##Issue Without Comment Detector
We found that some issues were created without comment. If the radio of issues without comments out of total issues is higher than certain threshold, we claim it is a bad smell. We named it [issueWithoutCommentDetector.](https://github.com/SuperCh-SE-NCSU/Project2_badsmell/blob/zhewei/bad_smell_detector/issueWithoutCommentDetector.py) Since issue can help team member to communicate with each other. So many issues without comment means writing issues only aims to deal with professor's rubric.

####Result
##Bad smells results
##Early warning
**Interval of created time of two adjacent issues**

**Description**

We use the trend of created time of issues to find the early warning. We assume that the interval of created time of two adjacent issues is stable if the team is developing the project in a good plan. If the team creates many issues in a short time, it means the team is rushing. If the team doesn't create a issue in a long time, it means the team may not work on the project in schedule.
Assume the number of issues is a function of time: inum=f(t), it will increase linearly as time increases. The differential of f(t) is the interval of created time of two adjacent issues. And the interval should be fluctuating little between a constant. 

**Script**

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
[Code Link] (https://github.com/SuperCh-SE-NCSU/Project2_badsmell/blob/liang/earlywarning)
##Early warning results

For project 1, the interval of created time of two adjacent issue is described in the following graph.
![Project1](https://github.com/SuperCh-SE-NCSU/Project2_badsmell/blob/liang/earlywarning/project1_interval.png)

The early warning detecting result is as following:
```
('the team may be falling behind the schedule before issue', 37)
```
For project 2, the interval of created time of two adjacent issue is described in the following graph.
![Project1](https://github.com/SuperCh-SE-NCSU/Project2_badsmell/blob/liang/earlywarning/project2_interval.png)

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
![Project1](https://github.com/SuperCh-SE-NCSU/Project2_badsmell/blob/liang/earlywarning/project3_interval.png)

The early warning detecting result is as following:
```
('the team may be falling behind the schedule before issue', 10)
('the team may be falling behind the schedule before issue', 37)
('the team may be falling behind the schedule before issue', 52)
('the team may be pushing before issue', 58)
('the team may be pushing before issue', 71)
```
