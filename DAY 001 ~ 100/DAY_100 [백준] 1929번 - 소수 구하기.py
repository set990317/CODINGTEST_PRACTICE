# [백준] 1929번 - 소수 구하기
# 블로그 주소 : https://tteum.tistory.com/235

import sys
def sosu (num):
    if num == 1 :
        return 0
    for i in range(2,int(num**0.5)+1):
        if num % i == 0:
            return 0
    print(num)
    return 0

n,m = map(int,sys.stdin.readline().split())

for num in range(n,m+1):
    sosu(num)