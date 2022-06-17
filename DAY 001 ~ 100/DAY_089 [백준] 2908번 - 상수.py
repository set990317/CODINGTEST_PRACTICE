# [백준] 2908번 - 상수
# 블로그 주소 : https://tteum.tistory.com/224

import sys

s = list(map(str, sys.stdin.readline().split()))
new = []
for i in range(2):
    tmp = ''
    for j in range(2,-1,-1):
        tmp += s[i][j]
    new.append(tmp)

print(max(new))