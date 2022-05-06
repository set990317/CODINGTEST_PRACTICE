# [프로그래머스 Level 1] - 자릿수 더하기
# 블로그 주소 : https://tteum.tistory.com/179

def solution(n):

    n_list = list(map(int, str(n)))
    answer = sum(n_list)
    
    return answer