# [백준] 2455번 - 지능형 기차
# 블로그 주소 : https://tteum.tistory.com/322

import sys

total = 0
max = 0

for _ in range(4):
    a, b = map(int, sys.stdin.readline().split())

    total = total - int(a)

    if max < total :
        max = total

    total = total + int(b)

    if max < total :
        max = total

print(max)