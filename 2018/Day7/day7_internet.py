from collections import defaultdict
# Edges
E = defaultdict(list)
# In-degree
D = defaultdict(int)
for line in open('input.txt'):
	words = line.split()
	x = words[1]
	y = words[7]
	E[x].append(y); #что из вершины выходит
	D[y] += 1; #сколько в вершину входит
print(E,'\n\n',D);
for k in E:
	E[k] = sorted(E[k]);#сортировка исходящих вершин, условие задачи

print(E);
# time
t = 0
# Events
EV = []
# Work queue
Q = []
def add_task(x):
	Q.append(x)
def start_work():
	global Q
	while len(EV) < 5 and Q:
		x = min(Q);
		print('\nx:',x);
		Q = [y for y in Q if y!=x]
		print( 'Starting {} at {}'.format(x, t));
		EV.append((t+61+ord(x)-ord('A'), x))

for k in E:
	if D[k] == 0:
		add_task(k)
print('\nQ:',Q, '\nEV',EV);
start_work()
print('start', '\nQ:',Q, '\nEV',EV);
while EV or Q:
        t, x = min(EV);
        print('EV, Q, t,x:',EV, Q, t, x);
        EV = [y for y in EV if y!=(t,x)];#pop from EV (t,x)
        for y in E[x]: #E[x] что выхдит из вершины x
                D[y] -= 1;
                if D[y] == 0:
                        print('into Q ', y);
                        add_task(y);
        start_work();
print(t);
