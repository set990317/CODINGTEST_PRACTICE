# [백준] 2739번 - 구구단
# 블로그 주소 : https://tteum.tistory.com/192

import sys

N = int(sys.stdin.readline())

for i in range(1,10):
    print(str(N) + " * " + str(i) + " = " + str(N*i))