# C - Max MEX
# https://atcoder.jp/contests/abc290/tasks/abc290_c
n, k = map(int, input().split())
a = list(map(int, input().split()))
a = list(set(a))
a.sort()

result = 0
for i in range(len(a)):
    if a[i] == result:
        result += 1
    else:
        break
result = min(result, k)

print(result)