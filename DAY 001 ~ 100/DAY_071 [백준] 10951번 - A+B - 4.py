# [백준] 10951번 - A + B - 4
# 블로그 주소 : https://tteum.tistory.com/205

import sys

while(True):
    try :
        A, B = map(int, sys.stdin.readline().split())
        print(A + B)
    except ValueError :
        break