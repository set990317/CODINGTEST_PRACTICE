# [백준] 2920번 - 음계
# 블로그 주소 : https://tteum.tistory.com/307

import sys

num = list(map(int,sys.stdin.readline().split()))
result = 'mixed'

if num[0] == 1 :
    answer = 1
    result = 'ascending'

    for i in range(len(num)):
        if num[i] != answer :
            result = 'mixed'
            break
        answer += 1

elif num[0] == 8 :
    answer = 8
    result = 'descending'

    for i in range(len(num)):
        if num[i] != answer:
            result = 'mixed'
            break
        answer -= 1

print(result)