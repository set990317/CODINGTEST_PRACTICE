# [코드업] 18310번 - 안테나
# 블로그 주소 : https://tteum.tistory.com/283

N = int(input())
data = list(map(int, input().split()))
data.sort()
 
print(data[(N-1)//2])