# [백준] 25304번 - 영수증
# 블로그 주소 : https://tteum.tistory.com/294

import sys

money = int(input())
n = int(input())

for _ in range(n):
    a, b = map(int,sys.stdin.readline().split())
    money -= a * b

if money == 0:
    print("Yes")
else :
    print("No")