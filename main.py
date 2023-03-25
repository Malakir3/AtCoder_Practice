total_num, mark_num = map(int, input().split())
mark_place_list = list(map(int, input().split()))

result = []
temp_list = []
pre_num = 0
for num in mark_place_list:
    if num == pre_num + 1:
        temp_list.append(num)
    else:
        temp_list.append(pre_num + 1)
        result.extend(reversed(temp_list))
        temp_list = []
        if num - pre_num > 2:
            result.extend(list(range[pre_num+2:num-1]))            
        else:
            temp_list.append(num)
    pre_num = num

result.extend(reversed(temp_list))
print(" ".join(result))    