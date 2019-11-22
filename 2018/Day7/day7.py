import os, sys, re;
import string;

def mkChanges(scheme, lttr, nodes):
    #print(nodes[1]);
    for node in nodes[1]:
        print('---',node, scheme[node], scheme[node][0]);
        scheme[node][0].remove(lttr);
    del scheme[lttr];
    print('***\n\n',scheme,'***\n\n');
    
    return;

step1 = [];
step2 = [];
alpha = list(string.ascii_uppercase);
step = [];
scheme = dict();
for l in open('input.txt','r'):
    lpart = re.search(r'Step (.) must be finished before step (.) can begin.',l);
    #print(lpart, lpart.groups(), lpart.group(1));
    start = lpart.group(1);
    end = lpart.group(2);
    if (start not in step1) :
        step1.append(start);
    if (end not in step2) :
        step2.append(end);
    if (not start in scheme): scheme[start]=([],[end]);
    else: scheme[start][1].append(end);
    if (not end in scheme): scheme[end] = ([start],[]);
    else: scheme[end][0].append(start);
    step.append((lpart.group(1), lpart.group(2)));
print('\n\n',scheme,'\n\n');
step1.sort();
step2.sort();
endNode = [item for item in alpha if item not in step1]
startNode = [item for item in alpha if item not in step2];
print(step1, endNode, startNode, step);
print(step2, len(step2));
isOut = True;
k = list(scheme.keys());
k.sort();
print(k, '\n\n',scheme,'\n\n');
part1 = '';
while (isOut) :
    k = list(scheme.keys());
    k.sort();
    for lttr in k:
        print(lttr, );
        if (len(scheme[lttr][0])==0) :
            part1 += lttr;
            mkChanges(scheme, lttr, scheme[lttr]);
            print(lttr, scheme);
            break;
    if (len(scheme)==0): isOut = False;
print('Part1: ',part1);

