# [프로그래머스 Level 1] - 제일 작은 수 제거하기 
# 블로그 주소 : https://tteum.tistory.com/170

def solution(arr):
    answer = []
    
    if len(arr) == 1:
        answer.append(-1)
    else :
        arr.remove(min(arr))
        answer = arr
    return answer