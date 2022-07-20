# [코드업] 6087 - 3의 배수는 통과
# 블로그 주소 : https://tteum.tistory.com/252

import sys

N = int(sys.stdin.readline())

for i in range(1,N+1):
    if i % 3 != 0 :
        print(i, end=' ')  