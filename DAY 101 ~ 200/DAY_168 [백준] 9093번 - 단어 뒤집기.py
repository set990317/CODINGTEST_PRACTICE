# [백준] 9093번 - 단어 뒤집기
# 블로그 주소 : https://tteum.tistory.com/325

import sys

T = int(input())
for _ in range(T):
    text = list(map(str,sys.stdin.readline().split()))
    result = []

    for i in range(len(text)):
        string = list(str(text[i]))
        string.reverse()
        s = "".join(string)
        result.append(s)

    for i in range(len(result)):
        print(result[i], end = ' ')