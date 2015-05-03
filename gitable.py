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

def showFigure(x):
    plt.plot(range(len(x)), x, 'ro-')   
    plt.show()

class L():
    "Anonymous container"
    def __init__(i,**fields) :
        i.override(fields)
    def override(i,d): i.__dict__.update(d); return i
    def __repr__(i):
        d = i.__dict__
        name = i.__class__.__name__
        return name+'{'+' '.join([':%s %s' % (k,pretty(d[k])) for k in i.show()])+ '}'
    def show(i):
        lst = [str(k)+" : "+str(v) for k,v in i.__dict__.iteritems() if v != None]
        return ',\t'.join(map(str,lst))
 
def secs(d0):
    d = datetime.datetime(*map(int, re.split('[^\d]', d0)[:-1]))
    epoch = datetime.datetime.utcfromtimestamp(0)
    delta = d - epoch
    return delta.total_seconds()

def dump1(u,issues):
    token = "8174633dcc5c8379a557af139c8589ec63b37327" 
    request = urllib2.Request(u, headers={"Authorization" : "token "+token})
    v = urllib2.urlopen(request).read()
    w = json.loads(v)
    if not w: return False
    for event in w:
        #print(type(event))
        issue_id = event['issue']['number']
        #label_name=None
        if not event.get('label'):
            continue
            
        #continue
        #   
        #else:
        #    label_name='null'
        created_at = secs(event['created_at'])
        action = event['event']
        label_name=event['label']['name']
        user = event['actor']['login']
        milestone = event['issue']['milestone']
        assignea=event['issue']['assignee']
        comments=event['issue']['comments']
        issuecreated_at=secs(event['issue']['created_at'])
        issueclosed_at=secs(event['issue']['closed_at'])
        duration=issueclosed_at-issuecreated_at
        assignee=None
        
        if assignea!=None: assignee=assignea['login']
        if milestone != None : milestone = milestone['title']
        eventObj = L(when=created_at,
                    action = action,
                    what = label_name,
                    user = user,
                    milestone = milestone,
                    assignee=assignee,
                    comments=comments,
                    issuecreated_at=issuecreated_at,
                    issueclosed_at=issueclosed_at,
                    duration=duration)
        all_events = issues.get(issue_id)
        if not all_events: all_events = []
        all_events.append(eventObj)
        issues[issue_id] = all_events
    return True
 
def dump(u,issues):
    try:
        return dump1(u, issues)
    except Exception as e:
        print(e)
        print("Contact TA")
    return False
 
def launchDump():
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

    
    f=open("Group6.txt","w")
    
 
    #issues2=dict()
    while(True):
        doNext = dump('https://api.github.com/repos/SuperCh-SE-NCSU/ProjectScraping/issues/events?page=' + str(page), issues)
        #doNext=dump('https://api.github.com/repos/CSC510/SQLvsNOSQL/issues/events?page=' + str(page),issues)
        #doNext=dump('https://api.github.com/repos/CSC510-2015-Axitron/maze/issues/events?page=' + str(page), issues)
        print("page" + str(page))
        page += 1
        if not doNext : break
    #print issues
    #with open('ProjectScraping.json','wb') as fp:
    #    json.dump(issues,fp,skipkeys=False, ensure_ascii=False)
    #rint json.dumps(issues)
    #with open('ProjectScraping.json','wb') as fp:
    #    json.dump(issues,fp)
    
    #with open('project1.json', 'w') as outfile:
    #      json.dump(issues, outfile)
    for issue, events in issues.iteritems():
        print("ISSUE " + str(issue)+"\n")
        f.write("ISSUE "+str(issue)+"\n")
        milestonetrue=True
        commentsi=True
        createat=True
        labelt=True
        assigneet=True
        tduration=True
        numofIssues=issue
        for event in events:
            for k,v in event.__dict__.iteritems():
                if str(k) is 'what':
                    if str(v) in labelnum.keys():
                        labelnum[str(v)]=labelnum[str(v)]+1
                    else:
                        labelnum[str(v)]=1
                    labelt=False
                if str(k) is 'assignee':
                    if assigneet==True:
                        if str(v) in assignques.keys():
                            assignques[str(v)]=assignques[str(v)]+1
                        else:
                            assignques[str(v)]=1
                        assigneet=False
                    
                if str(k) is 'milestone':
                    if str(v) in milestonenum.keys():
                        if milestonetrue==True:
                            milestonenum[str(v)]=milestonenum[str(v)]+1
                            milestonetrue=False
                    else:
                        milestonenum[str(v)]=1
                if str(k) is 'comments':
                    if commentsi==True:
                        if v==0:
                            numofiss_nocomments=numofiss_nocomments+1
                        commentsi=False
                if str(k) is 'issuecreated_at':
                    if createat==True:
                        createtime[issue]=v
                        createat=False
                if str(k) is 'duration':
                    if tduration==True:
                        timeduration.append(v)
                #if v != None:
                #    print(str(k)+" : "+str(v)) 
            #print(type(event))
            #print(event['issue']['number'])
            #if event.get('label'):
            #    print(event['label']['name'])
            f.write(event.show()+"\n")
            f.write('\n')
            print(event.show())
            print('')
        if labelt==True:
            numofissuenotlabeled=numofissuenotlabeled+1
        if createat==True:
            createtime[issue]=0
        
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

    f.close()
        #issues2[str(issue)]=events
    #with open('ProjectScraping.json','wb') as fp:
    #    json.dump(issues2,fp)

    #badsmell
    #badsmell 1: the distribution of number of issues distributed each week is not well
    plt.figure()
    
    n_groups=len(numberofissueWeek)
    meansone=range(1,n_groups,1)
    weekcount=numberofissueWeek

    fig,ax=plt.subplots()
    index = np.arange(n_groups)  
    bar_width = 0.35  
 
    opacity = 0.4  
    rects1 = plt.bar(index+bar_width, weekcount, bar_width,alpha=opacity, color='b',label=    'Number of issues')  
    #rects2 = fbadsmell1.bar(index + bar_width, means_women, bar_width,alpha=opacity,col    or='r',label='Women')  
 
    plt.xlabel('Week')  
    plt.ylabel('Number of Issues')  
    plt.title('Number of Issues Every Week')  
    #fbadsmell1.xticks(index + bar_width, ('A', 'B', 'C', 'D', 'E'))  
    #fbadsmell1.ylim(0,40)  
    plt.legend()  
       
 
    plt.show()

    #early warning
    fearly=plt.figure()
    plt.plot(createtime.keys(),createtime.values(),'ro-')
    plt.show()
launchDump() 
