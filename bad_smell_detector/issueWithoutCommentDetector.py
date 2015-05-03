def issueWithoutCommentDetector():
	#issueWithoutComment = 5
	issueWithoutComment = 41
	#issueWithoutComment = 6
	#totalNumOfComment = 69
	totalNumOfComment = 93
	#totalNumOfComment = 93
	
	if issueWithoutComment*1.0/totalNumOfComment > 0.2:
		print('Badsmell: Too many issues without comments.')
	else:
		print('Normal')
	
issueWithoutCommentDetector()
