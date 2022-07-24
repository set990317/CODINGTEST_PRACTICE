# [코드업] 11047번 - 동전 0
# 블로그 주소 : https://tteum.tistory.com/267

import sys

n, k = map(int, sys.stdin.readline().split())
money = []
result = 0

for _ in range(n):
    money.append(int(input()))

for i in range(len(money)-1,-1,-1):
    result += k // money[i]
    k = k % money[i]

print(result)