import os,sys;

def mkNodes(nodeCnt, paramCnt, inData, nodes, cnt):
    print(nodeCnt, paramCnt);
    #print(len(inData));
    #print('mkNodes ', nodeCnt, paramCnt, inData, nodes, cnt);
    if (nodeCnt > 0) :
        if (paramCnt == 0) :# если параметров нет
            nodes[cnt] = [];
            inData = inData[2:];
        else:
            nodes[cnt] = inData[-paramCnt:];
            inData = inData[2:-paramCnt]; # срез от 2, за минусом параметров в конце
    else: # 
        nodes[cnt] = inData[2:2+paramCnt:];
        inData = inData[2+paramCnt:];
    #paramCnt == 0
    if (len(inData)>2):
        #mkNodes(inData[0], inData[1], inData, nodes, cnt+1);
        #print(inData);
        return inData;
    else:
        #print('Qq!!', inData);
        return;
    return

inData = []
nodes = dict();

for line in open('input.txt'):
    l = line.split();
    for itm in l:
        inData.append(int(itm));

#mkNodes(inData[0], inData[1], inData, nodes, 0);
print(len(nodes)); #, nodes);
cnt = 0;
while (inData != None):
    inData = mkNodes(inData[0], inData[1], inData, nodes, cnt);
    #print(inData);
    cnt += 1;
    if (cnt%100 == 0) :print(cnt);
#print(len(nodes), nodes);
s = 0;
for i in nodes:
    s += sum(nodes[i]);
print(s);
