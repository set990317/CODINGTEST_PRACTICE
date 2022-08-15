# [백준] 10156번 - 과자
# 블로그 주소 : https://tteum.tistory.com/292

import sys

snack, n, money = map(int,sys.stdin.readline().split())

a = ( snack * n ) - money

if a <= 0 :
    print(0)
else :
    print(a)