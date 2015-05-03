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

Sample data table: 

| Commit Sha |date|  
|----------- |----|
|0734a1482f009b4c6c8dbe16e34daf3c75567373|2015-04-15 21:40:03 UTC|
|b71398d37c208a57e006753bcd6fd7ccee89357a|2015-04-15 20:25:37 UTC|

The links to the entire data set for this extractor can be found here
* [Project 1](features/uneven_commits/feature_results/project_1_commits.csv)
* [Project 2](features/uneven_commits/feature_results/project_2_commits.csv)
* [Project 3](features/uneven_commits/feature_results/project_3_commits.csv)

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


##Feature detection & Results

**1. Total number of issues**

This feature is quite straightforward. We decide to find the total number of issues of each team. And this feature can reflect briefly how team members communicate during the development period.

#####Result
We counted total number of issues of each project. And here is the result.

```  
Number of issues:
  Project1: 69
  Project2: 93
  Project3: 93
```

**2. Number of issues without comments**

We also want to know how many issues are actually no comments below. This feature goes deeper comparing to the first feature. And according to this feature, we can find out which issue actually makes the difference.

#####Result
We also counted the number of issues without comments.

```  
Number of issues without comments:
  Project1: 5
  Project2: 41
  Project3: 6
```

**3. Number of issues each week**

This issue is quite interesting.  We want to find out that which period is most likely to create issues, beginning or near the deadline. And we can analyse the results, which will help to optimize the development schedule.

#####Result
We divided the total number of issues monthly, and get an array for each project.

```  
Number of issues every week:
  Project1: [24, 9, 4, 2, 5, 6, 5, 8]
  Project2: [10, 12, 4, 1, 1, 1, 1, 37, 1]
  Project3: [21, 8, 9, 2, 9, 10, 26, 5]
```

**4. Total number of labels**

We want to know the total number of labels each team created. Different number of labels reflect different kinds of situations and different levels of priorities each team will set.

#####Result
We counted the total number of labels for each project.

```  
Total number of labels:
  Project1: 10
  Project2: 7
  Project3: 21
```

**5. Number of times each label was used**

We can figure out which kind of label was used a lot of times, and which kind of label was seldom used. And the results will reflect whether the quantity and the setting of labels are reasonable or not.

#####Result
We also counted the number of times each label was used.

![Project1](https://github.com/SuperCh-SE-NCSU/Project2_badsmell/blob/zhewei/project1_labels.png)
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
![Project1](https://github.com/SuperCh-SE-NCSU/Project2_badsmell/blob/zhewei/project2_labels.png)
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
![Project1](https://github.com/SuperCh-SE-NCSU/Project2_badsmell/blob/zhewei/project3_labels.png)
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

**6. Mean and standard deviation of time spent in each label**

This feature will show us mean and standard deviation of times spending in each label. And it will help us to analyse in depth. 

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

**7. "Unusually long" time a label**

"Unusually long" time means 1.5 or 2 standard deviations time in a label. In normal distribution, 1.5 or 2 standard deviations means the data point is quite far away from the mean value. In this case, unusually long time a label may indicate team do little stuff during this time period.

#####Result
We counted number of labels with unusually long time, which means 1.5 or 2 standard deviations time compatring to mean value.

```  
"Unusually long" time a label:
  Project1: 14
  Project2: 10
  Project3: 29
```

**8. Mean and standard deviation number of labels assigned to each issue**

This feature will show us mean and standard deviation of number of labels assigned to each issue. And in this feature, we consider label and issue together, we want to find out the reasonable of the setting of labels. Also, we want to find out whether team members used to add corresponding labels to issues or not.

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

**9. Number of times each milestone was used**

We are interesting in number of milestones. And each milestone usually represents one stage in development cycle. We can analyse which software development method each team used.

#####Result
We counted the number of times each milestone was used.

![Project1](https://github.com/SuperCh-SE-NCSU/Project2_badsmell/blob/zhewei/project1_milestones.png)
``` 
 Project1: 
          None 11
          Final release 6
          Beta Launch  15
          V1 19
          V2 8
          System test and Report 8
 ```
![Project1](https://github.com/SuperCh-SE-NCSU/Project2_badsmell/blob/zhewei/project2_milestones.png)
 ```
  Project2:
          None 12
          Final 17
          Small Scale Test and Comparison 4
          Basic Service and Test 23
          Large Scale Test 13
```
![Project1](https://github.com/SuperCh-SE-NCSU/Project2_badsmell/blob/zhewei/project3_milestones.png)
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

**10. Percentage of issues using labels**

We want to see how many issues used labels.

#####Result
We calculated percentage of issues using labels.

```  
Percentage of issues using labels:
  Project1: 91.3% in 69 issues
  Project2: 73.1% in 93 issues
  Project3: 96.8% in 93 issues
```

**11. Percentage of issues using milestones**

We want to see how many issues used milestones.

#####Result
We calculated percentage of issues using milestones.

```  
Percentage of issues using milestones:
  Project1: 83.6% in 69 issues
  Project2: 82.6% in 93 issues
  Project3: 52.1% in 93 issues
```

**12. Percentage of issues using assignees**

We are interested in how many issues used assignees. And if the percentage of issues using assignees is high, which means responsibility distribution is clear.

#####Result
We also calculated percentage of issues using assignees.

```  
Percentage of issues using milestones:
  Project1: 19.1% in 69 issues
  Project2: 60.3% in 93 issues
  Project3: 72.2% in 93 issues
```

**13. "Unusually small" number of issues handled only by one person**

A issue handled only by one person means this issue is opened and closed by same person and no other guys write comments below this issue. We define number of issues handles only by one person less than 10% indicates this person is a "passenger". And it means responsibility distribution of this team may be uneven.

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

**14. "Unusually large" number of issues handle by one person**

We define number of issues handles only by one person more than 70% indicates this person is a "great dictator". And it also means responsibility distribution of this team may be uneven.

Result

**15. Issue participating times of each user**

This feature calculates each user's frequency of attendency.

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

##Bad smells detector
##Bad smells results
##Early warning
Description
We use the trend of time when issues are created and closed to do early warning 
##Early warning results

