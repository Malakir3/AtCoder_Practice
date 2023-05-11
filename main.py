import string
# https://atcoder.jp/contests/abc285/tasks/abc285_c

str = list(input())

ls = string.ascii_uppercase
dic = {}
for i, letter in enumerate(ls, 1):
    dic[letter] = i

ans = 0
for index, s in enumerate(str[::-1]):
    ans += 26**index * dic[s]

print(ans)
    