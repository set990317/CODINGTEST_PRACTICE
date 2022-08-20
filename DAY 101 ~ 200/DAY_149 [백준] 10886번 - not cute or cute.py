s# [백준] 10886번 - 0 = not cute / 1 = cute
# 블로그 주소 : https://tteum.tistory.com/302

n = int(input())
total = 0

for _ in range(n):
    a = int(input())

    if a == 0 :
        total -= 1
    else :
        total += 1

if total < 0 :
    print("Junhee is not cute!")
else :
    print("Junhee is cute!")
