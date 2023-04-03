N = int(input())
a_list = list(map(int, input().split()))
Q = int(input())

def my_query(arg_list):
    if arg_list[0] == 1:
        a_list[arg_list[1]-1] = arg_list[2]
    else:
        print(a_list[arg_list[1]-1])

for _ in range(Q):
    q = list(map(int, input().split()))
    my_query(q)
        
