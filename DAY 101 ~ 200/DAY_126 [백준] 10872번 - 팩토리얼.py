# [백준] 10872번 - 팩토리얼
# 블로그 주소 : https://tteum.tistory.com/270

def factorial(num):
    if num > 1:
        return num * factorial(num-1)
    else : 
        return 1

n = int(input())
print(factorial(n))