N = int(input())
ls = list(map(int, input().split()))

st = set(ls)

count = 0
for color in st:
    count += ls.count(color) // 2

print(count)
