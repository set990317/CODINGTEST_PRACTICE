# [코드업] 7568번 - 덩치
# 블로그 주소 : https://tteum.tistory.com/291

import sys

n = int(input())
people = []
result = []

for _ in range(n):
    people.append(list(map(int,sys.stdin.readline().split())))

for i in range(len(people)):
    kg = people[i][0]
    cm = people[i][1]
    count = 0
    for j in range(len(people)):
        if kg < people[j][0] and cm < people[j][1]:
            count += 1
    result.append(count+1)

for i in range(len(result)):
    print(result[i], end =' ')