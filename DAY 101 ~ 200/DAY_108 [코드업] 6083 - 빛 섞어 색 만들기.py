# [코드업] 6083 - 빛 섞어 색 만들기
# 블로그 주소 : https://tteum.tistory.com/245

import sys

r, g, b = map(int,sys.stdin.readline().split())

for i in range(0,r):
    for j in range(0,g):
        for k in range(0,b):
            print(i,j,k)
print(r*g*b)