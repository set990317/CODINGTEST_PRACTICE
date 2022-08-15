# [백준] 2798번 - 블랙잭
# 블로그 주소 : https://tteum.tistory.com/289

import sys

n, m = map(int,sys.stdin.readline().split())
card = list(map(int,sys.stdin.readline().split()))
result = 0

for i in range(0,len(card)-2):
    for j in range(i+1,len(card)-1):
        for k in range(j+1,len(card)):
            hap = card[i]+card[j]+card[k]
            if hap <= m and result < hap:
                result = hap

print(result)