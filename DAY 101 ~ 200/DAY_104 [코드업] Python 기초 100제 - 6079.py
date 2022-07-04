# [코드업] Python 기초 100제 - 6079
# 블로그 주소 : https://tteum.tistory.com/241

n = int(input())
total = 0

for i in range(1,n+1):
    if (total < n) :
        total += i
        max = i
    else :
        break

print(max)