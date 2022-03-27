# [프로그래머스 Level 1] - x만큼 간격이 있는 n개의 숫자
# 블로그 주소 : https://tteum.tistory.com/136

def solution(x, n):
    answer = []
    answer.append(x)

    for i in range(2,n+1):
        answer.append(x*i)

    return answer