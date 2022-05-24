# [백준] 11021번 - A+B - 7
# 블로그 주소 : https://tteum.tistory.com/199

import sys

T = int(input())
input = []

for i in range(T):
    input = list(map(int,sys.stdin.readline().split()))
    print("Case"+" #"+str(i+1)+":",sum(input))