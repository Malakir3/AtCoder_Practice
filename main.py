# C - Coverage
import itertools

n,m = map(int, input().split())
c_ls = []
a_ls = [] #[[1,2],[1,3],[2]]
for _ in range(m):
    c_ls.append(int(input()))
    a_ls.append(list(map(int, input().split())))

count = 0
for comb_num in range(1,len(a_ls)+1):
    tmp_ls = itertools.combinations(a_ls,comb_num)    
    for each_tmp_ls in tmp_ls: # [[1,2],[1,3],[2]]
        my_ls = []
        for each_ls in each_tmp_ls: # [1,2]
            for a in each_ls:
                my_ls.append(a)
        my_set = set(my_ls)
        if len(my_set) == n:
            count += 1

print(count)