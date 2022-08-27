# [백준] 2576번 - 홀수
# 블로그 주소 : https://tteum.tistory.com/309

tmp = []
odd = []

for _ in range(7):
    tmp.append(int(input()))

for num in tmp:
    if num % 2 != 0 :
        odd.append(num)

if len(odd) != 0:
    print(sum(odd))
    print(min(odd))
else :
    print(-1)