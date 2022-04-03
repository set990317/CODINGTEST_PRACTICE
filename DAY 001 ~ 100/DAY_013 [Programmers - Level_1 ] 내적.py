# [프로그래머스 Level 1] - 내적
# 블로그 주소 : https://tteum.tistory.com/144

# 첫번째 방법
def solution(a, b):
    answer = 0

    for i in range(0,len(a)):
        answer += a[i] * b[i]
    
    return answer

# 두번째 방법 - sum 사용
def solution(a, b):
    answer = 0

    for i in range(0,len(a)):
        a[i] = a[i] * b[i]
    
    answer = sum(a)
        
    return answer