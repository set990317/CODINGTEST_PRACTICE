# [코드업] 6086 - 거기까지! 이제 그만~
# 블로그 주소 : https://tteum.tistory.com/251

import sys

N = int(sys.stdin.readline())
total = 0

for i in range(1,N+1):
    if total < N :
        total += i
    else : break
    
print(total)