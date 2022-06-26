# [백준] 1978번 - 소수 찾기
# 블로그 주소 : https://tteum.tistory.com/232

import sys

def sosu (num):
    if num == 1 :
        return 0
    for i in range(2,num):
        if num % i == 0:
            return 0
    return 1

n = int(input())
arr = list(map(int, sys.stdin.readline().split()))
cnt = 0
for i in range(len(arr)):
    cnt += sosu(arr[i])

print(cnt)