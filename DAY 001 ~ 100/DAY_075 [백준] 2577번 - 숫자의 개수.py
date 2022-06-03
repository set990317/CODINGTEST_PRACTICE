# [백준] 2577번 - 숫자의 개수
# 블로그 주소 : https://tteum.tistory.com/209

a = int(input())
b = int(input())
c = int(input())

result = a * b * c

arr = list(str(result))

for i in range(0,10):
    print(arr.count(str(i)))