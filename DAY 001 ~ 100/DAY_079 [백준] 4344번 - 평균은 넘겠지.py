# [백준] 4344번 - 평균은 넘겠지
# 블로그 주소 : https://tteum.tistory.com/213

import sys

n = int(input())

for _ in range(n):
    arr = list(map(int,sys.stdin.readline().split()))
    average = (sum(arr)-arr[0]) / arr[0]
    good = 0

    for i in range(1,arr[0]+1):
        if arr[i] > average :
            good += 1
            
    print('{:.3f}%'.format((good/arr[0])*100))