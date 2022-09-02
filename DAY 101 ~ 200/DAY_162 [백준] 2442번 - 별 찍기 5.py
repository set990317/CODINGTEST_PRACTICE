# [백준] 2442번 - 별 찍기 5
# 블로그 주소 : https://tteum.tistory.com/315

n = int(input())
total = 2 * n - 1

for i in range(1,n+1):
    print(' ' * ((total-(2*i-1))//2), end='')
    print('*' * (2*i-1), end='')
    print("")