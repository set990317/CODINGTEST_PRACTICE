# [백준] 2750번 - 수 정렬하기
# 블로그 주소 : https://tteum.tistory.com/301

n = int(input())
arr=[]

for i in range(0,n):
    arr.append(int(input()))

for i in range(n, 0, -1):
    for j in range(0,i-1):
        if arr[j]>arr[j+1]:
            tmp = arr[j+1];
            arr[j+1] = arr[j];
            arr[j]=tmp;

for i in range(0,n):
    print(arr[i])