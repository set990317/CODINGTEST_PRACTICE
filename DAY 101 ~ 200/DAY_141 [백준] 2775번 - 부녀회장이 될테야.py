# [백준] 2775번 - 부녀회장이 될테야
# 블로그 주소 : https://tteum.tistory.com/290

T = int(input())

for _ in range(T):

    k = int(input())
    n = int(input())

    people = [1,2,3,4,5,6,7,8,9,10,11,12,13,14]

    for i in range(k):
        for j in range(1,n):
            people[j] += people[j-1]

    print(people[n-1])