# [백준] 1075번 - 나누기
# 블로그 주소 : https://tteum.tistory.com/310

n = int(input())
f = int(input())

tmp = (n // 100) * 100

a = f - ( tmp % f )

if a == f :
    print("00")
else :
    if len(str(a)) == 1:
        print("0",end='')
        print(a)
    else :
        print(a)