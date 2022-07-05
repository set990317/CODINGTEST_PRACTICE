# [코드업] 6080 - 주사위 2개 던지기
# 블로그 주소 : https://tteum.tistory.com/242

import sys

n,m = map(int,sys.stdin.readline().split())

for i in range(1,n+1):
    for j in range(1,m+1):
        print(i,j)