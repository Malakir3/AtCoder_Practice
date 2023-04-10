# C - Merge Sequences 
N, M = map(int, input().split())

ls_a = list(map(int, input().split()))
ls_b = list(map(int, input().split()))
ls_c = sorted(ls_a + ls_b)

dic = {}
for index, num in enumerate(ls_c,1):
    dic[num] = index

ans_a = []
ans_b = []

for a in ls_a:
    ans_a.append(dic[a])

for b in ls_b:
    ans_b.append(dic[b])

print(" ".join([str(x) for x in ans_a]))
print(" ".join([str(y) for y in ans_b]))
