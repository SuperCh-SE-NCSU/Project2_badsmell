# Project2_badsmell
Bad smells 

##Collection
We selected three projects (our project is one of them), and extracted all the issues from these projects. <br/>
1. Projects with more issues are preferred.<br/>
2. Projects with more labels are proferred.
Then the gitable.py file is used to extract the issues and labels for each project.
##Anonymization
We labelled these three projects as Project1, Project2, Project3. And there is no clue telling about the the content of these projects in the features we extracted.<br/>
So it is hard to tell what these projects are about.
##Tables
Data extracted from issues are stored in a CSV file.
Then the Statistical measures like the min, max, accumulation, mean and standard deviation of the data set were extracted, which are the features that we want. All the features are represented by numbers, then Some values are set to detect bad smells based on the comparison of the results and these values.
##Data
We extracted all the issues from the three projects by running code from the given file gitable.py.
Then we extracted 16 features that we defined from the issues for these three projects.
### Features:

The values in the table represent the number of rows of data collected for that particular feature.

|Number|Feature|Project1|Project2|Project3|
|------|-------|--------|--------|--------|
|1|Total number of issues|121|510|182|
|2|Number of issues without comments|117|483|168|
|3|Number of issues each week|201|120|107|
|4|Time interval between the creation of two issues|35|56|64|
|5|Total number of labels|38|67|80|
|6|Number of times each label was used|60|68|93|
|7|Mean and standard deviation of times spent in each label|60|68|93|
|8|"Unusually long" time a label|38|67|80|
|9|Mean and standard deviation number of labels assigned to each issue|396|427|433|
|10|Total number of milestones|5|5|5|
|11|Percentage of issues using labels|38|67|80|
|12|Percentage of issues using milestones|38|67|80|
|13|Percentage of issues using assignees|38|67|80|
|14|"Unusually small" number of issues handled by one person(<10%)|38|67|80|
|15|"Unusually large" number of commits handle by one person(>70%)|38|67|80|
|16|Issue participating times of each user|38|67|80|

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

**4. Time interval between the creation of two issues**

**5. Total number of labels**

**6. Number of times each label was used**

**7. Mean and standard deviation of times spent in each label**

**8. "Unusually long" time a label**

**9. Mean and standard deviation number of labels assigned to each issue**

**10. Total number of milestones**

**11. Percentage of issues using labels**

**12. Percentage of issues using milestones**

**13. Percentage of issues using assignees**

**14. "Unusually small" number of issues handled by one person(<10%)**

**15. "Unusually large" number of commits handle by one person(>70%)**

**16. Issue participating times of each user**


##Feature detection & Results

**1. Total number of issues**

This feature is quite straightforward. We decide to find the total number of issues of each team. And this feature can reflect briefly how team members communicate during the development period.

Result

**2. Number of issues without comments**

We also want to know how many issues are actually no comments below. This feature goes deeper comparing to the first feature. And according to this feature, we can find out which issue actually makes the difference.

Result

**3. Number of issues each week**

This issue is quite interesting.  We want to find out that which period is most likely to create issues, beginning or near the deadline. And we can analyse the results, which will help to optimize the development schedule.

Result

**4. Time interval between the creation of two issues**

"Time interval between two issues" is also related to last feature. And it is quite possible that the creation of issues is uneven. We can analyse and find out turn points during which the frequency of creating issues changes dramatically.

Result

**5. Total number of labels**

We want to know the total number of labels each team created. Different number of labels reflect different kinds of situations and different levels of priorities each team will set.

Result

**6. Number of times each label was used**

We can figure out which kind of label was used a lot of times, and which kind of label was seldom used. And the results will reflect whether the quantity and the setting of labels are reasonable or not.

Result

**7. Mean and standard deviation of times spent in each label**

This feature will show us mean and standard deviation of times spending in each label. And it will help us to analyse in depth. 
Result

**8. "Unusually long" time a label**

"Unusually long" time means 1.5 or 2 standard deviations time in a label. In normal distribution, 1.5 or 2 standard deviations means the data point is quite far away from the mean value. In this case, unusually long time a label may indicate team do little stuff during this time period.

Result

**9. Mean and standard deviation number of labels assigned to each issue**<br/>
This feature will show us mean and standard deviation of number of labels assigned to each issue. And in this feature, we consider label and issue together, we want to find out the reasonable of the setting of labels. Also, we want to find out whether team members used to add corresponding labels to issues or not.

Result

**10. Total number of milestones**<br/>

Result

**11. Percentage of issues using labels**<br/>

Result

**12. Percentage of issues using milestones**<br/>

Result

**13. Percentage of issues using assignees**<br/>

Result

**14. "Unusually small" number of issues handled by one person(<10%)**<br/>

Result

**15. "Unusually large" number of commits handle by one person(>70%)**<br/>

Result

**16. Issue participating times of each user**<br/>

Result

##Bad smells detector
##Bad smells results
##Early warning
##Early warning results

