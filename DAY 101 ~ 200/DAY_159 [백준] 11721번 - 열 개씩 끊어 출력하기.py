# [백준] 11721번 - 열 개씩 끊어 출력하기
# 블로그 주소 : https://tteum.tistory.com/312

string = str(input())
count = 0
for i in range(len(string)):
    if count == 9:
        print(string[i], end='')
        print("")
        count = 0
    else :
        print(string[i], end = '')
        count += 1