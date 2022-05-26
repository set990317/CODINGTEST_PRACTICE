# [백준] 11022번 - A+B - 8
# 블로그 주소 : https://tteum.tistory.com/200

import sys

T = int(sys.stdin.readline())

for i in range(1,T+1):
    A, B = map(int, sys.stdin.readline().split())
    print("Case #"+str(i)+":",A,"+",B,"=",A+B)