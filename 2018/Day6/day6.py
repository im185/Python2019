import os;
from collections import defaultdict;

def d(pA, pB):
    return abs(pA[0]-pB[0]) + abs(pA[1]-pB[1]);

def closest(x,y):
    ds = [(d(p, (x,y)), p) for p in P];
    ds.sort();
    if(ds[0][1]==(5,5)):print('ds:',x,y, ds, ds[0][0],ds[1][0],ds[0][1]);
    if ds[0][0] < ds[1][0]:
        return ds[0][1];
    else:
        return (-1,-1);

def score_around(W):
    score = defaultdict(int);
    for x in range(0, xhi+W): #xlo-W, xhi+W
        for y in range(0, yhi+W):#ylo-W, yhi+W
            score[closest(x,y)] += 1;
            if(closest(x,y)==(5,5)):print('x,y,score: ',x,y,score);
    return score;

P = []
for l in open('input_tst.txt'):
    x,y = [int(s.strip()) for s in l.split(',')];
    #print(x,y);
    P.append((x,y));
print(P);
xlo = min([x for x,y in P]);
xhi = max([x for x,y in P]);
ylo = min([y for x,y in P]);
yhi = max([y for x,y in P]);
print ('X:', xlo, xhi);
print ('Y:', ylo, yhi);

S2 = score_around(20);#400
print("\n\n\nS2:\n",S2);
#S3 = score_around(25);#600
#print("\n\n\nS2:\n",S3);

#best = [(S2[k] if S2[k]==S3[k] else 0, k) for k in S2.keys()];#if S2[k]==S3[k] - result insideregion? good!
best = [(S2[k], k) for k in S2.keys()];
best.sort();
print('BEST:\n\n\n', best);
for area, p in best:
    print (area, p);
