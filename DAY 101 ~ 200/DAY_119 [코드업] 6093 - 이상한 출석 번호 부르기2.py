# [코드업] 6094 - 이상한 출석 번호 부르기3
# 블로그 주소 : https://tteum.tistory.com/259

import sys

T = int(input())
input = list(map(int,sys.stdin.readline().split()))

min = input[0]
for i in range(1,T):
    if input[i] < min:
        min = input[i]
print(min)