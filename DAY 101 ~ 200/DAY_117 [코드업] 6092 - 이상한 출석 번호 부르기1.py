# [코드업] 6092 - 이상한 출석 번호 부르기1
# 블로그 주소 : https://tteum.tistory.com/257

import sys

n = int(sys.stdin.readline())
a = list(map(int,sys.stdin.readline().split()))
student = []

for i in range(1,24):
    print(a.count(i), end=' ')
