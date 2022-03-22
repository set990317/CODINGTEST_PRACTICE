# [프로그래머스 Level 1] - 콜라츠 추측
# 블로그 주소 : https://tteum.tistory.com/129

def solution(num):
    answer = -1
    
    if num == 1:
        answer = 0
        return answer
    
    for i in range(0,501):
        if num % 2 == 0 :
            num /= 2
        else :
            num = num * 3 + 1
        if num == 1 :
            answer = i + 1
            break;

    return answer