def issueParticipateDetector():
	#eachMemberParticipateTimes=[56,54,7]
	eachMemberParticipateTimes=[78,20,4,1]
	#eachMemberParticipateTimes=[187,101,29,6]
	#eachMemberCommitTimes=[193,180,82]
	eachMemberCommitTimes=[48,48,26,22]
	#eachMemberCommitTimes=[151,127,62,38]
	
	sumOfParticipateTimes = 0
	sumOfCommitTimes = 0
	for i in range(len(eachMemberParticipateTimes)):
		sumOfParticipateTimes += eachMemberParticipateTimes[i]
		sumOfCommitTimes += eachMemberCommitTimes[i]
	print('sumOfParticipateTimes',sumOfParticipateTimes)
	print('sumOfCommitTimes',sumOfCommitTimes)
	
	for i in range(len(eachMemberParticipateTimes)):
		ratio1=eachMemberParticipateTimes[i]*1.0/sumOfParticipateTimes
		ratio2=eachMemberCommitTimes[i]*1.0/sumOfCommitTimes
		if ratio1 < 0.1 or ratio2 < 0.1:
			print("Badsmell: This user is likely be a 'passenger'.")
		elif ratio1 > 0.75 or ratio2 > 0.75:
			print("Badsmell: This user is likely be a 'great dictator'.")
		else:
			print("This user is normal.")
	
issueParticipateDetector()
