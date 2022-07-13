# [코드업] 6088 - 수 나열하기1
# 블로그 주소 : https://tteum.tistory.com/253

import sys

a, d, n = map(int, sys.stdin.readline().split())

print(a+(n-1)*d)