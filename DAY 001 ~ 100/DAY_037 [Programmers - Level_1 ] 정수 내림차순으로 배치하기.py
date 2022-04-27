# [프로그래머스 Level 1] - 정수 내림차순으로 배치하기 
# 블로그 주소 : https://tteum.tistory.com/169

def solution(n):
    answer = 0
    n = int(n)
    n_list = list(map(int, str(n)))
    n_list.sort(reverse=True)
    
    answer = ''.join(str(_) for _ in n_list)
    
    return int(answer)