# [백준] 4948번 - 베르트랑 공준
# 블로그 주소 : https://tteum.tistory.com/300

def prime(k):
    if k == 1 :
        return 0

    for i in range(2, int(k ** 0.5) + 1):
        if k % i == 0 :
            return 0
    return 1

prime_list = []

for i in range(2,123456*2+1):
    if prime(i):
        prime_list.append(i)

while True:
    n = int(input())

    if n == 0:
        break
    cnt = 0
    for i in prime_list:
        if i > 2*n :
            break
        elif n < i <= 2*n :
            cnt += 1

    print(cnt)