# [프로그래머스 Level 1] - 예산
# 블로그 주소 : https://tteum.tistory.com/152

def solution(d, budget):
    answer = 0
    d.sort()
    for num in d:
        budget -= num
        if budget < 0 :
            return answer        
        else : 
            answer += 1
    return answer