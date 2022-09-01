# [백준] 10773번 - 제로
# 블로그 주소 : https://tteum.tistory.com/314

import sys

k = int(input())
result = []

for _ in range(k):
    n = int(sys.stdin.readline())
    if n == 0:
        del result[-1]
    else :
        result.append(n)

print(sum(result))