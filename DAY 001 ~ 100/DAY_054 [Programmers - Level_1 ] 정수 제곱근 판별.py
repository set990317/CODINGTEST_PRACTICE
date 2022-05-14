# [프로그래머스 Level 1] - 정수 제곱근 판별
# 블로그 주소 : https://tteum.tistory.com/187

def solution(n):
    answer = 0
    num = n ** 0.5
    
    if n == int(num) ** 2:
        answer = ( int(num) + 1 ) ** 2
    else : answer = -1
    
    return answer