from collections import defaultdict

N = int(input())
ls = list(map(int, input().split()))

dic = defaultdict(int)

for num in ls:
    dic[num] += 1

count = 0
for key in dic:
    count += dic[key] // 2

print(count)