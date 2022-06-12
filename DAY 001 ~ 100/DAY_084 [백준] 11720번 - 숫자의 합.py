# [백준] 11720번 - 숫자의 합
# 블로그 주소 : https://tteum.tistory.com/219

n = int(input())
arr = str(input())
result = 0

for i in range(len(arr)):
    result += int(arr[i])

print(result)