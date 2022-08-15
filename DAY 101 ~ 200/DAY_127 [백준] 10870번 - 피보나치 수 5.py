# [백준] 10870번 - 피보나치 수 5
# 블로그 주소 : https://tteum.tistory.com/272

def fibo(num):
    if num == 0 :
        return 0
    elif num == 1 :
        return 1
    else :
        return fibo(num-1) + fibo(num-2)

n = int(input())
print(fibo(n))