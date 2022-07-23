# [코드업] 1003번 - 피보나치 함수
# 블로그 주소 : https://tteum.tistory.com/266

def fibo(n):
    length = len(zero)

    if length <= n :
        for i in range(length,n+1):
            zero.append(zero[i-1]+zero[i-2])
            one.append(one[i-1]+one[i-2])
    print(zero[n], one[n])

zero = [1,0,1]
one = [0,1,1]

T = int(input())

for _ in range(T):
    n = int(input())
    fibo(n)