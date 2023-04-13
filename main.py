# C - Make Takahashi Happy

# 3 3
# 3 2 2
# 2 1 3
# 1 5 4
# [[3, 2, 2], [2, 1, 3], [1, 5, 4]]

import itertools

H, W = map(int, input().split())

# [[3, 2, 2], [2, 1, 3], [1, 5, 4]]
ls = [ list(map(int, input().split())) for _ in range(H)]

move_num_ls = [ _ for _ in range(H+W-2)] # [0,1,2,...,H+W-1]

count = 0
for down_time in itertools.combinations(move_num_ls, H-1): # (0,2)等
    trail_log = set()
    trail_log.add(ls[0][0])
    
    x = 0
    y = 0
    for time in range(H+W-2):
        if time in down_time:
            y += 1
        else:
            x += 1
        trail_log.add(ls[y][x])
    
    if len(trail_log) == H+W-1:
        count += 1

print(count)

    