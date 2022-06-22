# [백준] 1712번 - 손익분기점
# 블로그 주소 : https://tteum.tistory.com/228

a, b, c = map(int,input().split())
n = 0

if b >= c:
    n = -1
else :
    num = c - b
    n = int(a / num) + 1

print(n)