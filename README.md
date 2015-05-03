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
We extracted all the issues from the three projects by running code from the given file gitable.py.
Then we extracted 16 features that we defined from the issues for these three projects.
