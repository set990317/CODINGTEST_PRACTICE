# [백준] 10871번 - X보다 작은 수
# 블로그 주소 : https://tteum.tistory.com/203

import sys

n, x = map(int, sys.stdin.readline().split())
list = list(map(int, sys.stdin.readline().split()))
little = []

for num in list:
    if num < x :
        little.append(num)

for num in little :
    print(num, end=' ')