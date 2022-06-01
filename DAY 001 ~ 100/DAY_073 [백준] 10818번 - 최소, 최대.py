# [백준] 10818번 - 최소, 최대
# 블로그 주소 : https://tteum.tistory.com/207

import sys

n = int(input())
arr = list(map(int, sys.stdin.readline().split()))

print(min(arr),max(arr))