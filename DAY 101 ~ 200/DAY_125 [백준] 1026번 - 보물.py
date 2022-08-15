# [백준] 1026번 - 보물
# 블로그 주소 : https://tteum.tistory.com/268

import sys

n = int(input())
A = list(map(int, sys.stdin.readline().split()))
B = list(map(int, sys.stdin.readline().split()))

result = 0

A.sort()

for i in range(n):
    result += A[i] * max(B)
    B.remove(max(B))
    
print(result)