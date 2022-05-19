# [백준] 10950번 - A+B - 3
# 블로그 주소 : https://tteum.tistory.com/193

import sys

T = int(sys.stdin.readline())

for _ in range(T):
    A,B = map(int, sys.stdin.readline().split())
    print(A+B)