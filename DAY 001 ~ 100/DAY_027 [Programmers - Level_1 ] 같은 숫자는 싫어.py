# [프로그래머스 Level 1] - 같은 숫자는 싫어
# 블로그 주소 : https://tteum.tistory.com/159

def solution(arr):
    num = arr[0]
    answer = []
    for i in arr :
        if i != num :
            answer.append(num)
            num = i
    answer.append(num)
    return answer