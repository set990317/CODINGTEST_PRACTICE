# [백준] 5622번 - 다이얼
# 블로그 주소 : https://tteum.tistory.com/225

import sys

s = str(sys.stdin.readline())
dial = ['ABC','DEF','GHI','JKL','MNO','PQRS','TUV','WXYZ']
sum = 0
for char in s:
    for i in range(len(dial)):
        if char in dial[i] :
            sum = sum + ( i + 3 )
print(sum)