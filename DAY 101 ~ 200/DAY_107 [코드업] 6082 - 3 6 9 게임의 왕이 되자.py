# [코드업] 6082 - 3 6 9 게임의 왕이 되자
# 블로그 주소 : https://tteum.tistory.com/244

import sys

n = int(sys.stdin.readline())

for num in range(1,n+1):
    if num % 10 == 3 or num % 10 == 6 or num % 10 == 9:
        print("X",end = ' ')
    else : print(num,end = ' ')