# [백준] 2231번 - 분해합
# 블로그 주소 : https://tteum.tistory.com/295

n = int(input())
answer = 0

for num in range(1,n):
    tmp_list = list(map(int,str(num)))
    if sum(tmp_list) + num == n :
        answer = num
        break

print(answer)