# Project2_badsmell
Bad smells 

##Collection
We selected three projects (our project is one of them), and extracted all the issues from these projects. <br/>
1. Projects with more issues are preferred.<br/>
2. Projects with more labels are proferred.
Then the gitable.py file is used to extract the issues, labels, milestones for each project.

##Anonymization
We labelled these three projects as Project1, Project2, Project3.In the dataset we extracted from these projects, we replace the specific username with user1,user2,etc. And there is no clue telling about the the content of these projects in the features we extracted.<br/>

##Tables
Data extracted from issues are stored in a CSV file.
Then the Statistical measures like the min, max, accumulation, mean and standard deviation of the data set were extracted, which are the features that we want. All the features are represented by numbers, then Some values are set to detect bad smells based on the comparison of the results and these values.

##Data

We extracted all the issues from the three projects by running code from the given file ```gitable.py```.
Then we extracted 14 features that we defined from the issues for these three projects.

#### Features

|Number|Feature|
|------|-------|
|1|Total number of issues|
|2|Number of issues without comments|
|3|Number of issues each week|
|4|Total number of labels|
|5|Number of times each label was used|
|6|Mean and standard deviation of time spent in each issue|
|7|Number of issues with "unusually long" time|
|8|Mean and standard deviation number of labels assigned to each issue|
|9|Number of times each milestone was used|
|10|Percentage of issues using labels|
|11|Percentage of issues using milestones|
|12|Percentage of issues using assignees|
|13|"Unusually small or large" number of commits made by one person|
|14|Issue participating times of each user|

##Data samples

####1. Issue info
issue_id | user | create time | duration time | assignee_id | comments number |
---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- |
3 | user1 | 1425291744 | 12536 | user2| 0 |
8 | user2 | 1473654743 | 1426211865 | none| 6 |

####2. Issue number per week
week 1 | week 2 | week 3 | week 4 | week 5 | week 6 | week 7 | week 8 | week 9 |
---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | 
10 | 12 | 4 | 1 | 1 | 1 | 1 | 37 | 2 |  
21 | 8 | 9 | 2 | 9 | 10 | 27 | 26 | 5 |

[project1] (https://github.com/SuperCh-SE-NCSU/Project2_badsmell/blob/zhewei/Data/project1/issueNumberPerWeek1.csv) |
[project2] (https://github.com/SuperCh-SE-NCSU/Project2_badsmell/blob/zhewei/Data/project2/issueNumberPerWeek2.csv) |
[project3] (https://github.com/SuperCh-SE-NCSU/Project2_badsmell/blob/zhewei/Data/project3/issueNumberPerWeek3.csv)

####3. Label info
label_id | name | number of use |
---- | ---- | ---- |
1 | develop | 15 |
4 | Solved | 36 |

[project1] (https://github.com/SuperCh-SE-NCSU/Project2_badsmell/blob/zhewei/Data/project1/labelInfo1.csv) |
[project2] (https://github.com/SuperCh-SE-NCSU/Project2_badsmell/blob/zhewei/Data/project2/labelInfo2.csv) |
[project3] (https://github.com/SuperCh-SE-NCSU/Project2_badsmell/blob/zhewei/Data/project3/labelInfo3.csv)

####4. Commit info
username | number of commit | percentage of use |
---- | ---- | ---- |
user1 | 193 | 42.4% |
user3 | 82 |18.1% |

[project1] (https://github.com/SuperCh-SE-NCSU/Project2_badsmell/blob/zhewei/Data/project1/commitInfo1.csv) |
[project2] (https://github.com/SuperCh-SE-NCSU/Project2_badsmell/blob/zhewei/Data/project2/commitInfo2.csv) |
[project3] (https://github.com/SuperCh-SE-NCSU/Project2_badsmell/blob/zhewei/Data/project3/commitInfo3.csv)

####5. Milestone info
milestone_id | name | number of use |
---- | ---- | ---- |
1 | Beta Launch | 15 |
3 | V2 | 8 |

[project1] (https://github.com/SuperCh-SE-NCSU/Project2_badsmell/blob/zhewei/Data/project1/milestoneInfo1.csv) |
[project2] (https://github.com/SuperCh-SE-NCSU/Project2_badsmell/blob/zhewei/Data/project2/milestoneInfo2.csv) |
[project3] (https://github.com/SuperCh-SE-NCSU/Project2_badsmell/blob/zhewei/Data/project3/milestoneInfo3.csv)

## Feature detection & Result

####1. Total number of issues

This feature is quite straightforward. We decide to find the total number of issues of each team. And this feature can reflect briefly how team members communicate during the development period.

[Script Link] (https://github.com/SuperCh-SE-NCSU/Project2_badsmell/blob/liang/feature_extractor/featureExtracter1.py)

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

[Script Link] (https://github.com/SuperCh-SE-NCSU/Project2_badsmell/blob/liang/feature_extractor/featureExtracter1.py)

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

[Script Link] (https://github.com/SuperCh-SE-NCSU/Project2_badsmell/blob/liang/feature_extractor/featureExtracter1.py)

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

[Script Link] (https://github.com/SuperCh-SE-NCSU/Project2_badsmell/blob/liang/feature_extractor/featureExtracter1.py)

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

[Script Link] (https://github.com/SuperCh-SE-NCSU/Project2_badsmell/blob/liang/feature_extractor/featureExtracter1.py)

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

[Script Link] (https://github.com/SuperCh-SE-NCSU/Project2_badsmell/blob/liang/feature_extractor/featureExtracter1.py)

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

####7. Number of issues with "unusually long" time

"Unusually long" time means 1.5 or 2 standard deviations time in a label. In normal distribution, 1.5 or 2 standard deviations means the data point is quite far away from the mean value. In this case, unusually long time a label may indicate team do little stuff during this time period.

[Script Link] (https://github.com/SuperCh-SE-NCSU/Project2_badsmell/blob/liang/feature_extractor/featureExtracter1.py)

#####Result
We counted number of labels with unusually long time, which means 1.5 or 2 standard deviations time compatring to mean value.

```  
Number of issues with "unusually long" time:
  Project1: 14
  Project2: 10
  Project3: 29
```

####8. Mean and standard deviation number of labels assigned to each issue

This feature will show us mean and standard deviation of number of labels assigned to each issue. And in this feature, we consider label and issue together, we want to find out the reasonable of the setting of labels. Also, we want to find out whether team members used to add corresponding labels to issues or not.

[Script Link] (https://github.com/SuperCh-SE-NCSU/Project2_badsmell/blob/liang/feature_extractor/featureExtracter2.py)

#####Result
We calculated mean and standard deviation number of labels assigned to each issue.

```  
Mean and standard deviation number of labels assigned to each issue:
  Project1:
          Mean value          1.73015873016
          Standard deviation  0.717277684298
  Project2:
          Mean value          1.42647058824
          Standard deviation  0.648894455086
  Project3:
          Mean value          1.62222222222
          Standard deviation  0.569166598883
```

####9. Number of times each milestone was used

We are interesting in number of milestones. And each milestone usually represents one stage in development cycle. We can analyse which software development method each team used.

[Script Link] (https://github.com/SuperCh-SE-NCSU/Project2_badsmell/blob/liang/feature_extractor/featureExtracter1.py)

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

[Script Link] (https://github.com/SuperCh-SE-NCSU/Project2_badsmell/blob/liang/feature_extractor/featureExtracter1.py)

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

[Script Link] (https://github.com/SuperCh-SE-NCSU/Project2_badsmell/blob/liang/feature_extractor/featureExtracter2.py)

#####Result
We calculated percentage of issues using milestones.

```  
Percentage of issues using milestones:
  Project1: 86.1% in 67 issues
  Project2: 79.9% in 80 issues
  Project3: 52.1% in 93 issues
```

####12. Percentage of issues using assignees

We are interested in how many issues used assignees. And if the percentage of issues using assignees is high, which means responsibility distribution is clear.

[Script Link] (https://github.com/SuperCh-SE-NCSU/Project2_badsmell/blob/liang/feature_extractor/featureExtracter2.py)

#####Result
We also calculated percentage of issues using assignees.

```  
Percentage of issues using milestones:
  Project1: 19.7% in 67 issues
  Project2: 70.1% in 80 issues
  Project3: 72.2% in 93 issues
```

####13. "Unusually small or large" number of commits made by one person

We define number of commits made by one person less than certain percentage of total commits indicates this person is a "passenger". And the number of commits made by one person more than certain percentage of total commits indicates this person is a "great dictator".The result can also indicate whether responsibility distribution of this team is uneven or not.

[Script Link] (https://github.com/SuperCh-SE-NCSU/Project2_badsmell/blob/liang/feature_extractor/featureExtracter2.py)

#####Result
We count the number of commits each user made, and calaulate the percentage.

```  
Unusually small or large" number of issues handled only by one person:
 Project1: 
          user 1: 193	42.4%
          user 2: 180	39.5%
          user 3: 82	18.1%
  Project2:
          user 1: 48	33.3%
          user 2: 48	33.3%
          user 3: 26	18.1%
          user 4: 22	15.3%
  Project3:
          user 1: 151	39.9%
          user 2: 127	33.6%
          user 3: 62	16.4%
          user 4: 38	10.1%
```

####14. Issue participating times of each user

This feature calculates each user's frequency of attendency.

[Script Link] (https://github.com/SuperCh-SE-NCSU/Project2_badsmell/blob/liang/feature_extractor/featureExtracter2.py)

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

###1. Issue Time Duration Detector
During the development cycle, team members will post some issues in order to communicate other members. However, the time duration between two issue creation may vary dramatically. This detector can analyse time duration to decide whether it is too long or too short. The result can reflect the process of each team. And we named it [issueTimeDurationDetector.](https://github.com/SuperCh-SE-NCSU/Project2_badsmell/blob/zhewei/bad_smell_detector/issueTimeDurationDetector.py) Below are pseudocode of algorithm we use to detect bad smells.
```
if issueTimeDuration > mean + 2*std_dev:
    Badsmell: Too long time duration of this issuet.

if issueTimeDuration < mean - 2*std_dev:
    Badsmell: Too little time duration of this issue.

Otherwise:
    This issue duration time is normal.
```

####Result
Because the result are too long, we eliminate some normal results and leave some bad smells.

Project 1
```
('Time duration:', [2328305.0, 1012209.0, 2087830.0, 82098.0, 2072034.0, 3018518.0, 2007166.0, 5370.0, 1555.0, 795809.0, 794524.0, 878029.0, 1997961.0, 1997849.0, 190791.0, 1997189.0, 1995992.0, 1995942.0, 874651.0, 520847.0, 438020.0, 2937.0, 410599.0, 244774.0, 167932.0, 69812.0, 65762.0, 274090.0, 1313615.0, 1307063.0, 46371.0, 1285860.0, 1224321.0, 1806161.0, 1709259.0, 1655536.0, 794363.0, 454158.0, 1092175.0, 1037100.0, 836874.0, 835102.0, 965432.0, 661319.0, 117642.0, 237020.0, 236807.0, 21101.0, 266086.0, 266015.0, 394622.0, 440278.0, 104484.0, 371162.0, 268173.0, 171637.0, 178076.0, 166252.0, 5722.0, 122784.0, 103773.0, 95909.0, 95869.0])
('mean:', 778043.11111111112)
('std_dev:', 756411.46628143825)
----------------------------------------------
0. Badsmell: Too long time duration of this issue.
1. This issue duration time is normal.
2. This issue duration time is normal.
3. This issue duration time is normal.
4. This issue duration time is normal.
5. Badsmell: Too long time duration of this issue.
6. This issue duration time is normal.
7. This issue duration time is normal.
8. This issue duration time is normal.
...
58. This issue duration time is normal.
59. This issue duration time is normal.
60. This issue duration time is normal.
61. This issue duration time is normal.
62. This issue duration time is normal.
```
Project 2
```
('Time duration:', [452566.0, 2117.0, 118312.0, 692389.0, 1443489.0, 1340439.0, 1339892.0, 4900.0, 330655.0, 1240.0, 261292.0, 3998953.0, 3811513.0, 195055.0, 947929.0, 220160.0, 847199.0, 57.0, 727599.0, 260.0, 656970.0, 609779.0, 3375203.0, 572373.0, 563915.0, 3365954.0, 2665954.0, 1289566.0, 235200.0, 44567.0, 300288.0, 12363.0, 148989.0, 148929.0, 148878.0, 148871.0, 148785.0, 178366.0, 141561.0, 169665.0, 42856.0, 106163.0, 94340.0, 176315.0, 67353.0, 97188.0, 852.0, 14143.0, 67240.0, 1008703.0, 65783.0, 65545.0, 62044.0, 61913.0, 65097.0, 63912.0, 63092.0, 1005495.0, 59255.0, 59512.0, 58368.0, 1000300.0, 5297.0, 3737.0, 22948.0, 965320.0, 442454.0, 2229.0])
('mean:', 550141.8529411765)
('std_dev:', 909676.13128271012)
----------------------------------------------
0. This issue duration time is normal.
1. This issue duration time is normal.
2. This issue duration time is normal.
3. This issue duration time is normal.
4. This issue duration time is normal.
5. This issue duration time is normal.
6. This issue duration time is normal.
7. This issue duration time is normal.
8. This issue duration time is normal.
9. This issue duration time is normal.
10. This issue duration time is normal.
11. Badsmell: Too long time duration of this issue.
12. Badsmell: Too long time duration of this issue.
13. This issue duration time is normal.
14. This issue duration time is normal.
15. This issue duration time is normal.
16. This issue duration time is normal.
17. This issue duration time is normal.
18. This issue duration time is normal.
19. This issue duration time is normal.
20. This issue duration time is normal.
21. This issue duration time is normal.
22. Badsmell: Too long time duration of this issue.
23. This issue duration time is normal.
24. This issue duration time is normal.
25. Badsmell: Too long time duration of this issue.
26. Badsmell: Too long time duration of this issue.
27. This issue duration time is normal.
28. This issue duration time is normal.
29. This issue duration time is normal.
30. This issue duration time is normal.
31. This issue duration time is normal.
32. This issue duration time is normal.
...
65. This issue duration time is normal.
66. This issue duration time is normal.
67. This issue duration time is normal.
```
Project 3
```
('Time duration:', [8903.0, 190701.0, 848449.0, 130018.0, 779742.0, 1332352.0, 654797.0, 779672.0, 697731.0, 364093.0, 83564.0, 613278.0, 2701.0, 57152.0, 57295.0, 238986.0, 2675.0, 40356.0, 391407.0, 720239.0, 948927.0, 1040294.0, 678806.0, 5705.0, 816090.0, 760622.0, 31395.0, 269668.0, 1719740.0, 351366.0, 2530579.0, 353674.0, 1063466.0, 1181458.0, 1375119.0, 1022531.0, 68778.0, 1099563.0, 761104.0, 132.0, 75056.0, 654885.0, 177690.0, 75.0, 1125976.0, 368300.0, 139766.0, 300924.0, 689812.0, 209757.0, 382835.0, 26790.0, 7327.0, 148024.0, 344144.0, 344055.0, 1431.0, 341477.0, 364028.0, 240208.0, 174089.0, 68333.0, 489217.0, 3372.0, 71.0, 48271.0, 101548.0, 12527.0, 2434.0, 19107.0, 15092.0, 99584.0, 23678.0, 532484.0, 1506.0, 1075.0, 54660.0, 166414.0, 34153.0, 7514.0, 10.0, 160.0, 45.0, 15383.0, 151888.0, 23021.0, 34897.0, 35024.0, 8572.0, 24400.0])
('mean:', 357380.18888888886)
('std_dev:', 458485.98025573732)
----------------------------------------------
0. This issue duration time is normal.
1. This issue duration time is normal.
2. This issue duration time is normal.
3. This issue duration time is normal.
4. This issue duration time is normal.
5. Badsmell: Too long time duration of this issue.
6. This issue duration time is normal.
7. This issue duration time is normal.
8. This issue duration time is normal.
...
24. This issue duration time is normal.
25. This issue duration time is normal.
26. This issue duration time is normal.
27. This issue duration time is normal.
28. Badsmell: Too long time duration of this issue.
29. This issue duration time is normal.
30. Badsmell: Too long time duration of this issue.
31. This issue duration time is normal.
32. This issue duration time is normal.
33. This issue duration time is normal.
34. Badsmell: Too long time duration of this issue.
35. This issue duration time is normal.
36. This issue duration time is normal.
37. This issue duration time is normal.
...
86. This issue duration time is normal.
87. This issue duration time is normal.
88. This issue duration time is normal.
89. This issue duration time is normal.
```

###2. Issue Without Comment Detector
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

###3. Label Usage Detector
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

###4. User Participate Detector
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

###5. Weekly Issue Detector
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

###6. Issue Assignee Detector
According to the ```Issue Without Comment Detector```, we found that there are many issues without having comments below. So if issue creator assigned the issue to himself/herself or other team members, we think this situation will be better. Since assignee means who this issue is assigned to, and he/she have to handle it. If one team member is assigned to too many or too few issues, another bad smell will occur. We named it [issueAssigneeDetector.](https://github.com/SuperCh-SE-NCSU/Project2_badsmell/blob/57672e3292594dc22788de81a6f06d887bbca0fb/bad_smell_detector/issueAssigneeDetector.py) Below are pseudocode of algorithm we use to detect bad smells.
```
if userName == 'None': 
	These are issues not assigned to any team member.
if userName != 'None' and eachUserAssignTimes > 1.5*assignTotalTimes/userNum:
 	Badsmell: This user assigned too many times.
if userName != 'None' and eachUserAssignTimes < 0.5*assignTotalTimes/userNum:
 	Badsmell: This user assigned too few times.
otherwise:
 	The assigned times of this user is normal.
``` 	
 	
####Result

Project 1
```
('assignTotalTimes:', 63)
Badsmell: user1 assigned too few times.
Badsmell: user2 assigned too few times.
Badsmell: user3 assigned too few times.
```
Project 2
```
('assignTotalTimes:', 68)
Badsmell: user1 assigned too few times.
The assigned times of user2 is normal.
The assigned times of user3 is normal.
The assigned times of user4 is normal.
```
Project 3
```
('assignTotalTimes:', 90)
Badsmell: user1 assigned too few times.
The assigned times of user2 is normal.
The assigned times of user3 is normal.
Badsmell: user4 assigned too few times.
```

##Early Warning

**Issue Interval Early Warning**

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
[Code Link] (https://github.com/SuperCh-SE-NCSU/Project2_badsmell/blob/liang/earlywarning/earlyWarningExtractorInterval.py)

**Issue Duration Early Warning**
Issue Duration early Warning is based on the trend of duration of issue. If the team spend much more time in closing the issue than before, the team may be struggling or waiting. TIt means we should notify the team to work harder. There are two methods to implement it. The first detecting method is also based on threshold, the second detecting method is based on the increasing trend of issue duration time in which we need linear regression to fit the trend. We implement the issue duration early warning in the code below:
```python
#method 1: based on threshold
sumtime=0
timethreshold=60*60*24*12
print('method 1')
for i in range(0,len(xa)-1,1):
    if ya[i]>2000000:
        sumtime=sumtime+ya[i]
    else:
        sumtime=0
    if sumtime>timethreshold:
        print('The team may be struggling at this moment, issue: '+str(i))
        sumtime=0
print('-------------------------------')

#method 2: based on the fit linear equation 
print('method 2')
km=list()
for i in range(8,len(xa)-1,1):
    tempx=xa[(i-8):i]
    tempy=ya[(i-8):i]
    m,b = polyfit(tempx, tempy, 1)
    fit=polyfit(tempx,tempy,1)
    fit_fn=poly1d(fit)
    if m>150000:
        print('The team may be waiting at this moment, issue: '+str(i))
    km.append(m)

```
[Code Link] (https://github.com/SuperCh-SE-NCSU/Project2_badsmell/blob/liang/earlywarning/earlyWarningExtractorDuration.py)

##Early Warning Results

**Issue Interval Early Warning Results**

For project 1, the interval of created time of two adjacent issue is described in the following graph.
![Project1](https://github.com/SuperCh-SE-NCSU/Project2_badsmell/blob/liang/earlywarning/project1_interval.png)

The early warning detecting result is as following:
```
the team may be falling behind the schedule before issue 37
```
For project 2, the interval of created time of two adjacent issue is described in the following graph.
![Project2](https://github.com/SuperCh-SE-NCSU/Project2_badsmell/blob/liang/earlywarning/project2_interval.png)

The early warning detecting result is as following:
```
the team may be pushing before issue 10
the team may be falling behind the schedule before issue 26
the team may be falling behind the schedule before issue 28
the team may be pushing before issue 35
the team may be pushing before issue 40
the team may be pushing before issue 49
the team may be pushing before issue 54
the team may be pushing before issue 59
the team may be pushing before issue 64
```
For project 3, the interval of created time of two adjacent issue is described in the following graph.
![Project3](https://github.com/SuperCh-SE-NCSU/Project2_badsmell/blob/liang/earlywarning/project3_interval.png)

The early warning detecting result is as following:
```
the team may be falling behind the schedule before issue 10
the team may be falling behind the schedule before issue 37
the team may be falling behind the schedule before issue 52
the team may be pushing before issue 58
the team may be pushing before issue 71
```

**Issue Duration Early Warning Results**

For project1, the duration of issues is shown in the following graph.
![Project1](https://github.com/SuperCh-SE-NCSU/Project2_badsmell/blob/liang/earlywarning/project1_duration.png)

The early warning detecting result is as following:
```
method 1
The team may be struggling at this moment, issue: 0
The team may be struggling at this moment, issue: 2
The team may be struggling at this moment, issue: 4
The team may be struggling at this moment, issue: 5
The team may be struggling at this moment, issue: 6
-------------------------------
method 2
The team may be waiting at this moment, issue: 15
The team may be waiting at this moment, issue: 16
The team may be waiting at this moment, issue: 33
The team may be waiting at this moment, issue: 34
The team may be waiting at this moment, issue: 35
```

For project2, the duration of issues is shown in the following graph.
![Project2](https://github.com/SuperCh-SE-NCSU/Project2_badsmell/blob/liang/earlywarning/project2_duration.png)

The early warning detecting result is as following:

```
method 1
The team may be struggling at this moment, issue: 11
The team may be struggling at this moment, issue: 12
The team may be struggling at this moment, issue: 22
The team may be struggling at this moment, issue: 25
The team may be struggling at this moment, issue: 26
-------------------------------
method 2
The team may be waiting at this moment, issue: 13
The team may be waiting at this moment, issue: 14
The team may be waiting at this moment, issue: 15
The team may be waiting at this moment, issue: 23
The team may be waiting at this moment, issue: 26
The team may be waiting at this moment, issue: 27
```

For project3, the duration of issues is shown in the following graph.
![Project2](https://github.com/SuperCh-SE-NCSU/Project2_badsmell/blob/liang/earlywarning/project2_duration.png)

The early warning detecting result is as following:
```
method 1
The team may be struggling at this moment, issue: 30
-------------------------------
method 2
The team may be waiting at this moment, issue: 22
The team may be waiting at this moment, issue: 31
```

Actually we found that method 1 and method 2 gives similar result in project 2 and 3. But method 2 works better in project 1. It means that linear regression is good at describing the trend. There is also an interesting trend here, the issue duration time is small near the deadline of the projects. Maybe all the teams are creating new issues to meet the requirements of our professor.

