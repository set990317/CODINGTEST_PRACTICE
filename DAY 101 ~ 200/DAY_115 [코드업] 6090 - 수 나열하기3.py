# [코드업] 6090 - 수 나열하기3
# 블로그 주소 : https://tteum.tistory.com/255

import sys

a, m, d, n = map(int, sys.stdin.readline().split())

for _ in range(1,n):
    a = a * m + d

print(a)