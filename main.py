# C - Four Variables

n = int(input())

# 1 <= ab <= n-1を満たすa,bの組み合わせ（約数の数）を調べる。
# 一方が決まれば他方も決まる。

# その後、cd = n-abを満たすc,dの組み合わせを調べる。

# resultに、abとcdの組み合わせ方の数を加える。
# a != b かつ、c !=d のときは+4
# a = b かつ、c = d のときは+1
# 他は+2
# dic = map()
ls = list()
for ab in range(1,n):
    # count = 0
    i = 1
    while i**2 <= ab:
        if ab % i == 0:
            a = i
            b = ab // i
            cd = n - ab

            j = 1
            while j**2 <= cd:
                if cd % j == 0:
                    c = j
                    d = cd // j
                ls.append([a,b,c,d])
                j += 1
        i += 1

count = 0
for pair in ls:
    a = pair[0]
    b = pair[1]
    c = pair[2]
    d = pair[3]
    if a != b & c != d:
        count += 4
    elif len(set(pair)) == 1:
        count += 1
    else:
        count += 2

print(count)        

