# [백준] 2441번 - 별 찍기 4
# 블로그 주소 : https://tteum.tistory.com/304

n = int(input())

for i in range(n,0,-1):
    print(" "*(n-i),end='')
    print("*"*i)