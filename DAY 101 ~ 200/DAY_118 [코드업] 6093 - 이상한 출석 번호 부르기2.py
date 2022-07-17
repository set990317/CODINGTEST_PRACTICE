# [코드업] 6093 - 이상한 출석 번호 부르기2
# 블로그 주소 : https://tteum.tistory.com/258

import sys

n = int(sys.stdin.readline())
a = list(sys.stdin.readline().split())

for i in range(n-1,-1,-1):
    print(a[i], end =' ')