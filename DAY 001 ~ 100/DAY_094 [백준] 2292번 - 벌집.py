# [백준] 2292번 - 벌집
# 블로그 주소 : https://tteum.tistory.com/229

n = int(input())

i = 0
cnt = 1
total = 1

while(True):
    total += (6 * i)

    if total >= n :
        break
    else :
        i += 1
        cnt += 1

print(cnt)