T = int(input())

n_list = []
a_list = []
for _ in range(T):
    n_list.append(int(input()))
    a_list.append(list(map(int, input().split())))

for test in a_list:
    count = 0
    for a in test:
        if a % 2 != 0:
            count += 1
    print(count)            