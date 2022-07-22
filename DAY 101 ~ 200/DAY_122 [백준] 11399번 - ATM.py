# [코드업] 11399번 - ATM
# 블로그 주소 : https://tteum.tistory.com/265

import sys

n = int(input())
time = list(map(int, sys.stdin.readline().split()))
total = 0
tmp = 0

time.sort()

for i in range(n):
    total += tmp + time[i]
    tmp += time[i]

print(total)