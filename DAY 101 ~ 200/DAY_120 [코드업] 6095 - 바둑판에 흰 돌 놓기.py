# [코드업] 6095 - 바둑판에 흰 돌 놓기
# 블로그 주소 : https://tteum.tistory.com/263

import sys

d = [[0 for j in range(19)] for i in range(19)]
n = int(sys.stdin.readline())
input = []
for _ in range(n):
    x, y = map(int, sys.stdin.readline().split())
    input.append([x,y])

for i in range(len(input)):
    x = input[i][0] - 1
    y = input[i][1] - 1
    d[x][y] = 1

for i in range(19):
    for j in range(19):
        print(d[i][j], end=' ')
    print("")