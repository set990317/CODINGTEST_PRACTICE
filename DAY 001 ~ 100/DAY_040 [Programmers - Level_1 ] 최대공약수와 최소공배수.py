# [프로그래머스 Level 1] - 약수의 합
# 블로그 주소 : https://tteum.tistory.com/172

def solution(n):
    answer = 0
    
    for i in range(1,n+1):
        if n % i == 0:
            answer += i
    return answer