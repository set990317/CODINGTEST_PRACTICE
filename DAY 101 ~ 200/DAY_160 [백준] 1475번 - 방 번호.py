# [백준] 1475번 - 방 번호
# 블로그 주소 : https://tteum.tistory.com/313

string = str(input())
string = string.replace('6','9')
num = list(map(int,string))

total = 0

for i in range(0,10):
    if i in num:
        if total < num.count(i) :
            if i == 9:
                total = num.count(i) // 2 + num.count(i) % 2
            else:
                total = num.count(i)

print(total)