# [코드업] Python 기초 100제 - 6077
# 블로그 주소 : https://tteum.tistory.com/236

n = int(input())
result = 0

for num in range(1,n+1):
    if num % 2 == 0:
        result += num
        
print(result)