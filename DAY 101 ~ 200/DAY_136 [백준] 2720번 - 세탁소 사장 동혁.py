# [백준] 2720번 - 세탁소 사장 동혁
# 블로그 주소 : https://tteum.tistory.com/285

import sys

T = int(sys.stdin.readline())
money = [25, 10, 5, 1]
for _ in range(T):
    C = int(sys.stdin.readline())
    result = []
    for num in money:
        result.append(C // num)
        C = C % num


    for i in range(len(result)):
        print(result[i], end = ' ')