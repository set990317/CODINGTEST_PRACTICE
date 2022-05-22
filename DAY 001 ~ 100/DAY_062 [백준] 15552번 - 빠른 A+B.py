# [백준] 15552번 - 빠른 A+B
# 블로그 주소 : https://tteum.tistory.com/195

import sys

T = int(sys.stdin.readline())

for i in range(T):
    x, y = map(int,sys.stdin.readline().split())
    print(x+y)