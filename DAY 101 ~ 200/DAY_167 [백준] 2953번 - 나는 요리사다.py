# [백준] 2953번 - 나는 요리사다
# 블로그 주소 : https://tteum.tistory.com/323

import sys

winner = 0
max_score = 0

for i in range(5):
    score = list(map(int,sys.stdin.readline().split()))
    if max_score < sum(score):
        max_score = sum(score)
        winner = i+1

print(winner,max_score)