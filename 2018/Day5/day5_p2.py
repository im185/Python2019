import os, sys;
import string;

def mkChanges(ini_str):
    i = 0;
    maxi = len(ini_str);
    print(ini_str, maxi);
    while i < maxi-1:
        if (ini_str[i]!=ini_str[i+1] and (ini_str[i]==ini_str[i+1].upper() or ini_str[i]==ini_str[i+1].lower())):
            ini_str = ini_str[:i]+ini_str[i+2:];
            maxi -= 2;
            i -= 1;
            if (i<0) : i=0;
            #print( maxi, i);
        else:
            i += 1;
            #print(maxi, i);
    print("Part1 ", len(ini_str)); #9078
    
    return len(ini_str);

fl = open('input.txt','r');
fl.close;
alpha = list(string.ascii_lowercase);
alpha.append('');
print(alpha);
all_lettr = dict();
for l in fl:
    for lttr in alpha:
        lmod = l.replace(lttr,'').replace(lttr.upper(),'');
        print(len(lmod), lttr, lttr.upper());
        lm = mkChanges(lmod);
        print('len(lmod) ', lm);
        all_lettr[lttr] = lm;
print(all_lettr, min(all_lettr.values()));
