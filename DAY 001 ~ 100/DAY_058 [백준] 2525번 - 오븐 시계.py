# [백준] 2525번 - 오븐 시계
# 블로그 주소 : https://tteum.tistory.com/191

# 성공 코드 1
import sys

H,M = map(int, sys.stdin.readline().split())
plus_M = int(sys.stdin.readline())

M += plus_M
H += (M // 60)
M %= 60
H %= 24

print(H,M)

# 성공 코드 2
import sys

hour, min = map(int, sys.stdin.readline().split())
new_min = int(sys.stdin.readline())

min = min + new_min

while min >= 60 :
    min = min-60
    hour += 1
    if hour == 24 :
        hour = 0

print(hour, min)