# [백준] 2562번 - 최댓값
# 블로그 주소 : https://tteum.tistory.com/208

arr = []

for _ in range(9):
    n = int(input())
    arr.append(n)

max = max(arr)

print(max)
print(arr.index(max)+1)