# [백준] 2439번 - 별 찍기 - 2
# 블로그 주소 : https://tteum.tistory.com/202

n = int(input())

for i in range(1,n+1):
    print(' ' * (n-i) + '*' * i)