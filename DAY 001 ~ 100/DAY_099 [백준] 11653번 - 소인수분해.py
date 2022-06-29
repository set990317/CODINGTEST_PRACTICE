# [백준] 11653번 - 소인수분해
# 블로그 주소 : https://tteum.tistory.com/234

n = int(input())

while (n > 1):
    for i in range(2,n+1):
        if n % i == 0 :
            n = n // i
            print(i)
            break