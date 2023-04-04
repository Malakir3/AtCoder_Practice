N, X = map(int, input().split())
ls = list(map(int, input().split()))

st = set(ls)

ans = 'No'
for num in st:
    if num + X in st:
        ans = 'Yes'
        break

print(ans)
