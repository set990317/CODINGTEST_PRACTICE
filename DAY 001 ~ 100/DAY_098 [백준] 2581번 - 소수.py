# [백준] 2581번 - 소수
# 블로그 주소 : https://tteum.tistory.com/233

def sosu (num):
    if num == 1 :
        return 0
    for i in range(2,num):
        if num % i == 0:
            return 0
    arr.append(num)
    return 0

n = int(input())
m = int(input())
arr = []

for num in range(n,m+1):
    sosu(num)

if sum(arr) == 0 :
    print(-1)
else :
    print(sum(arr))
    print(arr[0])
    