# [프로그래머스 코딩테스트 입문] - 모스부호 (1)
# 블로그 주소 : https://tteum.tistory.com/374

def solution(n, t):
    
    for i in range(t):
        n = n * 2
    answer = n
    
    return answer