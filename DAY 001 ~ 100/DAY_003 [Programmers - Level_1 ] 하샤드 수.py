# [프로그래머스 Level 1] - 하샤드 수
# 블로그 주소 : https://tteum.tistory.com/131

def solution(x):
    answer = True
    x_list = list(map(int, str(x)))
    if x % sum(x_list) == 0:
        return answer
    else : 
        answer = False
        return answer