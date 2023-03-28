N, M = map(int, input().split())
s_list = [ input()[3:] for _ in range(N)]
t_list = [ input() for _ in range(M)]

s_list = sorted(s_list)
t_list = sorted(t_list)

count = 0
for s in s_list:
    for t in t_list:
        if s == t :
            count += 1
            break

print(count)