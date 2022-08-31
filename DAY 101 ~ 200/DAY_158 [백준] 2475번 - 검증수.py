# [백준] 2475번 - 검증수
# 블로그 주소 : https://tteum.tistory.com/311

import math

num = list(map(int,input().split()))
result = 0

for i in num:
    result += math.pow(i,2)

result = result % 10
print(int(result))