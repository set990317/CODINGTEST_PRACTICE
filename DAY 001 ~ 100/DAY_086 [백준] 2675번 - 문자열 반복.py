# [백준] 2675번 - 문자열 반복
# 블로그 주소 : https://tteum.tistory.com/221

import sys

n = int(input())

for _ in range(n):
    r, s = sys.stdin.readline().split()
    r = int(r)
    p = ''
    for i in range(len(s)):
        print(s[i] * r, end='')
    print()