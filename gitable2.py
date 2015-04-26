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
import urllib2
import json
import re,datetime
import math
import sys
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
    token = "ca1cd448933062af92b7f3de85089a3ba546372e" # <===
    request = urllib2.Request(u, headers={"Authorization" : "token "+token})
    v = urllib2.urlopen(request).read()
    w = json.loads(v)
    if not w: return False
    for event in w:
        issue_id = event['issue']['number']
        if not event.get('label'): continue
        created_at = secs(event['created_at'])
        action = event['event']
        label_name = event['label']['name']
        user = event['actor']['login']
        milestone = event['issue']['milestone']
        if milestone != None : milestone = milestone['title']
        eventObj = L(when=created_at,
                    action = action,
                    what = label_name,
                    user = user,
                    milestone = milestone)
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
    milestonenum=dict()
    #feature17: store number of issues each person participating in
    userParticipateInIssue=dict()
    #feature13,14: store number of issues handled by each person
    userHandleWholeIssue=dict()
    userList=[]
    #judge issue is handled by same user
    sameUser=False
    #feature15,16: time interval between two issues' creation
    timeInterval=[]
    issueStartTime=[]

    f=open("Group6.txt","w")
    #issues2=dict()
    while(True):
        doNext = dump('https://api.github.com/repos/SuperCh-SE-NCSU/ProjectScraping/issues/events?page=' + str(page), issues)
        #print("page" + str(page))
        page += 1
        if not doNext : break
    #outer loop iterator
    iterator2=-1
    for issue, events in issues.iteritems():
        iterator2+=1
        print("ISSUE " + str(issue)+"\n")
        f.write("ISSUE "+str(issue)+"\n")
        milestonetrue=True
        numofIssues=issue
        #calculate the iteration times, inner loop
        iterator=-1;
        tempUser=''
        for event in events:
            iterator+=1
            for k,v in event.__dict__.iteritems():
                if str(k) is 'what':
                    if str(v) in labelnum.keys():
                        labelnum[str(v)]=labelnum[str(v)]+1
                    else:
                        labelnum[str(v)]=1
                #feature 17
                if str(k) is 'user':
                    if str(v) in userList:
                        userParticipateInIssue[str(v)]+=1
                    else:
                        userList.append(str(v))
                        userParticipateInIssue[str(v)]=0
                        userHandleWholeIssue[str(v)]=0

                #feature 13, 14
                if str(k) is 'user':
                    if tempUser=='':
                        tempUser=str(v)
                        sameUser=True
                    elif tempUser==str(v):
                        sameUser=True
                    else:
                        sameUser=False
                    if len(events)==1: userHandleWholeIssue[str(v)]+=1
                    if iterator==len(events)-1 and sameUser==True and len(events)>1: userHandleWholeIssue[str(v)]+=1
                #feature 3, 10
                if str(k) is 'milestone':
                    if str(v) in milestonenum.keys():
                        if milestonetrue==True:
                            milestonenum[str(v)]=milestonenum[str(v)]+1
                            milestonetrue=False
                    else:
                        milestonenum[str(v)]=1
                #feature 15, 16
                if str(k) is 'when':
                    if iterator==len(events)-1:
                        issueStartTime.append(float(v))
                        if len(timeInterval) > 0:
                            timeInterval.append(float(v)-float(issueStartTime[-2]))
                        else:
                            timeInterval.append(0.0)

            f.write(event.show()+"\n")
            f.write('\n')
            print(event.show())
            print('')
          
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
    print('feature 13, 14')
    print('"Unusually small" number of issues handled by one person(<10%)')
    print('"Unusually large" number of issues handled by one person(>70%)')
    for key, value in userHandleWholeIssue.items():
        print(key, value, value*1.0/numofIssues)
    print('-----------------------------')
    print('feature 17')
    print('Issue participating times of each user')
    for key, value in userParticipateInIssue.items():
        print(key, value)
    print('-----------------------------')
    print('feature 15, 16')
    print('Time interval between the creation of two issues')
    intervalSum=0
    for interval in timeInterval:
        #print(interval)
        if interval>0: intervalSum += float(interval)
    mean = intervalSum/len(timeInterval)
    stdevSum = 0
    for i in range(len(timeInterval)):
        if timeInterval[i]>0: stdevSum += pow((timeInterval[i]-mean),2)
    stdev=math.sqrt(stdevSum/(len(timeInterval)-1))
    print ('Number of interval: ',len(timeInterval))
    print ('Mean value of interval time', mean)
    print ('Standard deviation of interval time', stdev)
    f.close()
     
    
launchDump() 
