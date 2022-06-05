# [백준] 1546번 - 평균
# 블로그 주소 : https://tteum.tistory.com/211

import sys

n = int(input())
arr = list(map(int,sys.stdin.readline().split()))

max = max(arr)

for i in range(n):
    arr[i] = arr[i] / max * 100

avg = sum(arr) / len(arr)
print(avg)