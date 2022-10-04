# [프로그래머스 코딩테스트 입문] - 배열의 유사도
# 블로그 주소 : https://tteum.tistory.com/376

def solution(s1, s2):
    answer = 0
    
    for i in range(len(s1)):
        if s1[i] in s2 :
            answer += 1
            
    return answer