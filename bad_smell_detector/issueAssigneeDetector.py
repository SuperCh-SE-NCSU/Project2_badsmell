import numpy as np

def issueAssigneeDetector():
	
	userNum=3
	userName=['user1','user2','user3','None']
	eachUserAssignTimes=[9, 3, 0, 51]
	
	#userNum=4
	#userName=['user1','user2','user3','user4','None']
	#eachUserAssignTimes=[8, 11, 11, 11, 27]
	
	#userNum=4
	#userName=['user1','user2','user3','user4','None']
	#eachUserAssignTimes=[11, 19, 26, 9, 25]

 	
 	assignTotalTimes=0
 	for i in range(len(eachUserAssignTimes)):
 		assignTotalTimes += eachUserAssignTimes[i]

 	print('assignTotalTimes:', assignTotalTimes)

 	for i in range(len(eachUserAssignTimes)):
 		if userName[i] == 'None': return userName[i]
 		if userName[i] != 'None' and eachUserAssignTimes[i] > (1.0/userNum)*assignTotalTimes*1.5:
 			print('Badsmell: '+userName[i]+' assigned too many times.')
 		elif userName[i] != 'None' and eachUserAssignTimes[i] < (1.0/userNum)*assignTotalTimes*0.5:
 			print('Badsmell: '+userName[i]+' assigned too few times.')
 		else:
 			print('The assigned times of '+userName[i]+' is normal.')

issueAssigneeDetector()
