import os, sys, re;
from datetime import datetime, date, time

def mkMinutesFriq(minutes, startTime, stopTime):
# (curTime-mwSleep[curMW]).seconds/60;
    #print(minutes, startTime, stopTime);
    minutesStart = startTime.minute;
    for i in range(int((stopTime-startTime).seconds/60)+1):
        #print(i+minutesStart);
        if(not i+minutesStart in minutes): minutes[i+minutesStart] = 0;
        minutes[i+minutesStart] += 1;
    return;

data = [line.strip() for line in open("input.txt", 'r')]
#print(type(data), data.sort());
data.sort();
#print(data);
manoWar = dict();
mwSleep = dict();
curMW = '';
for l in data:
    lpart =re.search(r'\[(.*)\] (.*) (.*)', l)
    #print(lpart.groups().length);
    #print(l, "---",  lpart.groups(), lpart.group,'--', lpart[1], '--',lpart[2]);
    #print(datetime.strptime(lpart[1],"%Y-%m-%d %H:%M"));
    curTime = datetime.strptime(lpart[1],"%Y-%m-%d %H:%M");
    if (lpart[2]=='falls'):
        mwSleep[curMW] = curTime;
    elif (lpart[2]=='wakes'):
        #print(curTime, mwSleep[curMW], curMW, (curTime-mwSleep[curMW]) );
        manoWar[num[1]] += (curTime-mwSleep[curMW]).seconds/60;
        #print(manoWar[num[1]]);
        mwSleep.pop(curMW, None);
    else:
        num = re.search(r'#(.*) ', lpart[2]);
        curMW = num[1];
        if (not (num[1] in manoWar)) :
            manoWar[num[1]] = 0;
        #print(lpart[2], num, num[1]);
print('----', manoWar, max(manoWar.values()), );
p2 = dict();
sl = list(manoWar.keys())[list(manoWar.values()).index(max(manoWar.values()))];
print("Sleeper: ",sl);
for sl in manoWar.keys():
    #print(sl);
    if(manoWar[sl]==0): break;
    isPrint = False;
    minutes = dict();
    for l in data:
        lpart =re.search(r'\[(.*)\] (.*) (.*)', l);
        qq = lpart[2];
        if (lpart[2]=='falls'):
            if(isPrint): startTime = datetime.strptime(lpart[1],"%Y-%m-%d %H:%M");
        elif (lpart[2]=='wakes'):
            if(isPrint):
                stopTime = datetime.strptime(lpart[1],"%Y-%m-%d %H:%M");
                mkMinutesFriq(minutes, startTime, stopTime);
        else:
            num = re.search(r'#(.*) ', lpart[2]);
            curMW = num[1];
            if (curMW == sl):
                isPrint = True;
            else:
                isPrint = False;
            if (not (num[1] in manoWar)) :
                manoWar[num[1]] = 0;
        if (isPrint) :
            curTime = datetime.strptime(lpart[1],"%Y-%m-%d %H:%M");
            # print(l, curTime);
    print("Sleeper: ",sl, minutes, max(minutes.values()));
    p2[sl] = max(minutes.values());
print();
print(p2);
print("Part2 ", 179 * 30);
