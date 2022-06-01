# [백준] 1110번 - 더하기 사이클
# 블로그 주소 : https://tteum.tistory.com/206

n = int(input())
tmp = 0 # 계속 바뀔 예정인 변수
count = 0
n_list = list(str(n))

if len(n_list) == 1 :
    n_list.insert(0,0)
    
while (True):
    plus = str(int(n_list[0]) + int(n_list[1]))
    if len(plus) == 2 :
        plus = plus[-1]
    tmp = str(n_list[1]) + plus
    count += 1
    n_list = list(str(tmp))
    if int(tmp) == n:
        break

print(count)