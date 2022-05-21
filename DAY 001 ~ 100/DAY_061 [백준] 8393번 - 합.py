# [백준] 8393번 - 합
# 블로그 주소 : https://tteum.tistory.com/194

import sys

n = int(sys.stdin.readline())
total = 0

for i in range(1,n+1):
    total += i
print(total)