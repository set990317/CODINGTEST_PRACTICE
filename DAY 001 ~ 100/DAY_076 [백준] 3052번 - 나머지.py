# [백준] 3052번 - 나머지
# 블로그 주소 : https://tteum.tistory.com/210

arr = []

for _ in range(10):
    n = int(input()) % 42
    arr.append(n)

arr = list(set(arr))

print(len(arr))