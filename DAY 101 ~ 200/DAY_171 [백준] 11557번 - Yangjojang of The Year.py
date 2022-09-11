# [백준] 11557번 - Yangjojang of The Year
# 블로그 주소 : https://tteum.tistory.com/328

import sys

T = int(input())

for _ in range(T):
    N = int(input())
    max = 0

    for _ in range(N):
        alcohol = list(sys.stdin.readline().split())
        if max < int(alcohol[1]):
            max = int(alcohol[1])
            univ = alcohol[0]
    print(univ)