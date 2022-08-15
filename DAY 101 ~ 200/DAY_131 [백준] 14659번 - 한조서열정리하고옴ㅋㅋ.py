# [백준] 14659번 - 한조서열정리하고옴ㅋㅋ
# 블로그 주소 : https://tteum.tistory.com/280

import sys
N = int(sys.stdin.readline())
hanzo = list(map(int, sys.stdin.readline().split()))
winner = hanzo[0]
result = []
count = 0

for i in range(1,len(hanzo)):
    if winner < hanzo[i]:
        winner = hanzo[i]
        result.append(count)
        count = 0
    else :
        count += 1
        if i == len(hanzo)-1:
            result.append(count)
            
print(max(result))