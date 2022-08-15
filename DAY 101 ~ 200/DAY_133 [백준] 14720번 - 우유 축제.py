# [백준] 14720번 - 우유 축제
# 블로그 주소 : https://tteum.tistory.com/282

import sys

N = int(input())
milk = list(map(int, sys.stdin.readline().split()))
milk_answer = [0,1,2]
milk_answer_point = 0
count = 0

for i in range(len(milk)):
    if milk[i] == milk_answer_point:
        count += 1
        if milk_answer_point == 2 :
            milk_answer_point = -1
        milk_answer_point += 1

print(count)