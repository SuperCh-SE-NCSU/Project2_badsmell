# gitabel
# the world's smallest project management tool
# reports relabelling times in github (time in seconds since epoch)
# thanks to dr parnin
# todo:
# - ensure events sorted by time
# - add issue id
# - add person handle
 
"""
You will need to add your authorization token in the code.
Here is how you do it.
1) In terminal run the following command
curl -i -u <your_username> -d '{"scopes": ["repo", "user"], "note": "OpenSciences"}' https://api.github.com/authorizations
2) Enter ur password on prompt. You will get a JSON response.
In that response there will be a key called "token" .
Copy the value for that key and paste it on line marked "token" in the attached source code.
3) Run the python file.
python gitable.py
"""

from __future__ import print_function
import matplotlib.pyplot as plt
import urllib2
import json
import re,datetime
import sys
import math
import numpy as np

def ascii_encode_dict(data):
    ascii_encode = lambda x: x.encode('ascii') if isinstance(x, unicode) else x 
    return dict(map(ascii_encode, pair) for pair in data.items())
def ascii_equal(data,string):
    if unicode(data, 'ascii')  == unicode(string, 'utf-8'):
        return True
    else:
        return False
    
def featureExtracter():
    page = 1
    issues = dict()
    #feature1: Number of issues
    numofIssues=0
    #feature2: Number of different labels
    numoflabels=0
    #Number of times each label was used
    labelnum=dict()
    assignques=dict()
    milestonenum=dict()
    createtime=dict()
    numofiss_nocomments=0
    numberofissueWeek=list()
    timeduration=list()
    
    numofissuenotlabeled=0

    with open('../Data/project1.json') as data_file:    
        issues = json.load(data_file,object_hook=ascii_encode_dict)

 
    keylist=map(int,issues.keys())
    keylist.sort()
    
    for issue in keylist:
        events=issues[str(issue)]
        print("ISSUE " + str(issue)+"\n")
 
        milestonetrue=True
        commentsi=True
        createat=True
        labelt=True
        assigneet=True
        tduration=True
        numofIssues=issue
        for event in events:
            for k,v in event.iteritems():
                if ascii_equal(k,'what'):
                    if v in labelnum.keys():
                        labelnum[v]=labelnum[str(v)]+1
                    else:
                        labelnum[v]=1
                    labelt=False
                if ascii_equal(k,'assignee'):
                    if assigneet==True:
                        if str(v) in assignques.keys():
                            assignques[str(v)]=assignques[str(v)]+1
                        else:
                            assignques[str(v)]=1
                        assigneet=False
                    
                if ascii_equal(k,'milestone'):
                    if str(v) in milestonenum.keys():
                        if milestonetrue==True:
                            milestonenum[str(v)]=milestonenum[str(v)]+1
                            milestonetrue=False
                    else:
                        milestonenum[str(v)]=1
                if ascii_equal(k,'comments'):
                    if commentsi==True:
                        if v==0:
                            numofiss_nocomments=numofiss_nocomments+1
                        commentsi=False
                if ascii_equal(k,'issuecreated_at'):
                    if createat==True:
                        createtime[issue]=v
                        createat=False
                if ascii_equal(k,'duration'):
                    if tduration==True:
                        timeduration.append(v)
        if labelt==True:
            numofissuenotlabeled=numofissuenotlabeled+1
        if createat==True:
            createtime[issue]=0
    print(labelnum)
    numoflabels=len(labelnum)
    print('feature 1')
    print('Num of issues:',numofIssues)
    print('-----------------------------')
    print('featue 2')
    print('Num of labels:',numoflabels)
    print('-----------------------------')
    print('feature 3')
    print('Num of millstones:',len(milestonenum))
    for key, elem in milestonenum.items():
        print(key, elem)
    print('-----------------------------')
    print('feature 4')
    print('Number of times each label was used')
    for key, elem in labelnum.items():
        print(key, elem)
    print('-----------------------------')
    print('feature 5')
    print('Number of issues without comments:',numofiss_nocomments)
    print('-----------------------------')
    
    print('feature 6')
    endtime=0
    #print(len(createtime))
    #print(createtime)
    #plt.plot(createtime.keys(),createtime.values(),'ro-')
        
    #plt.show()
    
    for k,v in createtime.items():
        if endtime==0:
            numofissueweek=0
            endtime=v+60*60*24*7
            #print(endtime)
        if v<endtime:
            numofissueweek=numofissueweek+1
        else:
            numberofissueWeek.append(numofissueweek)
            numofissueweek=1
            endtime=endtime+60*60*24*7
            #print(endtime)
    numberofissueWeek.append(numofissueweek)
    print('Number of issues every week:',numberofissueWeek)
    print('-----------------------------')
    
    print('feature 7')
    print('mean and standard deviation')
    mean=0
    for timed in timeduration:
        mean=mean+timed
    mean=mean/len(timeduration)
    standard=0
    for timed in timeduration:
        standard=standard+(timed-mean)*(timed-mean)
    standard=math.sqrt(standard/len(timeduration))
    print('mean: ',mean)
    print('standard: ',standard)
    print('-----------------------------')

    print('feature 8')
   
    numofdura=0
    for timed in timeduration:
        if math.fabs(timed-mean)>1.5*standard:
            numofdura=numofdura+1
    
    print('Number of issues with unusually long time:',numofdura)
    print('-----------------------------')    
    
    print('feature 9')
    print('issues not labeled:',numofIssues-len(issues))
    print('-----------------------------')
    print('feature 10')
    print('Percentage of issues using milestones')
    sumMile=0
    noneMile=0
    for key, elem in milestonenum.items():
        if key=='None':
            noneMile=elem
        else:
            sumMile=sumMile+elem
    print(sumMile*1.0/(sumMile+noneMile))
    print('-----------------------------')
    print('feature 11')
    print('Percentage of issues using assignees')
    print('participants')
    print(assignques)
    nonassign=float(0)
    sumassign=float(0)
    for tkey, telem in assignques.items():
        if tkey=='None':
            nonassign=telem
        sumassign=sumassign+telem
    print('Percentage of issues using assignees:',1-nonassign/sumassign)

 
 
featureExtracter() 
