# [백준] 2884번 - 알람 시계
# 블로그 주소 : https://tteum.tistory.com/190

import sys

H,M = map(int, sys.stdin.readline().split())

if (M < 45):
    if (H == 0):
        H = 24
    H -= 1
    M = M + 60 - 45

else :                  # (M이 45보다 같거나 큰 경우)
    M = M - 45

print(H,M)