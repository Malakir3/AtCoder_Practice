N = int(input())
S = list(input())

for i in range(1, N):
    print(i)
    k = 0
    l = 0
    for k in range(1, N):
        if S[k-1] != S[k-1+i]:
            l += 1
        else:
            print(l)
            break
        