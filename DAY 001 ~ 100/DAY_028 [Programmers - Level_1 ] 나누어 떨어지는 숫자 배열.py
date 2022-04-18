# [프로그래머스 Level 1] - 나누어 떨어지는 숫자 배열
# 블로그 주소 : https://tteum.tistory.com/160

def solution(arr, divisor):
    answer = []

    arr.sort()
    for num in arr :
        if num % divisor == 0:
            answer.append(num)
    
    if len(answer) != 0 :
        return answer
    else : 
        answer.append(-1)
        return answer