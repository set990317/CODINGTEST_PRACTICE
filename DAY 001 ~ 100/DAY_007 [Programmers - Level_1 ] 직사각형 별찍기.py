# [프로그래머스 Level 1] - 직사각형 별찍기
# 블로그 주소 : https://tteum.tistory.com/137

a, b = map(int, input().strip().split(' '))

for i in range(b):
    for j in range(a):
        print("*",end = '')
    print("")