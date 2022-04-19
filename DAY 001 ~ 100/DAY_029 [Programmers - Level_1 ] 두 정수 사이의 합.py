# [프로그래머스 Level 1] - 두 정수 사이의 합
# 블로그 주소 : https://tteum.tistory.com/161

# 첫 번째 코드 - 큰 수 합에서 작은 수 합 빼는 방식 
def solution(a, b):
                    
    if a == b :
        return a
    if a > b :
        n1 = a * (a + 1) // 2
        n2 = (b - 1) * b // 2
        return n1 - n2
    else :
        n1 = (a - 1) * a // 2
        n2 = b * (b + 1) // 2
        return n2 - n1

# 두 번째 코드 - min, max 사용
def solution(a, b):
    answer = 0;
    a, b = min(a,b), max(a,b)
    
    for num in range(a,b+1):
        answer += num
    
    return answer