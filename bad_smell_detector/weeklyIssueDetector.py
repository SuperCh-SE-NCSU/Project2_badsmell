import numpy as np

def weeklyIssueDetector():
    #weeklyIssue=list()
    #weeklyIssue = gt.getIssueNumPerWeek()
    #print(weeklyIssue)
    #weeklyIssue=[24, 9, 4, 2, 5, 6, 5, 8]
    #weeklyIssue=[10, 12, 4, 1, 1, 1, 1, 37, 1]
    weeklyIssue=[21, 8, 9, 2, 9, 10, 26, 5]
    mean = np.mean(weeklyIssue)
    std_dev = np.std(weeklyIssue)
    print('weeklyIssue:',weeklyIssue)
    print('mean:', mean)
    print('std_dev:', std_dev)
    for i in range(len(weeklyIssue)):
        if weeklyIssue[i] > mean+std_dev:
            print('Badsmell: Too many issues in this week.')

        elif weeklyIssue[i] < mean-std_dev:
            print('Badsmell: Too little issues in this week.')
        else:
            print('Issue number is normal in this week.')



weeklyIssueDetector()
