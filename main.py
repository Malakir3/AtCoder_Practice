all_num, tgt_num = map(int, input().split())

ranker_list = []
for index, _ in enumerate(range(all_num), 1):
    if index > tgt_num:
        input()
    else:
        ranker_list.append(input())

for name in sorted(ranker_list):
    print(name)