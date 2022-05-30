# [백준] 10952번 - A + B - 5
# 블로그 주소 : https://tteum.tistory.com/204

import sys

while (True):
    A, B = map(int, sys.stdin.readline().split())
    if A == B == 0:
        break
    print(A+B)
