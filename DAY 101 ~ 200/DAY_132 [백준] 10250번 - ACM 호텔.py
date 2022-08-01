# [코드업] 10250번 - ACM 호텔
# 블로그 주소 : https://tteum.tistory.com/281

T =int(input())

for _ in range(T):

    h, w, n = map(int,input().split())

    if n % h == 0 :
        room = h * 100 + n // h
    else :
        room = (n % h) * 100 + (n // h) + 1

    print(room)