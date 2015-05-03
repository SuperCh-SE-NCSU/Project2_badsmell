import numpy as np

def labelUsageDetector():
    #labelUsage=list()
    #labelUsage = gt.getLabelUsage()
    #print(labelUsage)
    #labelUsage=[15,5,1,36,3,21,15,5,14,5]
    #labelUsage=[23,33,3,29,1,6,12]
    labelUsage=[27,42,58,12,1,1,22,4,3,1,51,33,1,40,8,2,3,1,11,5,1]
         
    mean = np.mean(labelUsage)
    std_dev = np.std(labelUsage)
    print('mean:', mean)
    print('std_dev:', std_dev)
    for i in range(len(labelUsage)):
        if labelUsage[i] < mean-std_dev:
            print('Badsmell: This label was used too little times.')
        else:
            print('The usage of this label is normal.')



labelUsageDetector()
