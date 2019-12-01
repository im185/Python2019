import sys;

def fuelTotal(amt):
    tax = 0;
    amt = int(amt);
    #print("amt : ", amt)
    if(amt < 6): # потому что вычитать 2
        return 0;
    else:
        amt = int(int(amt) / 3) - 2;
        tax +=  amt + fuelTotal(amt);
    #print("tax : " , tax);
    return tax;


fl = open('input.txt','r');
fl.close;
sum = 0;
sum2 = 0;
for l in fl:
    #print (l);
    sum += int(int(l) / 3) - 2;
    sum2 += fuelTotal(int(l));
    #print("sum2 : ", sum2);
print("Part1 : ", sum, "Part2: ", sum2);