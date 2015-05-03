def issueWithoutCommentDetector():
	#issueWithoutComment = 5
	#issueWithoutComment = 41
	issueWithoutComment = 6
	#totalNumOfIssues = 67
	#totalNumOfIssues = 80
	totalNumOfIssues = 93
	print('issueWithoutComment', issueWithoutComment)
	print('totalNumOfIssues', totalNumOfIssues)
	if issueWithoutComment*1.0/totalNumOfIssues > 0.2:
		print('Badsmell: Too many issues without comments.')
	else:
		print('Normal')
	
issueWithoutCommentDetector()
