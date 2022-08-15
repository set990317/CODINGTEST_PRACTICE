# [백준] 2869번 - 달팽이는 올라가고 싶다
# 블로그 주소 : https://tteum.tistory.com/279

import sys

a, b, v = map(int, sys.stdin.readline().split())

result = 0

v = v - a
result += 1

result += v // (a - b)

if v % (a-b) != 0 :
    result += 1

print(result)