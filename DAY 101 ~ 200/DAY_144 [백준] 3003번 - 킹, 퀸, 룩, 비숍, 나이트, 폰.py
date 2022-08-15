# [백준] 3003번 - 킹, 퀸, 룩, 비숍, 나이트, 폰
# 블로그 주소 : https://tteum.tistory.com/293

import sys

chess = list(map(int,sys.stdin.readline().split()))
answer = [1,1,2,2,2,8]

for i in range(len(chess)):
    print(answer[i]-chess[i], end =' ')