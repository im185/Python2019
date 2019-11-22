import os, sys;

fl = open('input.txt','r');
fl.close;
for l in fl:
    #print(l);
    i = 0;
    maxi = len(l);
    print(l, maxi);
    while i < maxi-1:
        if (l[i]!=l[i+1] and (l[i]==l[i+1].upper() or l[i]==l[i+1].lower())):
            l = l[:i]+l[i+2:];
            maxi -= 2;
            i -= 1;
            if (i<0) : i=0;
            print( maxi, i);
        else:
            i += 1;
            #print(maxi, i);
    print(l, len(l));
        
