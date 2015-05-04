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
import json,csv
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

def csv_writer(data, path):
   with open(path, "wb") as csv_file:
       writer = csv.writer(csv_file, delimiter=',')
       for line in data:
           writer.writerow([line])

def dump1(u,issues):
    token = "" 
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
    username=dict()
    issueinfo=list()
    while(True):
        #doNext = dump('https://api.github.com/repos/SuperCh-SE-NCSU/ProjectScraping/issues/events?page=' + str(page), issues)
        #doNext=dump('https://api.github.com/repos/CSC510/SQLvsNOSQL/issues/events?page=' + str(page),issues)
        doNext=dump('https://api.github.com/repos/CSC510-2015-Axitron/maze/issues/events?page=' + str(page), issues)
        print("page" + str(page))
        page += 1
        if not doNext : break
    
    newissues=dict()
    mapuser=dict()
 
    currentuser=1
    for issue, events in issues.iteritems():
        print("ISSUE " + str(issue)+"\n")
        newevents=list()
        new_eventdict=dict()
        new_eventdict['issue_id']=issue
        for event in events:
            eventdict=event.__dict__
            if eventdict['user'] in mapuser.keys():
                new_eventdict['user']='user'+str(mapuser[eventdict['user']])
            else:
                mapuser[eventdict['user']]=currentuser
                currentuser=currentuser+1
                new_eventdict['user']='user'+str(mapuser[eventdict['user']])
            new_eventdict['createtime']=eventdict['issuecreated_at']
            new_eventdict['durationtime']=eventdict['duration']

            #print(eventdict['assignee'])
            if eventdict['assignee'] is None:
                new_eventdict['assignee']='None'
            else:
                if eventdict['assignee'] in mapuser.keys():
                    new_eventdict['assignee']='user'+str(mapuser[eventdict['assignee']])
                else:
                    mapuser[eventdict['assignee']]=currentuser
                    currentuser=currentuser+1
                    new_eventdict['assignee']='user'+str(mapuser[eventdict['assignee']])

            new_eventdict['commentsnumber']=eventdict['comments']

            eventdict['user']=new_eventdict['user']
            eventdict['assignee']=new_eventdict['assignee']
            newevents.append(eventdict)
            #print(event.__dict__)
        newissues[issue]=newevents
        issueinfo.append(new_eventdict)
    print(mapuser)
    #print(issueinfo)
    with open('project3.json', 'w') as outfile:
            json.dump(newissues, outfile)
    with open('project3_issueinfo.json', 'w') as outfile:
            json.dump(issueinfo, outfile)
    csv_writer(issueinfo,'project3_issueinfo.csv')
    
        
 
launchDump() 
