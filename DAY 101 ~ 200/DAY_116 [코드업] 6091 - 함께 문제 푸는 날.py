# [코드업] 6091 - 함께 문제 푸는 날
# 블로그 주소 : https://tteum.tistory.com/256

import sys

a, b, c = map(int, sys.stdin.readline().split())
day = 0
for num in range(1,a*b*c+1):
    if num % a == 0 :
        if num % b == 0:
            if num % c == 0:
                day = num
                break
print(day)