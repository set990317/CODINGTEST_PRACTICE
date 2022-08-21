# [백준] 10817번 - 세 수
# 블로그 주소 : https://tteum.tistory.com/303

import sys

arr = list(map(int,sys.stdin.readline().split()))
arr.sort()

print(arr[1])