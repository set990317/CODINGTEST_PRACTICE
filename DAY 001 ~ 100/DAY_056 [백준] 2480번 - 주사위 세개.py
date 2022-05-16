# [백준] 2480번 - 주사위 세개
# 블로그 주소 : https://tteum.tistory.com/189

import sys

a, b, c = map(int, sys.stdin.readline().split())

if (a == b == c):
    print(10000 + ( a * 1000 ))
elif (a != b != c and a != c):
    max = max(a,b,c)
    print(max * 100)
else :
    if a == b :
        equal = a
    elif b == c :
        equal = b
    else : equal = c # a와 c가 같은 경우
    print(1000+equal*100)