# [프로그래머스 Level 1] - 자연수 뒤집어 배열로 만들기 
# 블로그 주소 : https://tteum.tistory.com/168

def solution(n):
    answer = []
    n_list = list(map(int, str(n)))
    
    for i in range(len(n_list)-1, -1, -1):
        answer.append(n_list[i])

    return answer