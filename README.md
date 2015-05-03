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

##Early warning results
