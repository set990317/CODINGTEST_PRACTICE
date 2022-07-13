# [코드업] 6089 - 수 나열하기2
# 블로그 주소 : https://tteum.tistory.com/254

import sys

a, r, n = map(int, sys.stdin.readline().split())

print(a*(r**(n-1)))