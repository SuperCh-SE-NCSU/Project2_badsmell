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
|6|Mean and standard deviation of time spent in each issue|
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

**6. Mean and standard deviation of time spent in each issue**

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

####6. Mean and standard deviation of time spent in each issue

This feature will show us mean and standard deviation of times spending in each issue. And it will help us to analyse in depth. 

<b>Scripts are found here</b>

#####Result
We calculated mean and standard deviation of time spent in each issue.

```  
Mean and standard deviation of time spent in each issue:
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

###Issue Time Duration Detector [need Liang's data]
During the development cycle, team members will post some issues in order to communicate other members. However, the time duration between two issue creation may vary dramatically. This detector can analyse time duration to decide whether it is too long or too short. The result can reflect the process of each team. And we named it [issueTimeDurationDetector.](https://github.com/SuperCh-SE-NCSU/Project2_badsmell/blob/zhewei/bad_smell_detector/issueTimeDurationDetector.py) Below are pseudocode of algorithm we use to detect bad smells.
```
if issueTimeDuration > mean + 2*std_dev:
    Badsmell: Too long time duration between this issue and the last.

if issueTimeDuration < mean - 2*std_dev:
    Badsmell: Too little time duration between this issue and the last.

Otherwise:
    Issue duration time is normal this time
```

####Result
Because the result are too long, we eliminate some normal results and leave some bad smells.

Project 1
```
('mean:', 72013.56451612903)
('std_dev:', 209839.24439541661)
...
38. Issue duration time is normal this time
39. Issue duration time is normal this time
40. Issue duration time is normal this time
41. Badsmell: Too long time duration between this issue and the last.
42. Badsmell: Too little time duration between this issue and the last.
43. Badsmell: Too long time duration between this issue and the last.
44. Issue duration time is normal this time
45. Issue duration time is normal this time
46. Issue duration time is normal this time
47. Issue duration time is normal this time
48. Issue duration time is normal this time
...
```
Project 2
```
('mean:', 90169.373134328358)
('std_dev:', 255257.2690866554)
...
20. Issue duration time is normal this time
21. Issue duration time is normal this time
22. Issue duration time is normal this time
23. Issue duration time is normal this time
24. Issue duration time is normal this time
25. Badsmell: Too long time duration between this issue and the last.
26. Badsmell: Too long time duration between this issue and the last.
27. Issue duration time is normal this time
28. Issue duration time is normal this time
29. Issue duration time is normal this time
30. Issue duration time is normal this time
...
63. Issue duration time is normal this time
64. Issue duration time is normal this time
65. Issue duration time is normal this time
66. Badsmell: Too long time duration between this issue and the last.
...
```
Project 3
```
('mean:', 53007.370786516854)
('std_dev:', 197722.12811823591)
...
15. Issue duration time is normal this time
16. Issue duration time is normal this time
17. Issue duration time is normal this time
18. Issue duration time is normal this time
19. Issue duration time is normal this time
20. Badsmell: Too long time duration between this issue and the last.
21. Badsmell: Too little time duration between this issue and the last.
22. Issue duration time is normal this time
23. Issue duration time is normal this time
24. Issue duration time is normal this time
25. Issue duration time is normal this time
...
35. Issue duration time is normal this time
36. Issue duration time is normal this time
37. Issue duration time is normal this time
38. Issue duration time is normal this time
39. Badsmell: Too long time duration between this issue and the last.
40. Issue duration time is normal this time
41. Issue duration time is normal this time
42. Issue duration time is normal this time
43. Issue duration time is normal this time
44. Issue duration time is normal this time
45. Issue duration time is normal this time
...
```

##Issue Without Comment Detector
We found that some issues were created without comment. If the radio of issues without comments out of total issues is higher than certain threshold, we claim it is a bad smell. We named it [issueWithoutCommentDetector.](https://github.com/SuperCh-SE-NCSU/Project2_badsmell/blob/zhewei/bad_smell_detector/issueWithoutCommentDetector.py) Since issue can help team member to communicate with each other. So many issues without comment may indicate that writing issues only aims to deal with professor's rubrics. Below are pseudocode of algorithm we use to detect bad smells.
```
if the radio of issueWithoutComment out of totalNumOfIssue > 20%:
    Badsmell: Too many issues without comments.
otherwise:
    The number of issues without comments is normal.
```

####Result

Project 1
```
('issueWithoutComment', 5)
('totalNumOfIssues', 67)
Normal
```
Project 2
```
('issueWithoutComment', 41)
('totalNumOfIssues', 80)
Badsmell: Too many issues without comments.
```
Project 3
```
('issueWithoutComment', 6)
('totalNumOfIssues', 93)
Normal
```

###Label Usage Detector
We can add one or more labels to each issue or each pull request in order to remind other team members. We found that some teams have many labels, but some labels were used only one or two times. So we consider this is another kind of bad smell. We named it [labelUsageDetector.](https://github.com/SuperCh-SE-NCSU/Project2_badsmell/blob/zhewei/bad_smell_detector/labelUsageDetector.py) The cause of this bad smell may be the setting of a label is not reasonable. Team members should rename it, merge it into another label or delete it. Below are pseudocode of algorithm we use to detect bad smells.(We do not detect whether a label was used too many times or not. Since label like "Solved" can be used almost every issue. And we think it is fine to do so.)
```
if labelUsage < mean - std_dev:
    Badsmell: This label was used too little times.
otherwise:
    The usage of this label is normal.
```

####Result

Project 1
```
('labelName', ['develop', 'question', 'invalid', 'Solved', 'duplicate', 'design', 'helpwanted', 'test', 'bug', 'enhancement'])
('labelUsage', [15, 5, 1, 36, 3, 21, 15, 5, 14, 5])
('mean:', 12.0)
('std_dev:', 10.139033484509261)
----------------------------------------------
The usage of [develop] is normal.
The usage of [question] is normal.
Badsmell: [invalid] was used too little times.
The usage of [Solved] is normal.
The usage of [duplicate] is normal.
The usage of [design] is normal.
The usage of [helpwanted] is normal.
The usage of [test] is normal.
The usage of [bug] is normal.
The usage of [enhancement] is normal.
```
Project 2
```
('labelName', ['Test Problem', 'info!', 'Configure Problem', 'help wanted', 'wontfix', 'bug', 'Design Problem'])
('labelUsage', [23, 33, 3, 29, 1, 6, 12])
('mean:', 15.285714285714286)
('std_dev:', 12.032269536711752)
----------------------------------------------
The usage of [Test Problem] is normal.
The usage of [info!] is normal.
Badsmell: [Configure Problem] was used too little times.
The usage of [help wanted] is normal.
Badsmell: [wontfix] was used too little times.
The usage of [bug] is normal.
The usage of [Design Problem] is normal.
```
Project 3
```
('labelName', ['feature dev', '4. feature complete', '2a. feature dev', '5. bug', 'wontfix', '2b. help wanted', 'feature QA', 'testing', 'question', 'backtrack.JS', '1. feature request', 'feature request', 'trailModel.JS', '3. feature QA', 'help wanted', 'branch', 'deployment', 'branch list', 'feature complete', 'bug', 'resources'])
('labelUsage', [27, 42, 58, 12, 1, 1, 22, 4, 3, 1, 51, 33, 1, 40, 8, 2, 3, 1, 11, 5, 1])
('mean:', 15.571428571428571)
('std_dev:', 18.175261650232763)
----------------------------------------------
The usage of [feature dev] is normal.
The usage of [4. feature complete] is normal.
The usage of [2a. feature dev] is normal.
The usage of [5. bug] is normal.
The usage of [wontfix] is normal.
The usage of [2b. help wanted] is normal.
The usage of [feature QA] is normal.
The usage of [testing] is normal.
The usage of [question] is normal.
The usage of [backtrack.JS] is normal.
The usage of [1. feature request] is normal.
The usage of [feature request] is normal.
The usage of [trailModel.JS] is normal.
The usage of [3. feature QA] is normal.
The usage of [help wanted] is normal.
The usage of [branch] is normal.
The usage of [deployment] is normal.
The usage of [branch list] is normal.
The usage of [feature complete] is normal.
The usage of [bug] is normal.
The usage of [resources] is normal.
```

###User Participate Detector
In a good team, the difference of each member's degree of participation, in other words, the difference of each member's contribution should not be too large. Otherwise, there must be "great dictator" or "passenger" in this team, which can become another bad smell. We named it [userParticipateDetector.](https://github.com/SuperCh-SE-NCSU/Project2_badsmell/blob/zhewei/bad_smell_detector/userParticipateDetector.py) Below are pseudocode of algorithm we use to detect bad smells. <b>(We consider not only commit times of each member, but also the issue participant times of each member.)</b>
```
ratio1=eachMemberIssueParticipateTimes[i]*1.0/sumOfIssueParticipateTimes
ratio2=eachMemberCommitTimes[i]*1.0/sumOfCommitTimes
if ratio1 < 10% or ratio2 < 10%:
  	Badsmell: This user is likely be a 'passenger'.
if ratio1 > 75% or ratio2 > 75%:
	Badsmell: This user is likely be a 'great dictator'.
otherwise:
	The participant of this user is normal.
```

####Result

Project 1
```
('eachMemberIssueParticipateTimes', [56, 54, 7])
('eachMemberCommitTimes', [193, 180, 82])
----------------------------------------------
The participant of this user is normal.
The participant of this user is normal.
Badsmell: This user is likely to be a 'passenger'.
```
Project 2
```
('eachMemberIssueParticipateTimes', [78, 20, 4, 1])
('eachMemberCommitTimes', [48, 48, 26, 22])
----------------------------------------------
Badsmell: This user is likely be a 'great dictator'.
The participant of this user is normal.
Badsmell: This user is likely to be a 'passenger'.
Badsmell: This user is likely to be a 'passenger'.
```
Project 3
```
('eachMemberIssueParticipateTimes', [187, 101, 29, 6])
('eachMemberCommitTimes', [151, 127, 62, 38])
----------------------------------------------
The participant of this user is normal.
The participant of this user is normal.
Badsmell: This user is likely to be a 'passenger'.
Badsmell: This user is likely to be a 'passenger'.
```

###Weekly Issue Detector
We are also interesting in the amount of weekly issues of each team. And the result can reflect which period is the most active period of each team. If one week had too many or too little issues been created, we consider it can be a bad smell. Since one team may catch up the schedule in one week. We named it [weeklyIssueDetector.](https://github.com/SuperCh-SE-NCSU/Project2_badsmell/blob/zhewei/bad_smell_detector/weeklyIssueDetector.py) Below are pseudocode of algorithm we use to detect bad smells.
```
if weeklyIssue > mean + std_dev:
	Badsmell: Too many issues in this week.
if weeklyIssue < mean - std_dev:
	Badsmell: Too little issues in this week.
otherwise:
	Issue number is normal in this week.
```

####Result

Project 1
```
('weeklyIssue:', [24, 9, 4, 2, 5, 6, 5, 8])
('mean:', 7.875)
('std_dev:', 6.4311254847032799)
----------------------------------------------
Badsmell: Too many issues in this week.
Issue number is normal in this week.
Issue number is normal in this week.
Issue number is normal in this week.
Issue number is normal in this week.
Issue number is normal in this week.
Issue number is normal in this week.
Issue number is normal in this week.
```
Project 2
```
('weeklyIssue:', [10, 12, 4, 1, 1, 1, 1, 37, 1])
('mean:', 7.5555555555555554)
('std_dev:', 11.156573658721083)
----------------------------------------------
Issue number is normal in this week.
Issue number is normal in this week.
Issue number is normal in this week.
Issue number is normal in this week.
Issue number is normal in this week.
Issue number is normal in this week.
Issue number is normal in this week.
Badsmell: Too many issues in this week.
Issue number is normal in this week.
```
Project 3
```
('weeklyIssue:', [21, 8, 9, 2, 9, 10, 26, 5])
('mean:', 11.25)
('std_dev:', 7.5787531956120588)
----------------------------------------------
Badsmell: Too many issues in this week.
Issue number is normal in this week.
Issue number is normal in this week.
Badsmell: Too little issues in this week.
Issue number is normal in this week.
Issue number is normal in this week.
Badsmell: Too many issues in this week.
Issue number is normal in this week.
```







##Early warning

**Issue Interval early Warning**

**Description**

We use the trend of created time of issues to find the early warning. We assume that the interval of created time of two adjacent issues is stable if the team is developing the project in a good plan. If the team creates many issues in a short time, it means the team is rushing. If the team doesn't create a issue in a long time, it means the team may not work on the project in schedule.
Assume the number of issues is a function of time: inum=f(t), it will increase linearly as time increases. The differential of f(t) is the interval of created time of two adjacent issues. And the interval should be fluctuating little between a constant. 

**Script**

We implement the issue interval early warning in the following script:
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
