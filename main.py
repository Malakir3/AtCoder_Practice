import sys
total_num, mark_num = map(int, input().split())

if mark_num == 0:
  ans = list(range(1,total_num+1))
  print(*ans)
  sys.exit()

mark_place_list = list(map(int, input().split()))

result = []
temp_list = []
pre_num = 0
count = 0
for num in mark_place_list:
    count += 1

    if num == pre_num + 1:
        temp_list.append(num)
    else:
        temp_list.append(pre_num + 1)
        result.extend(reversed(temp_list))
        temp_list = []
        if num - pre_num > 2:
            result.extend(list(range(pre_num+2,num)))            
        
        temp_list.append(num)

    if count == mark_num:
        temp_list.append(num + 1)

    pre_num = num

result.extend(reversed(temp_list))

last_num = mark_place_list[mark_num-1]
additional_num = total_num - last_num

if  additional_num > 1:
    left_list = list(range(last_num+2,total_num+1))
    result.extend(left_list)

print(" ".join(map(str,result)))    