# C - LRUD Instructions 2 
from collections import defaultdict

n = int(input())
s_ls = [ _ for _ in input()]

dic = defaultdict(set)
x = 0
y = 0
dic[(0,0)] = 0
for str in s_ls:
    if str == "R":
        x += 1
    elif str == "L":
        x -= 1
    elif str == "U":
        y += 1
    else:
        y -= 1

    dic[(x,y)] = 0

if len(dic) != n+1:
    print('Yes')
else:
    print('No')