# [코드업] 10039번 - 평균 점수
# 블로그 주소 : https://tteum.tistory.com/288

import sys

data = [int(sys.stdin.readline()) for i in range(5)]
total = 0;

for i in data:
    if i<40:
        total += 40
    else : total += i

print(total//5)