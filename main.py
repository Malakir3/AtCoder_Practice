# C - Max MEX
# https://atcoder.jp/contests/abc290/tasks/abc290_c
import sys

n,k = map(int, input().split())
a_ls = [ _ for _ in map(int, input().split())]

a_set = sorted(set(a_ls))

if a_set[0] != 0:
    print(0)
    sys.exit()

pre_num = -1
count = 0
while count <= k+1:
  for i in a_set:
      count += 1
      result = pre_num + 1

      if i == pre_num + 1:
          pre_num = i
      else:
          break
      
print(result)