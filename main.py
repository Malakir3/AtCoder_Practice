N = int(input())
S = list(input())

for i in range(1, N):
    count = N-i
    for k in range(N-i):      
        if S[k] == S[i+k]:
            count = k
            break
    
    print(count)

        