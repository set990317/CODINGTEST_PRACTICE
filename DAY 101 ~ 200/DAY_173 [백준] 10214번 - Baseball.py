# [백준] 10214번 - Baseball
# 블로그 주소 : https://tteum.tistory.com/330

import sys

t = int(input())

for _ in range(t):
    yonsei = 0
    korea = 0
    for _ in range(9):
        tmp = list(map(int,sys.stdin.readline().split()))

        yonsei += tmp[0]
        korea += tmp[1]

    if yonsei < korea :
        print("Korea")
    elif yonsei > korea :
        print("Yonsei")
    else :
        print("Draw")