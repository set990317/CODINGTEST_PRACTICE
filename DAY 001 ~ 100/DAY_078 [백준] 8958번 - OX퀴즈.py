# [백준] 8958번 - OX퀴즈
# 블로그 주소 : https://tteum.tistory.com/212

n = int(input())

for _ in range(n):

    arr = list(map(str,input()))
    stack = 0
    result = 0

    for i in range(len(arr)):
        if arr[i] == 'O':
            result += 1 + stack
            stack += 1
        else :
            stack = 0

    print(result)