N = int(input())
ls = list(map(int, input().split()))

# st = set(ls)

# count = 0
# for color in st:
#     count += ls.count(color) // 2

# print(count)


s_ls = sorted(ls)

pre_color = 0
count = 0
for color in s_ls:
    if pre_color == 0:
        pre_color = color
        continue
    
    if color == pre_color:
        count += 1
        pre_color = 0
    else:
        pre_color = color
        
print(count)