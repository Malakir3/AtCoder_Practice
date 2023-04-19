# C - Max MEX
# https://atcoder.jp/contests/abc290/tasks/abc290_c
import sys

n,k = map(int, input().split())
a_ls = [ _ for _ in map(int, input().split())]

a_set = sorted(set(a_ls))

if a_set[0] != 0:
    print(0)
    sys.exit()
elif len(a_set) == k:
    if k == 1:
        print(1)
    else:
        print(k)
    sys.exit()

pre_num = -1
for index, i in enumerate(a_set):
    result = pre_num + 1

    if i == result:
        pre_num = i
    else:
        break
    
    if index > k-1:
        break

if result == 0:
    print(1)
else:
    print(result)
# 7 3
# 2 0 2 3 2 1 4
# [0, 1, 2, 3, 4]