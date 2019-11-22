import os,sys;
from collections import defaultdict;


def mkNodes(nodeCnt, paramCnt, inData, nodes, cnt):
    inData = inData[2:];
    #print('ini', nodeCnt, paramCnt, nodes, cnt); #inData,
    #print(len(inData));
    #print('mkNodes ', nodeCnt, paramCnt, inData, nodes, cnt);
    if (nodeCnt == 0) :
        #print('node 0', paramCnt, inData[:paramCnt:], inData[paramCnt:]);
        nodes[cnt] = inData[:paramCnt:];
        inData = inData[paramCnt:];
        #print('node 0-2',inData, nodes);
        return sum(nodes[cnt]), sum(nodes[cnt]), inData;
    sm = 0; v = defaultdict(int); vm = 0;
    for n in range(nodeCnt):
        #print('-->', cnt, inData, paramCnt);
        val, m, inData = mkNodes(inData[0], inData[1], inData, nodes, cnt+n+1);
        sm +=m;
        v[n] = val;
        #print('<--', cnt, inData, paramCnt);
    #print('-S ', paramCnt, cnt, inData, nodes );
    for p in range(paramCnt):
        vm += v[inData[p]];
    nodes[cnt] = inData[:paramCnt:];
    #print(inData, ' = ', inData[paramCnt:]);
    inData = inData[paramCnt:];
    #print('*S ', cnt, paramCnt, 'inData: ', inData, nodes);
    sm += sum(nodes[cnt]);
    return vm, sm, inData;

inData = []
nodes = dict();

for line in open('input.txt'):
    l = line.split();
    for itm in l:
        inData.append(int(itm));

#mkNodes(inData[0], inData[1], inData, nodes, 0);
print(len(nodes), inData); #, nodes);
cnt = 0;
sm = 0; v = 0;
while (inData != None or len(inData)>0 ):
    v, sm, inData = mkNodes(inData[0], inData[1], inData, nodes, cnt);
    #print(inData);
    cnt += 1;
    if (cnt%100 == 0) :print(cnt);
    break;
print('nodes  ',len(nodes), nodes, sm, v);

