# [프로그래머스 Level 1] - 짝수와 홀수
# 블로그 주소 : https://tteum.tistory.com/181

def solution(num):
    answer = ''
    
    if num % 2 == 0 :
        answer = 'Even'
    else : answer = 'Odd'
    
    return answer