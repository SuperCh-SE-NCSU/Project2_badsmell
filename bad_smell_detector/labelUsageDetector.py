import numpy as np

def labelUsageDetector():
    #labelUsage=list()
    #labelUsage = gt.getLabelUsage()
    #print(labelUsage)
    #labelUsage=[15,5,1,36,3,21,15,5,14,5]
    #labelName=['develop','question','invalid','Solved','duplicate','design','help' 'wanted','test','bug','enhancement']
    #labelUsage=[23,33,3,29,1,6,12]
    #labelName=['Test Problem','info!','Configure Problem','help wanted','wontfix','bug', 'Design Problem']
    labelUsage=[27,42,58,12,1,1,22,4,3,1,51,33,1,40,8,2,3,1,11,5,1]
    labelName=['feature dev','4. feature complete','2a. feature dev','5. bug','wontfix','2b. help wanted','feature QA','testing','question','backtrack.JS','1. feature request','feature request','trailModel.JS','3. feature QA','help wanted','branch','deployment','branch list','feature complete','bug','resources']
    print('labelName', labelName)
    print('labelUsage', labelUsage)
    mean = np.mean(labelUsage)
    std_dev = np.std(labelUsage)
    print('mean:', mean)
    print('std_dev:', std_dev)
    for i in range(len(labelUsage)):
        if labelUsage[i] < mean-std_dev:
            print('Badsmell: ['+labelName[i]+'] was used too little times.')
        else:
            print('The usage of ['+labelName[i]+'] is normal.')



labelUsageDetector()
