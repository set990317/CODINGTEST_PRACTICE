# [백준] 1032번 - 명령 프롬프트
# 블로그 주소 : https://tteum.tistory.com/318

import sys

n = int(input())
file = []
answer = ''

for _ in range(n):
    file.append(sys.stdin.readline())

for i in range(len(file[0])):
    status = True
    for j in range(0,n-1):
        if file[j+1][i] != file[j][i]:
            status = False
            break
    if status == True:
        answer += file[0][i]
    else :
        answer += '?'

print(answer)