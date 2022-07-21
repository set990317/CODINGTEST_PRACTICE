# [코드업] 2839번 - 설탕 배달
# 블로그 주소 : https://tteum.tistory.com/264

n = int(input())
result = -1

for i in range(0,n):
    tmp = n - (3 * i)
    if tmp % 5 == 0 or tmp == 0:
        if tmp < 0 :
            continue
        result = i + (tmp // 5)
        break

print(result)