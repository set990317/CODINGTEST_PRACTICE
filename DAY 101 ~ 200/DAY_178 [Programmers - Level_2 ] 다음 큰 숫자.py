# [프로그래머스 Level 2] - 다음 큰 숫자
# 블로그 주소 : https://tteum.tistory.com/360

def solution(n):
    answer = 0
    one_count = format(n, 'b').count('1')
    
    while(answer == 0):
        n += 1
        tmp = format(n, 'b').count('1')
        
        if tmp == one_count:
            answer = n
            
    return answer